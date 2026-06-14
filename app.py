import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
from datetime import datetime, date

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
    .stSlider > label { font-size: 14px; color: #444; }
    .stButton > button { border-radius: 10px; font-weight: 500; height: 46px; transition: all .2s; }
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

if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset():
    st.session_state.step = 1
    st.session_state.mode = None

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;padding:1rem 0 1.5rem'>
  <div style='font-size:48px;margin-bottom:8px'>💜</div>
  <h1 style='font-size:22px;font-weight:600;margin:0 0 6px'>Analizor de Compatibilitate Relațională</h1>
  <p style='color:#888;font-size:14px;margin:0'>Câțiva pași simpli. Un raport detaliat despre ce simți.<br>Instrument de reflecție personală — nu un diagnostic.</p>
</div>
""", unsafe_allow_html=True)

# ── STEP MAP (depinde de mod) ───────────────────────────────────────────────
mode = st.session_state.get('mode')
if mode == "profund":
    labels_prog = ["Intro", "Context", "Atracție", "Compatibilitate", "Profunzime", "Portret cosmic", "Raport"]
else:
    labels_prog = ["Intro", "Context", "Atracție", "Compatibilitate", "Profunzime", "Raport"]

total_steps = len(labels_prog)
step = st.session_state.step

# ── PROGRESS ──────────────────────────────────────────────────────────────────
cols_prog = st.columns(total_steps)
for i, (col, label) in enumerate(zip(cols_prog, labels_prog)):
    with col:
        if i + 1 < step:
            st.markdown(f"<div style='text-align:center'><div style='width:26px;height:26px;border-radius:50%;background:#1D9E75;color:white;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:12px'>✓</div><div style='font-size:9px;color:#1D9E75;font-weight:500'>{label}</div></div>", unsafe_allow_html=True)
        elif i + 1 == step:
            st.markdown(f"<div style='text-align:center'><div style='width:26px;height:26px;border-radius:50%;background:#534AB7;color:white;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:12px;font-weight:600'>{i+1}</div><div style='font-size:9px;color:#534AB7;font-weight:600'>{label}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:center'><div style='width:26px;height:26px;border-radius:50%;background:#f0f0f0;color:#aaa;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:12px'>{i+1}</div><div style='font-size:9px;color:#aaa'>{label}</div></div>", unsafe_allow_html=True)

st.progress((step - 1) / (total_steps - 1), text="")
st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 1 — INTRO + EXPLICAȚII + ALEGERE MOD
# ════════════════════════════════════════════════════════════════════════════
if step == 1:
    st.markdown("### Cum funcționează acest test")
    st.markdown("""
Vei răspunde la o serie de întrebări despre o persoană la care te gândești.
Pentru fiecare întrebare vei alege o notă **de la 1 la 10**, unde:

- **1–2** = aproape deloc / nu se aplică
- **3–4** = puțin, ocazional
- **5–6** = moderat, undeva la mijloc
- **7–8** = destul de mult, frecvent
- **9–10** = foarte mult / aproape mereu

Nu există răspunsuri "corecte" — fii sincer cu tine. La final vei primi un raport
cu un scor general, grafice și o interpretare a rezultatelor tale.
""")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Ce tip de răspuns vrei?")
    st.caption("Alege nivelul de profunzime al analizei.")

    mode_choice = st.radio("mod", options=[
        "⚡ Orientativ — răspuns rapid, bazat doar pe întrebările despre relație",
        "🔭 Profund — pe lângă întrebări, adaugă și un portret simbolic (zodie + numerologie) pentru o perspectivă suplimentară",
    ], label_visibility="collapsed", index=0 if st.session_state.get('mode') != 'profund' else 1)

    if mode_choice.startswith("⚡"):
        st.session_state.mode = "orientativ"
    else:
        st.session_state.mode = "profund"
        st.info("📌 Secțiunea de portret cosmic (zodie + numerologie) este prezentată **separat**, ca o perspectivă simbolică și de divertisment — nu influențează scorul calculat din răspunsurile tale.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Continuă →", type="primary", use_container_width=True, on_click=next_step)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 2 — CONTEXT
# ════════════════════════════════════════════════════════════════════════════
elif step == 2:
    st.markdown("### Care este starea actuală a relației?")
    st.caption("Alege situația care descrie cel mai bine contextul vostru în acest moment.")
    st.markdown("<br>", unsafe_allow_html=True)

    context = st.radio("context", options=[
        "💚 Aliniere Deschisă — Suntem împreună / Sentimente confirmate reciproc",
        "🟡 Canal Parțial Blocat — Conexiune profundă, dar suntem amici / altă relație / distanță",
        "🔴 Asimetrie Neconfirmată — Simt conexiunea, dar cealaltă persoană nu o cunoaște sau nu o împărtășește",
    ], label_visibility="collapsed", index=["💚","🟡","🔴"].index(st.session_state.get('context','💚')[0]) if st.session_state.get('context') else 0)
    st.session_state.context = context
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2: st.button("Continuă →", type="primary", use_container_width=True, on_click=next_step)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 3 — ATRACTIE (q1-q5)
# ════════════════════════════════════════════════════════════════════════════
elif step == 3:
    st.markdown("### Atracție")
    st.caption("Cât de puternic te trage această persoană? (1 = aproape deloc · 10 = foarte mult)")
    st.markdown("<br>", unsafe_allow_html=True)

    q1 = st.slider("1. Cât de des te surprinzi gândindu-te la ea/el, chiar și fără niciun motiv anume?", 1, 10, st.session_state.get('q1', 5), help="1 = Rar / 10 = Constant")
    q2 = st.slider("2. Dacă ai afla mâine că s-a mutat în altă țară pentru totdeauna, cât de tare ți-ar influența starea?", 1, 10, st.session_state.get('q2', 5), help="1 = Puțin / 10 = Enorm")
    q3 = st.slider("3. Cât de mult te fascinează lucrurile la ea/el pe care nu le-ai găsit la altcineva?", 1, 10, st.session_state.get('q3', 5), help="1 = Deloc / 10 = Profund")
    q4 = st.slider("4. Când ești în preajma ei/lui, cât de mult simți că devii mai atent, mai prezent, mai viu?", 1, 10, st.session_state.get('q4', 5), help="1 = Nimic special / 10 = Total diferit")
    q5 = st.slider("5. Cât de des ți-ai imaginat cum ar fi să petreceți timp împreună, să fiți în aceeași lume?", 1, 10, st.session_state.get('q5', 5), help="1 = Niciodată / 10 = Foarte des")

    for k,v in [('q1',q1),('q2',q2),('q3',q3),('q4',q4),('q5',q5)]:
        st.session_state[k] = v

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2: st.button("Continuă →", type="primary", on_click=next_step, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 4 — COMPATIBILITATE (q6-q10)
# ════════════════════════════════════════════════════════════════════════════
elif step == 4:
    st.markdown("### Compatibilitate")
    st.caption("Cât de bine funcționați împreună? (1 = aproape deloc · 10 = foarte mult)")
    st.markdown("<br>", unsafe_allow_html=True)

    q6  = st.slider("6. Cât de ușor poți vorbi cu ea/el ore întregi despre orice, fără să simți că pierzi vremea?", 1, 10, st.session_state.get('q6', 5), help="1 = Greu / 10 = Natural")
    q7  = st.slider("7. Când ești trist sau copleșit, cât de mult îți vine să îi spui ei/lui mai degrabă decât să ascunzi?", 1, 10, st.session_state.get('q7', 5), help="1 = Ascund / 10 = Îi spun primul")
    q8  = st.slider("8. Cât de des vi se întâmplă să vă gândiți la același lucru în același moment sau să vă căutați simultan?", 1, 10, st.session_state.get('q8', 5), help="1 = Niciodată / 10 = Frecvent")
    q9  = st.slider("9. După o conversație cu ea/el, cât de mult pleci cu mai multă energie și stare bună decât ai avut înainte?", 1, 10, st.session_state.get('q9', 5), help="1 = Epuizat / 10 = Reîncărcat")
    q10 = st.slider("10. Cât de mult simți că există o versiune a ta pe care o arăți doar în preajma ei/lui și nicăieri altundeva?", 1, 10, st.session_state.get('q10', 5), help="1 = Sunt la fel ca oriunde / 10 = Complet diferit")

    for k,v in [('q6',q6),('q7',q7),('q8',q8),('q9',q9),('q10',q10)]:
        st.session_state[k] = v

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2: st.button("Continuă →", type="primary", on_click=next_step, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# PASUL 5 — PROFUNZIME (q11-q12)
# ════════════════════════════════════════════════════════════════════════════
elif step == 5:
    st.markdown("### Profunzime")
    st.caption("Întrebările care spun adevărul. (1 = aproape deloc · 10 = foarte mult)")
    st.markdown("<br>", unsafe_allow_html=True)

    q11 = st.slider("11. Cât de mult ai lăsa orice altceva deoparte dacă ea/el ar fi în dificultate și ar avea nevoie de tine?", 1, 10, st.session_state.get('q11', 5), help="1 = Depinde / 10 = Oricând, fără ezitare")
    q12 = st.slider("12. Cât de greu ți-ar fi să descrii această persoană în doar trei cuvinte — pentru că simți că sunt prea puține?", 1, 10, st.session_state.get('q12', 5), help="1 = Ușor / 10 = Imposibil, e prea mult")

    for k,v in [('q11',q11),('q12',q12)]:
        st.session_state[k] = v

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2:
        label = "Continuă →" if mode == "profund" else "💜 Calculează Raportul"
        if st.button(label, type="primary", use_container_width=True):
            next_step()

# ════════════════════════════════════════════════════════════════════════════
# PASUL 6 (doar mod profund) — PORTRET COSMIC: date de naștere
# ════════════════════════════════════════════════════════════════════════════
elif step == 6 and mode == "profund":
    st.markdown("### Portret cosmic")
    st.markdown("""
<div style='background:#FAEEDA;border-radius:12px;padding:1rem 1.25rem;margin-bottom:1rem;font-size:14px;color:#7a5a1e;line-height:1.6'>
🔭 Această secțiune este <b>simbolică și de divertisment</b> — folosește zodia și numerologia
pentru o perspectivă suplimentară. Nu are bază științifică și <b>nu influențează scorul</b>
calculat din răspunsurile tale.
</div>
""", unsafe_allow_html=True)
    st.caption("Completează datele pentru a vedea zodiile și numerele guvernante ale celor doi.")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("**Tu**")
    col1, col2 = st.columns(2)
    with col1:
        data_ta = st.date_input("Data nașterii (tu)", value=st.session_state.get('data_ta', date(1995,1,1)),
                                 min_value=date(1930,1,1), max_value=date.today())
    with col2:
        gen_tau = st.selectbox("Gen (tu)", ["Feminin", "Masculin"], index=0 if st.session_state.get('gen_tau','Feminin')=="Feminin" else 1)

    st.markdown("**Persoana cealaltă**")
    col3, col4 = st.columns(2)
    with col3:
        data_ei = st.date_input("Data nașterii (cealaltă persoană)", value=st.session_state.get('data_ei', date(1995,1,1)),
                                 min_value=date(1930,1,1), max_value=date.today())
    with col4:
        gen_ei = st.selectbox("Gen (cealaltă persoană)", ["Feminin", "Masculin"], index=1 if st.session_state.get('gen_ei','Masculin')=="Masculin" else 0)

    st.session_state.data_ta = data_ta
    st.session_state.gen_tau = gen_tau
    st.session_state.data_ei = data_ei
    st.session_state.gen_ei = gen_ei

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button("← Înapoi", on_click=prev_step, use_container_width=True)
    with col2:
        if st.button("💜 Calculează Raportul", type="primary", use_container_width=True):
            next_step()

# ════════════════════════════════════════════════════════════════════════════
# PASUL FINAL — REZULTATE
# ════════════════════════════════════════════════════════════════════════════
elif step == total_steps:
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
    q11 = st.session_state.get('q11', 5)
    q12 = st.session_state.get('q12', 5)
    context = st.session_state.get('context', '')

    # ── CALCULE TSC ───────────────────────────────────────────────────────
    atractie  = (q1 + q2 + q3 + q4 + q5) / 5          # lambda — forta de atractie
    conectiv  = (q6 + q7 + q8 + q9 + q10) / 5         # C — conectivitatea structurala
    profunzime = (q11 + q12) / 2                        # factor de profunzime

    E = 10 - profunzime
    H = E - (atractie * conectiv / 10)                  # Hamiltonianul relatiei

    vals_all = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
    C_norm = conectiv / 10
    beta = 1 / C_norm if C_norm > 0 else 10
    var_C = float(np.var([q/10 for q in [q6,q7,q8,q9,q10]]))
    chi = beta * var_C * 10

    scor_brut = 100 - (H * 5) - (chi * 10)

    # Penalizare context
    if "Aliniere" in context:
        penaliz, ctx_label, ctx_desc = 0, "Aliniere Deschisă", "Contextul este complet favorabil. Energia relației circulă liber în ambele sensuri."
    elif "Parțial" in context or "Blocat" in context:
        penaliz, ctx_label, ctx_desc = 10, "Canal Parțial Blocat", "Există obstacole externe care limitează exprimarea naturală a conexiunii voastre."
    else:
        penaliz, ctx_label, ctx_desc = 20, "Asimetrie Neconfirmată", "Decalajul dintre ce simți tu și ce știe/simte cealaltă persoană creează o presiune internă semnificativă."

    final = max(0, min(100, scor_brut - penaliz))

    # ── STATUS ────────────────────────────────────────────────────────────
    if final >= 75:
        emoji_s, status_title, status_color, bg_color = "🟢", "Conexiune Puternică și Echilibrată", "#534AB7", "#EEEDFE"
        insight = "Atracția și conectivitatea sunt puternice și echilibrate, iar profunzimea legăturii e reală. Sistemul vostru e stabil — există baze solide pe toate planurile. Dacă nu ați deschis deja comunicarea despre ce simțiți, acum este momentul potrivit."
        st.balloons()
    elif final >= 55:
        emoji_s, status_title, status_color, bg_color = "🔵", "Potrivire Bună cu Zone de Crescut", "#185FA5", "#E6F1FB"
        insight = "Există o fundație reală. Atracția e prezentă și conexiunea funcționează, dar există un mic dezechilibru între ce simți și cât de deschisă e comunicarea. Cultivă profunzimea — ea e ce transformă atracția în ceva durabil."
    elif final >= 40:
        emoji_s, status_title, status_color, bg_color = "🟡", "Atracție Prezentă, Echilibru Fragil", "#BA7517", "#FAEEDA"
        insight = "Simți ceva real, dar sistemul e instabil — fie atracția nu e susținută de o conectivitate profundă, fie contextul adaugă prea multă presiune. Întreabă-te: ce anume creează dezechilibrul? Vine din interior sau din circumstanțe externe?"
    else:
        emoji_s, status_title, status_color, bg_color = "🔴", "Dezechilibru Semnificativ", "#A32D2D", "#FCEBEB"
        insight = "Există o presiune internă mare — fie între ce simți și ce există în realitate, fie între atracție și conectivitate. Un scor mic nu înseamnă că relația e greșită. Poate înseamnă că momentul, contextul sau comunicarea nu sunt încă aliniate."

    # Salvează
    salveaza({
        "Data/Ora": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Mod": mode,
        "Context": ctx_label,
        "Atractie_lambda": round(atractie, 2),
        "Conectivitate_C": round(conectiv, 2),
        "Profunzime": round(profunzime, 2),
        "Hamiltonian_H": round(H, 2),
        "Susceptibilitate_chi": round(chi, 2),
        "Scor_Brut": round(scor_brut, 2),
        "Penalizare": penaliz,
        "Scor_Final": round(final, 2),
        "Q1":q1,"Q2":q2,"Q3":q3,"Q4":q4,"Q5":q5,
        "Q6":q6,"Q7":q7,"Q8":q8,"Q9":q9,"Q10":q10,
        "Q11":q11,"Q12":q12
    })

    # ── SCOR HERO ─────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style='background:{bg_color};border-radius:16px;padding:2rem;text-align:center;margin-bottom:1.5rem'>
      <div style='font-size:72px;font-weight:700;color:{status_color};line-height:1'>{int(final)}</div>
      <div style='font-size:13px;color:#999;margin-bottom:8px'>din 100</div>
      <div style='font-size:18px;font-weight:600;color:{status_color}'>{emoji_s} {status_title}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── METRICI TSC ───────────────────────────────────────────────────────
    st.markdown("**Indicatori**")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Atracție (λ)", f"{atractie:.1f}/10", help="Forța de atracție — cât de puternic te trage spre ea/el")
    col2.metric("Conectivitate (C)", f"{conectiv:.1f}/10", help="Cât de profundă și fluidă e legătura dintre voi")
    col3.metric("Profunzime", f"{profunzime:.1f}/10", help="Cât de profund e angajamentul și unicitatea legăturii")
    col4.metric("Echilibru (χ)", f"{chi:.2f}", delta="stabil" if chi < 0.05 else "instabil", delta_color="normal" if chi < 0.05 else "inverse", help="Susceptibilitate — cât de echilibrat e sistemul intern. Mai mic = mai stabil.")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── GRAFIC RADAR ──────────────────────────────────────────────────────
    labels_radar = [
        'Gând constant', 'Impact absență', 'Fascinație', 'Prezență vie', 'Imaginație comună',
        'Comunicare', 'Deschidere', 'Sincronicitate', 'Energie după', 'Versiunea ta',
        'Disponibilitate', 'Complexitate'
    ]
    vals_radar = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=vals_radar + [vals_radar[0]],
        theta=labels_radar + [labels_radar[0]],
        fill='toself', fillcolor='rgba(83,74,183,0.12)',
        line=dict(color='#534AB7', width=2),
        marker=dict(size=6, color='#534AB7'), name='Profilul tău'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=[7]*12+[7], theta=labels_radar+[labels_radar[0]],
        line=dict(color='#ddd', width=1, dash='dot'), showlegend=False
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0,10], tickfont=dict(size=9), gridcolor='#eee'),
            angularaxis=dict(tickfont=dict(size=11), gridcolor='#eee')
        ),
        showlegend=False,
        margin=dict(l=60, r=60, t=50, b=40),
        height=420,
        paper_bgcolor='rgba(0,0,0,0)',
        title=dict(text='Profil complet pe toate dimensiunile', font=dict(size=14, color='#555'), x=0.5)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # ── BAR CHART ─────────────────────────────────────────────────────────
    colors_bar = ['#534AB7']*5 + ['#1D9E75']*5 + ['#BA7517']*2
    fig_bar = go.Figure(go.Bar(
        x=labels_radar, y=vals_radar,
        marker_color=colors_bar, marker_line_width=0,
        text=vals_radar, textposition='outside', textfont=dict(size=11)
    ))
    fig_bar.update_layout(
        yaxis=dict(range=[0,12], showgrid=True, gridcolor='#f0f0f0', title='Scor /10'),
        xaxis=dict(showgrid=False, tickfont=dict(size=10), tickangle=-30),
        margin=dict(l=20, r=20, t=50, b=80),
        height=360,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title=dict(text='Mov = Atracție  |  Verde = Compatibilitate  |  Portocaliu = Profunzime', font=dict(size=13, color='#555'), x=0.5)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ── CEL MAI BUN / CEL MAI SLAB ────────────────────────────────────────
    all_items = list(zip(labels_radar, vals_radar))
    max_item = max(all_items, key=lambda x: x[1])
    min_item = min(all_items, key=lambda x: x[1])
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.success(f"**⭐ Cea mai puternică dimensiune**\n\n{max_item[0]}: **{max_item[1]}/10**")
    with col_e2:
        st.warning(f"**📈 Zona cu cel mai mult potențial**\n\n{min_item[0]}: **{min_item[1]}/10**")

    st.markdown("---")

    # ── INSIGHT ───────────────────────────────────────────────────────────
    st.markdown("### Ce înseamnă pentru tine")
    st.markdown(f"""
    <div style='background:{bg_color};border-left:3px solid {status_color};border-radius:0 12px 12px 0;padding:1.25rem 1.5rem;margin-bottom:1rem;line-height:1.7;color:#333'>
      {insight}
    </div>
    """, unsafe_allow_html=True)

    # ── CONTEXT ───────────────────────────────────────────────────────────
    st.markdown(f"**Context aplicat:** {ctx_label}")
    st.caption(ctx_desc)
    if penaliz > 0:
        st.caption(f"Penalizare de context: -{penaliz} puncte din scorul brut de {scor_brut:.0f}.")

    # ════════════════════════════════════════════════════════════════════
    # PORTRET COSMIC (doar mod profund) — secțiune SEPARATĂ, simbolică
    # ════════════════════════════════════════════════════════════════════
    if mode == "profund":
        st.markdown("---")
        st.markdown("## 🔭 Portret cosmic")
        st.markdown("""
<div style='background:#FAEEDA;border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.25rem;font-size:14px;color:#7a5a1e;line-height:1.6'>
Această secțiune este <b>complet separată</b> de scorul calculat mai sus. Zodia și
numerologia sunt prezentate ca <b>perspectivă simbolică și de divertisment</b>,
nu ca o evaluare științifică a relației voastre.
</div>
""", unsafe_allow_html=True)

        def zodie(d: date):
            zodii = [
                (date(1900,1,20), "Capricorn"), (date(1900,2,19), "Vărsător"), (date(1900,3,20), "Pisci"),
                (date(1900,4,20), "Berbec"), (date(1900,5,21), "Taur"), (date(1900,6,21), "Gemeni"),
                (date(1900,7,22), "Rac"), (date(1900,8,22), "Leu"), (date(1900,9,22), "Fecioară"),
                (date(1900,10,23), "Balanță"), (date(1900,11,22), "Scorpion"), (date(1900,12,22), "Săgetător"),
                (date(1900,12,31), "Capricorn"),
            ]
            md = (d.month, d.day)
            for cutoff, name in zodii:
                if md <= (cutoff.month, cutoff.day):
                    return name
            return "Capricorn"

        def numar_guvernant(d: date):
            digits = [int(c) for c in d.strftime("%Y%m%d")]
            total = sum(digits)
            while total > 9 and total not in (11, 22, 33):
                total = sum(int(c) for c in str(total))
            return total

        zodie_ta = zodie(st.session_state.data_ta)
        zodie_ei = zodie(st.session_state.data_ei)
        nr_tau = numar_guvernant(st.session_state.data_ta)
        nr_ei = numar_guvernant(st.session_state.data_ei)

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown(f"""
            <div style='background:#f5f3ff;border-radius:12px;padding:1rem;text-align:center;border:0.5px solid #ded8f5'>
              <div style='font-size:12px;color:#888'>Tu ({st.session_state.gen_tau.lower()})</div>
              <div style='font-size:20px;font-weight:600;color:#534AB7;margin:4px 0'>{zodie_ta}</div>
              <div style='font-size:12px;color:#888'>Numărul guvernant: <b>{nr_tau}</b></div>
            </div>
            """, unsafe_allow_html=True)
        with col_c2:
            st.markdown(f"""
            <div style='background:#f5f3ff;border-radius:12px;padding:1rem;text-align:center;border:0.5px solid #ded8f5'>
              <div style='font-size:12px;color:#888'>Cealaltă persoană ({st.session_state.gen_ei.lower()})</div>
              <div style='font-size:20px;font-weight:600;color:#534AB7;margin:4px 0'>{zodie_ei}</div>
              <div style='font-size:12px;color:#888'>Numărul guvernant: <b>{nr_ei}</b></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Compatibilitate zodiacală simplificată (elementele)
        elemente = {
            "Berbec":"Foc","Leu":"Foc","Săgetător":"Foc",
            "Taur":"Pământ","Fecioară":"Pământ","Capricorn":"Pământ",
            "Gemeni":"Aer","Balanță":"Aer","Vărsător":"Aer",
            "Rac":"Apă","Scorpion":"Apă","Pisci":"Apă"
        }
        el_ta, el_ei = elemente[zodie_ta], elemente[zodie_ei]
        compat_elemente = {
            ("Foc","Foc"):"Energie intensă, dinamism mare, dar și posibile fricțiuni de ego.",
            ("Foc","Aer"):"Combinație clasică — aerul alimentează focul, comunicare vie.",
            ("Foc","Pământ"):"Tensiune creativă — focul aduce mișcare, pământul aduce stabilitate.",
            ("Foc","Apă"):"Contrast puternic — pasiune versus profunzime emoțională, poate fi greu sau complementar.",
            ("Aer","Aer"):"Conexiune mentală puternică, multă comunicare, posibil lipsă de ancorare.",
            ("Aer","Pământ"):"Aerul aduce idei, pământul aduce concret — pot construi împreună cu răbdare.",
            ("Aer","Apă"):"Mental versus emoțional — necesită traducere între cele două lumi.",
            ("Pământ","Pământ"):"Stabilitate solidă, valori comune, ritm asemănător.",
            ("Pământ","Apă"):"Combinație nutritivă — pământul oferă structură, apa oferă profunzime.",
            ("Apă","Apă"):"Conexiune emoțională foarte intensă, empatie mare, posibil prea multă intensitate.",
        }
        key = (el_ta, el_ei) if (el_ta, el_ei) in compat_elemente else (el_ei, el_ta)
        desc_elemente = compat_elemente.get(key, "")

        st.markdown(f"**Elementele zodiacale:** {zodie_ta} ({el_ta}) și {zodie_ei} ({el_ei})")
        st.caption(desc_elemente)

        # Numerologie - relatia dintre numere
        st.markdown(f"**Numerele guvernante:** {nr_tau} și {nr_ei}")
        diff = abs(nr_tau - nr_ei)
        if nr_tau == nr_ei:
            st.caption("Numere identice — rezonanță puternică, înțelegere intuitivă, dar atenție să nu vă oglindiți doar punctele slabe.")
        elif diff in (1, 2):
            st.caption("Numere apropiate — ritmuri compatibile, ajustări ușoare necesare.")
        else:
            st.caption("Numere distante — perspective diferite asupra vieții, care pot fi complementare sau pot necesita mai multă comunicare.")

        st.caption("🔭 Reamintire: această secțiune este simbolică, nu schimbă scorul de mai sus.")

    st.markdown("---")
    st.button("🔄 Completează din nou", on_click=reset, use_container_width=True)

    # ── ISTORIC ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋 Vezi toate rezultatele salvate"):
        df = incarca()
        if df.empty:
            st.info("Nu există rezultate salvate încă.")
        else:
            cols_show = [c for c in ["Data/Ora","Mod","Context","Atractie_lambda","Conectivitate_C","Profunzime","Hamiltonian_H","Susceptibilitate_chi","Scor_Final"] if c in df.columns]
            st.dataframe(df[cols_show], use_container_width=True)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Descarcă toate rezultatele (CSV)", csv, "rezultate.csv", "text/csv", use_container_width=True)
            st.caption(f"Total rezultate salvate: **{len(df)}**")

    st.markdown("---")
    st.caption("⚠️ Instrument de reflecție personală, nu un diagnostic psihologic sau științific.")

st.markdown("---")
st.caption("© 2026 Ciprian Axiniei · Instrument de reflecție relațională")
