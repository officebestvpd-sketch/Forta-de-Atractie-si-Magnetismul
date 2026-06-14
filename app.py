import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Analizor de Compatibilitate", page_icon="💜", layout="centered")

st.markdown("""
<style>
    .block-container { max-width: 720px; padding-top: 2rem; }
    .stSlider > label { font-size: 14px; color: #666; }
    .metric-row { display: flex; gap: 12px; margin-bottom: 1.5rem; }
    div[data-testid="metric-container"] { background: #f7f7f5; border-radius: 10px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)

st.title("Analizor de Compatibilitate Relațională")
st.caption("Un instrument de reflecție personală — scorurile reflectă percepția ta subiectivă în acest moment.")
st.markdown("---")

st.subheader("1. Starea actuală a relației")
context = st.radio(
    "Alege situația care descrie cel mai bine contextul vostru:",
    (
        "Aliniere deschisă — suntem împreună sau sentimentele sunt confirmate reciproc",
        "Canal parțial blocat — conexiune profundă, dar există obstacole (distanță, circumstanțe, altă relație)",
        "Asimetrie neconfirmată — simt conexiunea, dar cealaltă persoană nu o cunoaște sau nu o împărtășește"
    ),
    label_visibility="collapsed"
)

st.markdown("---")
st.subheader("2. Atracție și interes")
st.caption("Cât de intens ești atras și cât de prezentă este această persoană în gândurile tale?")

q1 = st.slider("Gând și dor — cât de des îți apare în minte?", 1, 10, 5)
q2 = st.slider("Magnetism — intensitatea emoției la apropiere fizică", 1, 10, 5)
q3 = st.slider("Prioritate — prima persoană la care apelezi?", 1, 10, 5)
q4 = st.slider("Bucurie — cât de ușor te face să zâmbești?", 1, 10, 5)
q5 = st.slider("Inspirație — te stimulează să evoluezi?", 1, 10, 5)

st.markdown("---")
st.subheader("3. Conectivitate și deschidere")
st.caption("Cât de profundă și fluidă este comunicarea și încrederea dintre voi?")

q6 = st.slider("Deschidere — te poți destăinui fără frică?", 1, 10, 5)
q7 = st.slider("Empatie — simți starea lui/ei în propriul corp?", 1, 10, 5)
q8 = st.slider("Sincronicitate — momente de gând comun, contact simultan", 1, 10, 5)
q9 = st.slider("Rezoluție — cât de repede se dizolvă conflictele?", 1, 10, 5)
q10 = st.slider("Siguranță — liniște și pace în prezența sa?", 1, 10, 5)

st.markdown("---")

if st.button("Calculează raportul", type="primary", use_container_width=True):

    atractie = (q1 + q2 + q3 + q4 + q5) / 5
    conectiv = (q6 + q7 + q8 + q9 + q10) / 5
    compatib = (atractie + conectiv) / 2

    if "Aliniere" in context:
        penaliz = 0
        ctx_label = "Aliniere deschisă"
    elif "parțial" in context:
        penaliz = 15
        ctx_label = "Canal parțial blocat"
    else:
        penaliz = 30
        ctx_label = "Asimetrie neconfirmată"

    final = max(0, min(100, compatib * 10 - penaliz))

    st.markdown("### Raport de compatibilitate")

    col1, col2, col3 = st.columns(3)
    col1.metric("Scor atracție", f"{atractie:.1f} / 10")
    col2.metric("Scor conectivitate", f"{conectiv:.1f} / 10")
    col3.metric("Scor final", f"{final:.0f} / 100")

    st.markdown("---")

    if final >= 75:
        st.success("**Conexiune puternică și echilibrată**\n\nAtracția și conectivitatea sunt amândouă ridicate, iar contextul e favorabil. Relația are baze solide pe ambele planuri.")
    elif final >= 55:
        st.info("**Potrivire bună cu zone de crescut**\n\nExistă o fundație reală, dar unele dimensiuni pot fi aprofundate. Comunicarea deschisă poate consolida relația.")
    elif final >= 35:
        st.warning("**Atracție prezentă, conectivitate în construcție**\n\nScorul arată interes real, dar și câteva zone unde legătura nu e încă profundă sau contextul adaugă fricțiune.")
    else:
        st.error("**Dezechilibru semnificativ**\n\nFie atracția și conectivitatea nu sunt sincronizate, fie contextul actual creează o presiune considerabilă. Merită reflecție.")

    st.markdown("---")

    labels = ['Dor/Gând', 'Magnetism', 'Prioritate', 'Bucurie', 'Inspirație',
              'Deschidere', 'Empatie', 'Sincron', 'Rezoluție', 'Siguranță']
    vals = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    col_a, col_b = st.columns(2)

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
        st.markdown("**Atracție vs conectivitate**")
        fig_bar = go.Figure(go.Bar(
            x=['Atracție', 'Conectivitate', 'Scor final /10'],
            y=[atractie, conectiv, final / 10],
            marker_color=['#534AB7', '#1D9E75', '#BA7517'],
            marker_line_width=0,
            text=[f"{atractie:.1f}", f"{conectiv:.1f}", f"{final/10:.1f}"],
            textposition='outside'
        ))
        fig_bar.update_layout(
            yaxis=dict(range=[0, 11], showgrid=True, gridcolor='#eee'),
            xaxis=dict(showgrid=False),
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    st.markdown("**Detaliu scoruri**")
    detail_col1, detail_col2 = st.columns(2)
    with detail_col1:
        st.markdown("**Atracție și interes**")
        for label, val in zip(['Gând și dor', 'Magnetism', 'Prioritate', 'Bucurie', 'Inspirație'], [q1,q2,q3,q4,q5]):
            st.progress(val/10, text=f"{label}: {val}/10")
    with detail_col2:
        st.markdown("**Conectivitate și deschidere**")
        for label, val in zip(['Deschidere', 'Empatie', 'Sincronicitate', 'Rezoluție', 'Siguranță'], [q6,q7,q8,q9,q10]):
            st.progress(val/10, text=f"{label}: {val}/10")

    st.markdown("---")
    st.caption(f"Context: **{ctx_label}** · Penalizare aplicată: -{penaliz} puncte · Scor brut: {compatib*10:.1f} → Scor final: {final:.0f}/100")
    st.caption("⚠️ Acest instrument este un exercițiu de reflecție personală, nu un diagnostic psihologic sau științific.")

st.markdown("---")
st.caption("© 2026 Ciprian Axiniei · Aplicație de reflecție relațională")
