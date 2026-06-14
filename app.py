import streamlit as st

# Configurare pagină - strict standard
st.set_page_config(page_title="Analizor de Rezonanță TSC", page_icon="📊", layout="centered")

# ==========================================
# BARA LATERALĂ (CREDITS & METODOLOGIE)
# ==========================================
st.sidebar.title("🔬 Teoria TSC")
st.sidebar.markdown("### **Modelul Susceptibilității Critice**")
st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Autor și Dezvoltator:**")
st.sidebar.info("🧠 **Ciprian Axiniei**")
st.sidebar.markdown("""
**Despre Model:**
Acest algoritm analizează cuplajul electromagnetic și rezonanța biologică dintre două noduri informaționale dintr-o rețea. 

Prin ecuația Hamiltoniană, modelul măsoară modul în care constrângerile din realitate generează un efect de recul energetic în corpul uman (stres structural).
""")
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Toate drepturile rezervate autorului.")

# Titlul principal pe ecran
st.title("📊 Analizor Universal de Rezonanță TSC")
st.markdown("---")

# ==========================================
# FORMULAR IZOLAT (Previne bug-ul removeChild din Streamlit)
# ==========================================
with st.form(key="tsc_form"):
    st.subheader("1. Contextul Real al Legăturii")
    context = st.radio(
        "Care este starea actuală a relației în teren?",
        (
            "Aliniere Deschisă (Suntem împreună / Sentimente confirmate reciproc)",
            "Canal Blocat (Conexiune profundă, dar suntem doar amici / alte relații)",
            "Emisie Asimetrică (Simt conexiunea, dar cealaltă persoană nu o împărtășește/nu știe)"
        )
    )

    st.markdown("---")
    st.subheader("2. Secțiunea λ – Forța de Atracție și Magnetismul")
    st.caption("Măsoară intensitatea câmpului electromagnetic și cât de puternic te trage această persoană în orbita sa.")

    q1 = st.slider("1. Dorul și Gândul: Cât de des apar gânduri legate de această persoană când nu sunteți în același loc?", 1, 10, 5)
    q2 = st.slider("2. Chimia și Atingerea: Cât de puternic este magnetismul sau emoția intensă în corp la o apropiere fizică?", 1, 10, 5)
    q3 = st.slider("3. Focalizarea Informațională: Cât de prima persoană este când vrei să împarți o bucurie sau o problemă?", 1, 10, 5)
    q4 = st.slider("4. Declanșatorul de Bucurie: Cât de ușor reușește să te facă să zâmbești dintr-o privire sau un mesaj?", 1, 10, 5)
    q5 = st.slider("5. Model și Sprijin: În ce măsură este un exemplu din care înveți, te stimulează să evoluezi și e un sprijin emoțional?", 1, 10, 5)

    st.markdown("---")
    st.subheader("3. Secțiunea C – Conectivitatea Structurală")
    st.caption("Măsoară curățenia canalelor de comunicare și cât de profund sunt cuplate sistemele voastre biologice.")

    q6 = st.slider("6. Deschiderea și Destăinuirea: Cât de ușor îți este să te destăinui și să îți arăți vulnerabilitățile fără frică?", 1, 10, 5)
    q7 = st.slider("7. Empatia Biologică / Co-rezonanța: Cât de mult te influențează direct în corp starea ei de spirit sau de sănătate?", 1, 10, 5)
    q8 = st.slider("8. Telepatia și Intuiția: Cât de des experimentați momente de sincron (spuneți același lucru, vă căutați în același timp)?", 1, 10, 5)
    q9 = st.slider("9. Fluiditatea și Rezoluția: Cât de repede și curat se dizolvă neînțelegerile fără să rămână răceală/noduri energetice?", 1, 10, 5)
    q10 = st.slider("10. Siguranța în Rețea: Cât de profundă este starea de liniște, siguranță și pace pe care o simți în prezența sa?", 1, 10, 5)

    # Singurul buton din formular care declanșează acțiunea
    submit_button = st.form_submit_button(label="🔮 Calculează Rezonanța TSC", type="primary")

# ==========================================
# PROCESARE REZULTATE (Rulează doar după Submit)
# ==========================================
if submit_button:
    # Calcul mediilor
    lambda_param = (q1 + q2 + q3 + q4 + q5) / 5.0
    c_param = (q6 + q7 + q8 + q9 + q10) / 5.0
    
    # Determinare factor de context (Penalizare)
    if "Aliniere Deschisă" in context:
        fs = 0
        status_text = "Aliniere Deschisă"
    elif "Canal Blocat" in context:
        fs = 25
        status_text = "Canal Blocat (Atracție sub Constrângere)"
    else:
        fs = 50
        status_text = "Emisie Asimetrică (Scurtcircuit)"
        
    # Calcul Hamiltonian pur și final
    h_teoretic = 100 - (lambda_param * c_param)
    h_final = h_teoretic + fs
    h_final = min(max(h_final, 0.0), 100.0)
    
    # Afișare rezultate
    st.header("📊 Raport de Diagnostic Biofizic")
    st.write(f"**Status Context:** {status_text}")
    st.metric(label="Hamiltonianul Final (Scor de Stres H)", value=f"{h_final:.2f}")
    
    # Afișare stare pe baza intervalelor
    if 0 <= h_final <= 15:
        st.success(f"**Nivel de Conexiune detectat:** Rezonanță Absolută (Suflet Pereche)")
    elif 16 <= h_final <= 35:
        st.success(f"**Nivel de Conexiune detectat:** Aliniere de Fază (Potrivire Înaltă)")
    elif 36 <= h_final <= 50:
        st.warning(f"**Nivel de Conexiune detectat:** Echilibru Stabil (Atracție și Conexiune)")
