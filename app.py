import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Analizor de Compatibilitate", page_icon="💜", layout="centered")

st.markdown("""
<style>
    .block-container { max-width: 720px; padding-top: 2rem; }
    div[data-testid="metric-container"] { background: #f7f7f5; border-radius: 10px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)

FISIER = "rezultate.csv"

def salveaza(row):
    df_nou = pd.DataFrame([row])
    if os.path.exists(FISIER):
        df_nou.to_csv(FISIER, mode='a', header=False, index=False)
    else:
        df_nou.to_csv(FISIER, index=False)

def incarca():
    if os.path.exists(FISIER):
        return pd.read_csv(FISIER)
    return pd.DataFrame()

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("💜 Analizor de Compatibilitate Relațională")
st.caption("Un instrument de reflecție personală — scorurile reflectă percepția ta subiectivă în acest moment.")
st.markdown("---")

st.subheader("1. Starea actuală a relației")
context = st.radio("context", (
    "Aliniere Deschisă — Suntem împreună / Sentimente confirmate reciproc",
    "Canal Parțial Blocat — Conexiune profundă, dar suntem doar amici / alte circumstanțe / distanță",
    "Asimetrie Neconfirmată — Simt conexiunea, dar cealaltă persoană nu o cunoaște sau nu o împărtășește"
), label_visibility="collapsed")

st.markdown("---")
st.subheader("2. Atracție și interes")
st.caption("Măsoară intensitatea atracției și cât de puternic te trage această persoană în orbita sa.")
q1 = st.slider("1. Dorul și Gândul — Cât de des apar gânduri legate de această persoană când nu sunteți în același loc?", 1, 10, 5)
q2 = st.slider("2. Chimia și Atingerea — Cât de puternic este magnetismul sau emoția intensă în corp la o apropiere fizică?", 1, 10, 5)
q3 = st.slider("3. Focalizarea — Cât de prima persoană este când vrei să împărtășești o bucurie sau o problemă?", 1, 10, 5)
q4 = st.slider("4. Declanșatorul de Bucurie — Cât de ușor reușește să te facă să zâmbești dintr-o privire sau un mesaj?", 1, 10, 5)
q5 = st.slider("5. Model și Sprijin — În ce măsură te stimulează să evoluezi și îți oferă sprijin emoțional?", 1, 10, 5)

st.markdown("---")
st.subheader("3. Conectivitate și deschidere")
st.caption("Măsoară cât de profund sunt cuplate sistemele voastre emoționale și cât de curată e comunicarea.")
q6 = st.slider("6. Deschiderea și Destăinuirea — Cât de ușor îți este să te destăinui fără frică?", 1, 10, 5)
q7 = st.slider("7. Empatia și Co-rezonanța — Cât de mult te influențează starea lui/ei de spirit?", 1, 10, 5)
q8 = st.slider("8. Sincronicitatea — Cât de des experimentați momente sincrone?", 1, 10, 5)
q9 = st.slider("9. Fluiditatea și Rezoluția — Cât de repede se dizolvă neînțelegerile?", 1, 10, 5)
q10 = st.slider("10. Siguranța și Pacea — Cât de profundă este liniștea pe care o simți în prezența sa?", 1, 10, 5)

st.markdown("---")

if st.button("💜 Calculează Raportul de Compatibilitate", type="primary", use_container_width=True):
    atractie = (q1 + q2 + q3 + q4 + q5) / 5
    conectiv = (q6 + q7 + q8 + q9 + q10) / 5
    compatib = (atractie + conectiv) / 2

    if "Aliniere" in context:
        penaliz, ctx_label, ctx_desc = 0, "Aliniere Deschisă", "Contextul este complet favorabil. Energia relației circulă liber în ambele sensuri."
    elif "Parțial" in context:
        penaliz, ctx_label, ctx_desc = 15, "Canal Parțial Blocat", "Există obstacole externe care limitează exprimarea naturală a conexiunii voastre."
    else:
        penaliz, ctx_label, ctx_desc = 30, "Asimetrie Neconfirmată", "Decalajul dintre ce simți tu și ce știe/simte cealaltă persoană creează o presiune internă semnificativă."

    final = max(0, min(100, compatib * 10 - penaliz))
    vals = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    salveaza({
        "Data/Ora": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Context": ctx_label,
        "Atractie": round(atractie, 2),
        "Conectivitate": round(conectiv, 2),
        "Scor Brut": round(compatib * 10, 2),
        "Penalizare": penaliz,
        "Scor Final": round(final, 2),
        "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5,
        "Q6": q6, "Q7": q7, "Q8": q8, "Q9": q9, "Q10": q10
    })
    st.toast("Rezultat salvat!", icon="✅")

    st.markdown("## 📊 Raport de Compatibilitate")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Atracție", f"{atractie:.1f}/10")
    col2.metric("Conectivitate", f"{conectiv:.1f}/10")
    col3.metric("Scor brut", f"{compatib*10:.0f}/100")
    col4.metric("Scor final", f"{final:.0f}/100", delta=f"-{penaliz} context" if penaliz > 0 else "fără penalizare")

    st.markdown("---")

    if final >= 75:
        st.success(f"""**🟢 Conexiune Puternică și Echilibrată — {final:.0f}/100**\n\nAtracția și conectivitatea sunt amândouă ridicate, iar contextul este favorabil. Relația ta are fundații solide pe ambele planuri.\n\n**Ce înseamnă asta pentru tine:** Relația are potențial real de profunzime și durabilitate. Dacă nu ați deschis deja comunicarea despre ce simțiți, acum este momentul potrivit.""")
    elif final >= 55:
        st.info(f"""**🔵 Potrivire Bună cu Zone de Crescut — {final:.0f}/100**\n\nExistă o fundație reală și autentică. Atracția este prezentă și conexiunea funcționează, dar există dimensiuni care pot fi aprofundate.\n\n**Ce înseamnă asta pentru tine:** Relația merită investiție. Identifică ce dimensiune a ieșit cel mai slab în graficul radar și gândește-te concret cum poate fi îmbunătățită.""")
    elif final >= 35:
        st.warning(f"""**🟡 Atracție Prezentă, Echilibru în Construcție — {final:.0f}/100**\n\nExistă interes și atracție reale, dar un dezechilibru — fie conectivitatea nu a ajuns la nivelul atracției, fie contextul adaugă fricțiune.\n\n**Ce înseamnă asta pentru tine:** Înțelege dacă scorul mic vine din interior (conectivitate slabă) sau din exterior (context nefavorabil). Răspunsul schimbă complet ce ai de făcut.""")
    else:
        st.error(f"""**🔴 Dezechilibru Semnificativ — {final:.0f}/100**\n\nFie un dezechilibru major între ce simți și ce există în realitate, fie o presiune externă care comprimă o conexiune altfel valoroasă.\n\n**Ce înseamnă asta pentru tine:** Merită o reflecție sinceră. Un scor mic nu înseamnă că relația e greșită — poate înseamnă că momentul sau contextul nu e potrivit.""")

    st.markdown("---")
    st.markdown(f"**Context aplicat: {ctx_label}**")
    st.caption(ctx_desc)

    labels = ['Dor/Gând','Magnetism','Prioritate','Bucurie','Inspirație','Deschidere','Empatie','Sincron','Rezoluție','Siguranță']
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Profil pe dimensiuni**")
        fig_radar = go.Figure(go.Scatterpolar(
            r=vals + [vals[0]], theta=labels + [labels[0]], fill='toself',
            fillcolor='rgba(83,74,183,0.15)', line=dict(color='#534AB7', width=2), marker=dict(size=5, color='#534AB7')
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,10], tickfont=dict(size=10)), angularaxis=dict(tickfont=dict(size=11))), showlegend=False, margin=dict(l=40,r=40,t=30,b=30), height=300)
        st.plotly_chart(fig_radar, use_container_width=True)
    with col_b:
        st.markdown("**Atracție vs conectivitate vs scor final**")
        fig_bar = go.Figure(go.Bar(x=['Atracție','Conectivitate','Scor /10'], y=[atractie, conectiv, final/10], marker_color=['#534AB7','#1D9E75','#BA7517'], marker_line_width=0, text=[f"{atractie:.1f}", f"{conectiv:.1f}", f"{final/10:.1f}"], textposition='outside'))
        fig_bar.update_layout(yaxis=dict(range=[0,12], showgrid=True, gridcolor='#eee'), xaxis=dict(showgrid=False), margin=dict(l=20,r=20,t=30,b=20), height=300, plot_bgcolor='white', paper_bgcolor='white')
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    all_items = list(zip(['Dor și Gând','Chimie','Prioritate','Bucurie','Inspirație','Deschidere','Empatie','Sincron','Rezoluție','Siguranță'], vals))
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.info(f"**Cea mai puternică dimensiune:** {max(all_items, key=lambda x: x[1])[0]} ({max(all_items, key=lambda x: x[1])[1]}/10)")
    with col_e2:
        st.warning(f"**Zona cu cel mai mult potențial:** {min(all_items, key=lambda x: x[1])[0]} ({min(all_items, key=lambda x: x[1])[1]}/10)")

    st.caption("⚠️ Instrument de reflecție personală, nu un diagnostic psihologic sau științific.")

# ── ISTORIC ───────────────────────────────────────────────────────────────────
st.markdown("---")
with st.expander("📋 Vezi toate rezultatele salvate"):
    df = incarca()
    if df.empty:
        st.info("Nu există rezultate salvate încă.")
    else:
        st.dataframe(df[["Data/Ora","Context","Atractie","Conectivitate","Scor Final"]], use_container_width=True)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Descarcă toate rezultatele (CSV)", csv, "rezultate.csv", "text/csv", use_container_width=True)
        st.caption(f"Total rezultate salvate: {len(df)}")

st.markdown("---")
st.caption("© 2026 Ciprian Axiniei · Instrument de reflecție relațională")
