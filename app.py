import streamlit as st
import pandas as pd

# Configurare pagină
st.set_page_config(page_title="Analizor de Rezonanță TSC", page_icon="📊", layout="centered")

# Sidebar
st.sidebar.title("🔬 Teoria TSC")
st.sidebar.info("🧠 Ciprian Axiniei")
st.sidebar.caption("© 2026 Toate drepturile rezervate.")

st.title("📊 Analizor Universal de Rezonanță TSC")

# Formularul care conține toate input-urile
with st.form(key="tsc_form"):
    context = st.radio("Starea relației:", (
        "Aliniere Deschisă",
        "Canal Blocat",
        "Emisie Asimetrică"
    ))
    
    q1 = st.slider("Dor și Gând (λ1)", 1, 10, 5)
    q2 = st.slider("Chimia și Atingerea (λ2)", 1, 10, 5)
    q3 = st.slider("Focalizarea Informațională (λ3)", 1, 10, 5)
    q4 = st.slider("Declanșatorul de Bucurie (λ4)", 1, 10, 5)
    q5 = st.slider("Model și Sprijin (λ5)", 1, 10, 5)
    
    q6 = st.slider("Deschiderea și Destăinuirea (C1)", 1, 10, 5)
    q7 = st.slider("Empatia Biologică (C2)", 1, 10, 5)
    q8 = st.slider("Telepatia și Intuiția (C3)", 1, 10, 5)
    q9 = st.slider("Fluiditatea și Rezoluția (C4)", 1, 10, 5)
    q10 = st.slider("Siguranța în Rețea (C5)", 1, 10, 5)
    
    submit_button = st.form_submit_button(label="🔮 Calculează Rezonanța TSC")

# Procesarea se întâmplă doar după ce butonul este apăsat
if submit_button:
    lambda_param = (q1 + q2 + q3 + q4 + q5) / 5.0
    c_param = (q6 + q7 + q8 + q9 + q10) / 5.0
    
    fs = 0 if context == "Aliniere Deschisă" else (25 if context == "Canal Blocat" else 50)
    h_teoretic = 100 - (lambda_param * c_param)
    h_final = min(max(h_teoretic + fs, 0.0), 100.0)
    
    st.header("📊 Raport de Diagnostic")
    st.metric("Hamiltonianul Final (Stres H)", f"{h_final:.2f}")
    
    # Grafic
    df = pd.DataFrame({
        "Indicator": ["Atracție (λ*10)", "Conectivitate (C*10)", "Stres (H)"],
        "Scor": [lambda_param * 10, c_param * 10, h_final]
    }).set_index("Indicator")
    
    st.bar_chart(df)
    
    # Interpretare
    if h_final < 40:
        st.success("Sistem stabil și armonios.")
    elif h_final < 70:
        st.warning("Fluctuații energetice detectate.")
    else:
        st.error("Stres structural critic! Rețeaua este suprasolicitată.")
