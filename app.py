import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Analizor de Compatibilitate", page_icon="💜", layout="centered")

st.markdown("""
<style>
    .block-container { max-width: 700px; padding-top: 2rem; padding-bottom: 3rem; }
    div[data-testid="metric-container"] {
        background: #f5f3ff;
        border-radius: 12px;
        padding: 1rem;
        border: 0.5px solid #ded8f5;
    }
    .stRadio > label { font-size: 15px; font-weight: 500; }
    .stSlider > label { font-size: 14px; color: #555; }
    div[data-baseweb="slider"] { padding: 0 4px; }
    .stButton > button {
        border-radius: 10px;
        font-weight: 500;
        height: 46px;
        transition: all .2s;
    }
    hr { margin: 1.5rem 0; border-color: #eee; }
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

# ── SESIUNE ───────────────────────────────────────────────────────────────────
if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

def reset():
    st.session_state.step = 1

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;padding:1rem 0 1.5rem'>
  <div style='font-size:48px;margin-bottom:8px'>💜</div>
  <h1 style='font-size:22px;font-weight:600;margin:0 0 6px'>Analizor de Compatibilitate Relațională</h1>
  <p style='color:#888;font-size:14px;margin:0'>Trei pași simpli. Un raport detaliat despre ce simți.<br>Instrument de reflecție personală — nu un diagnostic.</p>
</div>
""", unsafe_allow_html=True)

# ── PROGRESS BAR ──────────────────────────────────────────────────────────────
step = st.session_state.step
progress = (step - 1) / 3
labels = ["Context", "Atracție", "Conectivitate", "Raport"]
cols_prog = st.columns(4)
for i, (col, label) in enumerate(zip(cols_prog, labels)):
    with col:
        if i + 1 < step:
            st.markdown(f"<div style='text-align:center'><div style='width:30px;height:30px;border-radius:50%;background:#1D9E75;color:white;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:14px'>✓</div><div style='font-size:11px;color:#1D9E75;font-weight:500'>{label}</div></div>", unsafe_allow_html=True)
        elif i + 1 == step:
            st.markdown(f"<div style='text-align:center'><div style='width:30px;height:30px;border-radius:50%;background:#534AB7;color:white;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:14px;font-weight:600'>{i+1}</div><div style='font-size:11px;color:#534AB7;font-weight:600'>{label}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:center'><div style='width:30px;height:30px;border-radius:50%;background:#f0f0f0;color:#aaa;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:14px'>{i+1}</div><div style='font-size:11px;color:#aaa'>{label}</div></div>", unsafe_allow_html=True)

st.progress(progress, text="")
st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 1 — CONTEXT
# ════════════════════════════════════════════════════════════════════════════
if step == 1:
    st.markdown("### Care este starea actuală a relației?")
    st.caption("Alege situația care descrie cel mai bine contextul vostru în acest moment.")
    st.markdown("<br>", unsafe_allow_html=True)

    context = st.radio(
        "context",
        options=[
            "💚 Aliniere Deschisă — Suntem împreună / Sentimente confirmate reciproc",
            "🟡 Canal Parțial Blocat — Conexiune profundă, dar suntem amici / altă relație / distanță",
            "🔴 Asimetrie Neconfirmată — Simt conexiunea, dar cealaltă persoană nu o cunoaște sau nu o împărtășește",
        ],
        label_visibility="collapsed"
    )
    st.session_state.context = context
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Continuă →", type="primary", use_container_width=True, on_click=next_step):
        pass

