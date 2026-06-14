import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Analizor de Compatibilitate", page_icon="💜", layout="centered")

st.markdown("""
<style>
    .block-container { max-width: 720px; padding-top: 2rem; }
    div[data-testid="metric-container"] { background: #f7f7f5; border-radius: 10px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)

st.title("💜 Analizor de Compatibilitate Relațională")
st.caption("Un instrument de reflecție personală — scorurile reflectă percepția ta subiectivă în acest moment.")
st.markdown("---")

# ── CONTEXT ──────────────────────────────────────────────────────────────────
st.subheader("1. Starea actuală a relației")
st.caption("Alege situația care descrie cel mai bine contextul vostru în acest moment.")
context = st.radio(
    "context",
    (
        "Aliniere Deschisă — Suntem împreună / Sentimente confirmate reciproc",
        "Canal Parțial Blocat — Conexiune profundă, dar suntem doar amici / alte circumstanțe / distanță",
        "Asimetrie Neconfirmată — Simt conexiunea, dar cealaltă persoană nu o cunoaște sau nu o împărtășește"
    ),
    label_visibility="collapsed"
)

st.markdown("---")

# ── SECTIUNEA ATRACTIE ────────────────────────────────────────────────────────
st.subheader("2. Atracție și interes")
st.caption("Măsoară intensitatea atracției și cât de puternic te trage această persoană în orbita sa.")

q1 = st.slider("1. Dorul și Gândul — Cât de des apar gânduri legate de această persoană când nu sunteți în același loc?", 1, 10, 5)
q2 = st.slider("2. Chimia și Atingerea — Cât de puternic este magnetismul sau emoția intensă în corp la o apropiere fizică?", 1, 10, 5)
q3 = st.slider("3. Focalizarea — Cât de prima persoană este când vrei să împărtășești o bucurie sau o problemă?", 1, 10, 5)
q4 = st.slider("4. Declanșatorul de Bucurie — Cât de ușor reușește să te facă să zâmbești dintr-o privire sau un mesaj?", 1, 10, 5)
q5 = st.slider("5. Model și Sprijin — În ce măsură este un exemplu din care înveți, te stimulează să evoluezi și îți oferă sprijin emoțional?", 1, 10, 5)

st.markdown("---")

# ── SECTIUNEA CONECTIVITATE ───────────────────────────────────────────────────
st.subheader("3. Conectivitate și deschidere")
st.caption("Măsoară cât de profund sunt cuplate sistemele voastre emoționale și cât de curată e comunicarea.")

q6 = st.slider("6. Deschiderea și Destăinuirea — Cât de ușor îți este să te destăinui și să îți arăți vulnerabilitățile fără frică?", 1, 10, 5)
q7 = st.slider("7. Empatia și Co-rezonanța — Cât de mult te influențează direct starea ei/lui de spirit sau de sănătate?", 1, 10, 5)
q8 = st.slider("8. Sincronicitatea — Cât de des experimentați momente sincrone (spuneți același lucru, vă căutați în același timp)?", 1, 10, 5)
q9 = st.slider("9. Fluiditatea și Rezoluția — Cât de repede și curat se dizolvă neînțelegerile fără să rămână răceală sau tensiune?", 1, 10, 5)
q10 = st.slider("10. Siguranța și Pacea — Cât de profundă este starea de liniște și siguranță pe care o simți în prezența sa?", 1, 10, 5)

st.markdown("---")

if st.button("💜 Calculează Raportul de Compatibilitate", type="primary", use_container_width=True):

    atractie = (q1 + q2 + q3 + q4 + q5) / 5
    conectiv = (q6 + q7 + q8 + q9 + q10) / 5
    compatib = (atractie + conectiv) / 2

    if "Aliniere" in context:
        penaliz = 0
        ctx_label = "Aliniere Deschisă"
        ctx_desc = "Contextul este complet favorabil. Energia relației circulă liber în ambele sensuri."
    elif "Parțial" in context:
        penaliz = 15
        ctx_label = "Canal Parțial Blocat"
        ctx_desc = "Există obstacole externe care limitează exprimarea naturală a conexiunii voastre."
    else:
        penaliz = 30
        ctx_label = "Asimetrie Neconfirmată"
        ctx_desc = "Decalajul dintre ce simți tu și ce știe/simte cealaltă persoană creează o presiune internă semnificativă."

    final = max(0, min(100, compatib * 10 - penaliz))

    # ── SCORURI ───────────────────────────────────────────────────────────────
    st.markdown("## 📊 Raport de Compatibilitate")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Atracție", f"{atractie:.1f}/10")
    col2.metric("Conectivitate", f"{conectiv:.1f}/10")
    col3.metric("Scor brut", f"{compatib*10:.0f}/100")
    col4.metric("Scor final", f"{final:.0f}/100", delta=f"-{penaliz} context" if penaliz > 0 else "fără penalizare")

    st.markdown("---")

    # ── STATUS PRINCIPAL ──────────────────────────────────────────────────────
    if final >= 75:
        st.success(f"""
**🟢 Conexiune Puternică și Echilibrată — {final:.0f}/100**

Atracția și conectivitatea sunt amândouă ridicate, iar contextul este favorabil. 
Relația ta are fundații solide pe ambele planuri — ești atras puternic și în același timp 
te simți în siguranță și deschis. Aceasta este o combinație rară și valoroasă.

**Ce înseamnă asta pentru tine:** Relația are potențial real de profunzime și durabilitate. 
Dacă nu ați deschis deja comunicarea despre ce simțiți, acum este momentul potrivit.
        """)
    elif final >= 55:
        st.info(f"""
**🔵 Potrivire Bună cu Zone de Crescut — {final:.0f}/100**

Există o fundație reală și autentică. Scorul tău arată că atracția este prezentă 
și conexiunea emoțională funcționează, dar există câteva dimensiuni care pot fi 
aprofundate — fie în comunicare, fie în exprimarea vulnerabilității.

**Ce înseamnă asta pentru tine:** Relația merită investiție. Identifică ce dimensiune 
a ieșit cel mai slab în graficul radar și gândește-te concret cum poate fi îmbunătățită.
        """)
    elif final >= 35:
        st.warning(f"""
**🟡 Atracție Prezentă, Echilibru în Construcție — {final:.0f}/100**

Scorul arată un interes și o atracție reale, dar există un dezechilibru — fie 
conectivitatea emoțională nu a ajuns la nivelul atracției, fie contextul actual 
(circumstanțe, distanță, situație) adaugă o fricțiune semnificativă.

**Ce înseamnă asta pentru tine:** Este important să înțelegi dacă scorul mic vine 
din interior (conectivitate slabă) sau din exterior (context nefavorabil). 
Răspunsul schimbă complet ce ai de făcut în continuare.
        """)
    else:
        st.error(f"""
**🔴 Dezechilibru Semnificativ — {final:.0f}/100**

Scorul reflectă fie un dezechilibru major între ce simți și ce există în realitate, 
fie o presiune externă (contextul) care comprimă puternic o conexiune altfel valoroasă.

**Ce înseamnă asta pentru tine:** Merită o reflecție sinceră. Întreabă-te: 
este dezechilibrul în sentimente (atracție ≠ conectivitate) sau în circumstanțe? 
Un scor mic nu înseamnă că relația e greșită — poate înseamnă că momentul sau contextul nu e potrivit.
        """)

    st.markdown("---")

    # ── CONTEXT CARD ─────────────────────────────────────────────────────────
    st.markdown(f"**Context aplicat: {ctx_label}**")
    st.caption(ctx_desc)
    if penaliz > 0:
        st.caption(f"Penalizare de context: -{penaliz} puncte din scorul brut de {compatib*10:.0f}.")

    st.markdown("---")

    # ── GRAFICE ───────────────────────────────────────────────────────────────
    col_a, col_b = st.columns(2)

    labels = ['Dor/Gând', 'Magnetism', 'Prioritate', 'Bucurie', 'Inspirație',
              'Deschidere', 'Empatie', 'Sincron', 'Rezoluție', 'Siguranță']
    vals = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    with col_a:
        st.markdown("**Profil pe dimensiuni**")
        fig_radar = go.Figure(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=labels + [labels[0]],
            fill='toself',
            fillcolor='rgba(83,74,183,0.15)',
            line=dict(color='#534AB7', width=2),
            marker=dict(size=5, color='#534AB7')
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(size=10)),
                angularaxis=dict(tickfont=dict(size=11))
            ),
            showlegend=False,
            margin=dict(l=40, r=40, t=30, b=30),
            height=300
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_b:
        st.markdown("**Atracție vs conectivitate vs scor final**")
        fig_bar = go.Figure(go.Bar(
            x=['Atracție', 'Conectivitate', 'Scor final /10'],
            y=[atractie, conectiv, final / 10],
            marker_color=['#534AB7', '#1D9E75', '#BA7517'],
            marker_line_width=0,
            text=[f"{atractie:.1f}", f"{conectiv:.1f}", f"{final/10:.1f}"],
            textposition='outside',
            textfont=dict(size=13)
        ))
        fig_bar.update_layout(
            yaxis=dict(range=[0, 12], showgrid=True, gridcolor='#eee', title="Scor /10"),
            xaxis=dict(showgrid=False),
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # ── DETALIU PROGRESS BARS ─────────────────────────────────────────────────
    st.markdown("**Detaliu pe fiecare dimensiune**")
    col_d1, col_d2 = st.columns(2)

    atractie_items = [
        ("Dor și Gând", q1),
        ("Chimie și Magnetism", q2),
        ("Focalizare", q3),
        ("Bucurie", q4),
        ("Model și Sprijin", q5),
    ]
    conectiv_items = [
        ("Deschidere", q6),
        ("Empatie", q7),
        ("Sincronicitate", q8),
        ("Rezoluție", q9),
        ("Siguranță și Pace", q10),
    ]

    with col_d1:
        st.markdown("*Atracție și interes*")
        for label, val in atractie_items:
            st.progress(val / 10, text=f"{label}: **{val}/10**")

    with col_d2:
        st.markdown("*Conectivitate și deschidere*")
        for label, val in conectiv_items:
            st.progress(val / 10, text=f"{label}: **{val}/10**")

    # ── DIMENSIUNE CEA MAI SLABA ──────────────────────────────────────────────
    st.markdown("---")
    all_items = atractie_items + conectiv_items
    min_item = min(all_items, key=lambda x: x[1])
    max_item = max(all_items, key=lambda x: x[1])

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.info(f"**Cea mai puternică dimensiune:** {max_item[0]} ({max_item[1]}/10)\n\nAcesta este punctul tău de forță în această relație.")
    with col_e2:
        st.warning(f"**Zona cu cel mai mult potențial:** {min_item[0]} ({min_item[1]}/10)\n\nAcesta este locul unde există cel mai mult spațiu de crescut.")

    st.markdown("---")
    st.caption(f"Context: **{ctx_label}** · Scor atracție: {atractie:.1f} · Scor conectivitate: {conectiv:.1f} · Scor brut: {compatib*10:.0f} · Penalizare: -{penaliz} · Scor final: {final:.0f}/100")
    st.caption("⚠️ Acest instrument este un exercițiu de reflecție personală, nu un diagnostic psihologic sau științific. Scorurile reflectă exclusiv percepția ta subiectivă.")

st.markdown("---")
st.caption("© 2026 Ciprian Axiniei · Instrument de reflecție relațională")