# ════════════════════════════════════════════════════════════════════════════
# PASUL 2 — ATRACTIE
# ════════════════════════════════════════════════════════════════════════════
elif step == 2:
    st.markdown("### Atracție și interes")
    st.caption("Cât de intens ești atras și cât de prezentă este această persoană în gândurile tale?")
    st.markdown("<br>", unsafe_allow_html=True)

    q1 = st.slider("1. **Dorul și Gândul** — Cât de des apar gânduri legate de această persoană când nu sunteți în același loc?", 1, 10, st.session_state.get('q1', 5), help="1 = Rar / 10 = Constant")
    q2 = st.slider("2. **Chimia și Atingerea** — Cât de puternic este magnetismul sau emoția intensă la o apropiere fizică?", 1, 10, st.session_state.get('q2', 5), help="1 = Neutru / 10 = Foarte puternic")
    q3 = st.slider("3. **Focalizarea** — Cât de prima persoană este când vrei să împărtășești o bucurie sau o problemă?", 1, 10, st.session_state.get('q3', 5), help="1 = Nu prima / 10 = Mereu prima")
    q4 = st.slider("4. **Declanșatorul de Bucurie** — Cât de ușor reușește să te facă să zâmbești dintr-o privire sau un mesaj?", 1, 10, st.session_state.get('q4', 5), help="1 = Greu / 10 = Instantaneu")
    q5 = st.slider("5. **Model și Sprijin** — În ce măsură te stimulează să evoluezi și îți oferă sprijin emoțional?", 1, 10, st.session_state.get('q5', 5), help="1 = Deloc / 10 = Enorm")

    st.session_state.q1 = q1
    st.session_state.q2 = q2
    st.session_state.q3 = q3
    st.session_state.q4 = q4
    st.session_state.q5 = q5

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2:
        st.button("Continuă →", type="primary", on_click=next_step, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 3 — CONECTIVITATE
# ════════════════════════════════════════════════════════════════════════════
elif step == 3:
    st.markdown("### Conectivitate și deschidere")
    st.caption("Cât de profundă și fluidă este comunicarea și încrederea dintre voi?")
    st.markdown("<br>", unsafe_allow_html=True)

    q6  = st.slider("6. **Deschiderea și Destăinuirea** — Cât de ușor îți este să te destăinui și să îți arăți vulnerabilitățile fără frică?", 1, 10, st.session_state.get('q6', 5), help="1 = Dificil / 10 = Complet natural")
    q7  = st.slider("7. **Empatia și Co-rezonanța** — Cât de mult te influențează direct starea lui/ei de spirit sau de sănătate?", 1, 10, st.session_state.get('q7', 5), help="1 = Deloc / 10 = Profund")
    q8  = st.slider("8. **Sincronicitatea** — Cât de des experimentați momente sincrone (spuneți același lucru, vă căutați în același timp)?", 1, 10, st.session_state.get('q8', 5), help="1 = Niciodată / 10 = Frecvent")
    q9  = st.slider("9. **Fluiditatea și Rezoluția** — Cât de repede și curat se dizolvă neînțelegerile fără să rămână răceală?", 1, 10, st.session_state.get('q9', 5), help="1 = Greu / 10 = Foarte ușor")
    q10 = st.slider("10. **Siguranța și Pacea** — Cât de profundă este starea de liniște și siguranță pe care o simți în prezența sa?", 1, 10, st.session_state.get('q10', 5), help="1 = Anxios / 10 = Complet în pace")

    st.session_state.q6  = q6
    st.session_state.q7  = q7
    st.session_state.q8  = q8
    st.session_state.q9  = q9
    st.session_state.q10 = q10

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2:
        if st.button("💜 Calculează Raportul", type="primary", use_container_width=True):
            next_step()

# ════════════════════════════════════════════════════════════════════════════
# PASUL 4 — REZULTATE
# ════════════════════════════════════════════════════════════════════════════
elif step == 4:
    q1  = st.session_state.get('q1', 5)
    q2  = st.session_state.get('q2', 5)
    q3  = st.session_state.get('q3', 5)
    q4  = st.session_state.get('q4', 5)
    q5  = st.session_state.get('q5', 5)
    q6  = st.session_state.get('q6', 5)
    q7  = st.session_state.get('q7', 5)
    q8  = st.session_state.get('q8', 5)
    q9  = st.session_state.get('q9', 5)
    q10 = st.session_state.get('q10', 5)
    context = st.session_state.get('context', '')

    atractie = (q1+q2+q3+q4+q5) / 5
    conectiv = (q6+q7+q8+q9+q10) / 5
    compatib = (atractie+conectiv) / 2

    if "Aliniere" in context:
        penaliz, ctx_label, ctx_desc = 0, "Aliniere Deschisă", "Contextul este complet favorabil. Energia relației circulă liber în ambele sensuri, fără obstacole."
        ctx_color = "#1D9E75"
    elif "Parțial" in context or "Blocat" in context:
        penaliz, ctx_label, ctx_desc = 15, "Canal Parțial Blocat", "Există obstacole externe care limitează exprimarea naturală a conexiunii voastre. Energia există, dar e parțial blocată de circumstanțe."
        ctx_color = "#BA7517"
    else:
        penaliz, ctx_label, ctx_desc = 30, "Asimetrie Neconfirmată", "Decalajul dintre ce simți tu și ce știe/simte cealaltă persoană creează o presiune internă semnificativă."
        ctx_color = "#A32D2D"

    final = max(0, min(100, compatib * 10 - penaliz))

    # Scor și stare
    if final >= 75:
        emoji_status = "🟢"
        status_title = "Conexiune Puternică și Echilibrată"
        status_color = "#534AB7"
        bg_color = "#EEEDFE"
        insight = "Relația ta are fundații solide pe ambele planuri — ești atras puternic și în același timp te simți în siguranță și deschis. Această combinație e rară și valoroasă. Dacă nu ați deschis deja comunicarea despre ce simțiți, acum este momentul potrivit."
        st.balloons()
    elif final >= 55:
        emoji_status = "🔵"
        status_title = "Potrivire Bună cu Zone de Crescut"
        status_color = "#185FA5"
        bg_color = "#E6F1FB"
        insight = "Există o fundație reală și autentică. Atracția este prezentă și conexiunea funcționează, dar există una sau două dimensiuni unde legătura nu e încă profundă. Identifică ce dimensiune a ieșit cel mai slab și gândește-te concret cum poate fi cultivată."
    elif final >= 35:
        emoji_status = "🟡"
        status_title = "Atracție Prezentă, Echilibru în Construcție"
        status_color = "#BA7517"
        bg_color = "#FAEEDA"
        insight = "Există atracție reală, dar un dezechilibru — fie conectivitatea nu a ajuns la nivelul atracției, fie contextul adaugă fricțiune semnificativă. Întreabă-te: problema vine din interior (deschidere, încredere) sau din exterior (circumstanțe, situație)?"
    else:
        emoji_status = "🔴"
        status_title = "Dezechilibru Semnificativ"
        status_color = "#A32D2D"
        bg_color = "#FCEBEB"
        insight = "Scorul reflectă fie un dezechilibru major între ce simți și ce există în realitate, fie o presiune externă puternică. Un scor mic nu înseamnă că relația e greșită — poate înseamnă că momentul sau contextul nu este potrivit acum."

    # Salvează
    vals = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
    salveaza({
        "Data/Ora": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Context": ctx_label, "Atractie": round(atractie,2),
        "Conectivitate": round(conectiv,2), "Scor Brut": round(compatib*10,2),
        "Penalizare": penaliz, "Scor Final": round(final,2),
        "Q1":q1,"Q2":q2,"Q3":q3,"Q4":q4,"Q5":q5,
        "Q6":q6,"Q7":q7,"Q8":q8,"Q9":q9,"Q10":q10
    })

    # ── SCOR HERO ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style='background:{bg_color};border-radius:16px;padding:2rem;text-align:center;margin-bottom:1.5rem'>
      <div style='font-size:72px;font-weight:700;color:{status_color};line-height:1'>{int(final)}</div>
      <div style='font-size:13px;color:#999;margin-bottom:8px'>din 100</div>
      <div style='font-size:18px;font-weight:600;color:{status_color}'>{emoji_status} {status_title}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── METRICI ────────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    col1.metric("Atracție", f"{atractie:.1f}/10")
    col2.metric("Conectivitate", f"{conectiv:.1f}/10")
    col3.metric("Penalizare context", f"-{penaliz} pct")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── GRAFIC RADAR ───────────────────────────────────────────────────────
    labels_radar = ['Dor/Gând','Magnetism','Prioritate','Bucurie','Inspirație','Deschidere','Empatie','Sincron','Rezoluție','Siguranță']
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=vals+[vals[0]], theta=labels_radar+[labels_radar[0]],
        fill='toself', fillcolor='rgba(83,74,183,0.12)',
        line=dict(color='#534AB7', width=2), marker=dict(size=6, color='#534AB7'),
        name='Profilul tău'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=[7]*10+[7], theta=labels_radar+[labels_radar[0]],
        line=dict(color='#ccc', width=1, dash='dot'), showlegend=False
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0,10], tickfont=dict(size=10), gridcolor='#eee'),
            angularaxis=dict(tickfont=dict(size=12), gridcolor='#eee')
        ),
        showlegend=False,
        margin=dict(l=50, r=50, t=40, b=40),
        height=380,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=dict(text='Profil pe dimensiuni', font=dict(size=14, color='#555'), x=0.5)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # ── BAR CHART ──────────────────────────────────────────────────────────
    colors_bar = ['#534AB7']*5 + ['#1D9E75']*5
    fig_bar = go.Figure(go.Bar(
        x=labels_radar, y=vals,
        marker_color=colors_bar, marker_line_width=0,
        text=vals, textposition='outside', textfont=dict(size=12)
    ))
    fig_bar.update_layout(
        yaxis=dict(range=[0,12], showgrid=True, gridcolor='#f0f0f0', title='Scor /10'),
        xaxis=dict(showgrid=False, tickfont=dict(size=11)),
        margin=dict(l=20, r=20, t=40, b=20),
        height=320,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title=dict(text='Scoruri pe fiecare dimensiune', font=dict(size=14, color='#555'), x=0.5)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ── CEL MAI BUN / CEL MAI SLAB ────────────────────────────────────────
    all_items = list(zip(['Dor și Gând','Chimie','Prioritate','Bucurie','Inspirație','Deschidere','Empatie','Sincron','Rezoluție','Siguranță'], vals))
    max_item = max(all_items, key=lambda x: x[1])
    min_item = min(all_items, key=lambda x: x[1])

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success(f"**⭐ Cea mai puternică dimensiune**\n\n{max_item[0]}: **{max_item[1]}/10**\n\nAcesta este punctul tău de forță în această relație.")
    with col_e2:
        st.warning(f"**📈 Zona cu cel mai mult potențial**\n\n{min_item[0]}: **{min_item[1]}/10**\n\nAici există cel mai mult spațiu de crescut.")

    st.markdown("---")

    # ── INSIGHT ────────────────────────────────────────────────────────────
    st.markdown("### Ce înseamnă pentru tine")
    st.markdown(f"""
    <div style='background:{bg_color};border-left:3px solid {status_color};border-radius:0 12px 12px 0;padding:1.25rem 1.5rem;margin-bottom:1rem;line-height:1.7;color:#333'>
      {insight}
    </div>
    """, unsafe_allow_html=True)

    # ── CONTEXT ────────────────────────────────────────────────────────────
    st.markdown(f"**Context aplicat:** {ctx_label}")
    st.caption(ctx_desc)

    st.markdown("---")

    # ── BUTON RESET ────────────────────────────────────────────────────────
    st.button("🔄 Completează din nou", on_click=reset, use_container_width=True)

    # ── ISTORIC ────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋 Vezi toate rezultatele salvate"):
        df = incarca()
        if df.empty:
            st.info("Nu există rezultate salvate încă.")
        else:
            st.dataframe(df[["Data/Ora","Context","Atractie","Conectivitate","Scor Final"]], use_container_width=True)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Descarcă toate rezultatele (CSV)", csv, "rezultate.csv", "text/csv", use_container_width=True)
            st.caption(f"Total rezultate salvate: **{len(df)}**")

    st.markdown("---")
    st.caption("⚠️ Instrument de reflecție personală, nu un diagnostic psihologic sau științific. Scorurile reflectă exclusiv percepția ta subiectivă în acest moment.")

st.markdown("---")
st.caption("© 2026 Ciprian Axiniei · Instrument de reflecție relațională")
