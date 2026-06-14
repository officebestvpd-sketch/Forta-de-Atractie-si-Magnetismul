import streamlit as st

# Configurare pagină
st.set_page_config(page_title="Analizor de Rezonanță TSC", page_icon="📊", layout="centered")

# ==========================================
# NOUTATE: BARA LATERALĂ (CREDITS & METODOLOGIE CIPRIAN AXINIEI)
# ==========================================
with st.sidebar:
    st.header("🔬 Informații Model")
    st.markdown("### **Teoria Susceptibilității Critice (TSC)**")
    st.markdown("---")
    st.markdown("💡 **Autor și Dezvoltator:**")
    st.info("🧠 **Ciprian Axiniei**")
    st.markdown("""
    **Despre Model:**
    Acest algoritm analizează cuplajul electromagnetic și rezonanța biologică dintre două noduri informaționale dintr-o rețea. 
    
    Prin ecuația Hamiltoniană, modelul măsoară modul în care constrângerile din realitate generează un efect de recul energetic în corpul uman (stres structural).
    """)
    st.markdown("---")
    st.caption("© 2026 Toate drepturile rezervate autorului.")

# Titlul principal pe ecran
st.title("📊 Analizor Universal de Rezonanță TSC")
st.markdown("---")

# ==========================================
# PASUL 1: INTRODUCERE DATE (ÎNTREBĂRILE APAR PRIMA DATĂ)
# ==========================================

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

st.markdown("---")

# ==========================================
# PASUL 2: CALCULUL ȘI AFIȘAREA REZULTATULUI
# ==========================================

if st.button("🔮 Calculează Rezonanța TSC", type="primary"):
    
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
    
    # Limităm H între 0 și 100 pentru siguranță grafică
    h_final = min(max(h_final, 0.0), 100.0)
    
    # Stabilire stare
    if 0 <= h_final <= 15:
        stare = "Rezonanță Absolută (Suflet Pereche)"
        alert_box = st.success
    elif 16 <= h_final <= 35:
        stare = "Aliniere de Fază (Potrivire Înaltă)"
        alert_box = st.success
    elif 36 <= h_final <= 50:
        stare = "Echilibru Stabil (Atracție și Conexiune)"
        alert_box = st.warning
    elif 51 <= h_final <= 70:
        stare = "Încetinire Critică (Zonă de Fluctuație)"
        alert_box = st.warning
    elif 71 <= h_final <= 85:
        stare = "Disonanță de Aliniere (Conveniență)"
        alert_box = st.error
    else:
        stare = "Haos Total (Colapsul Rețelei)"
        alert_box = st.error

    # Afișare rezultate pe ecran
    st.header("📊 Raport de Diagnostic Biofizic")
    st.write(f"**Status Context:** {status_text}")
    st.metric(label="Hamiltonianul Final (Scor de Stres H)", value=f"{h_final:.2f}")
    
    alert_box(f"**Nivel de Conexiune detectat:** {stare}")
    
    st.markdown("---")
    st.subheader("🔀 Dinamica Sistemului: Potențial vs. Realitate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🟢 Potențialul Teoretic (Nucleul Curat)")
        st.write(f"* **Scor de compatibilitate nativă:** `{h_teoretic:.2f}`")
        st.write(f"* **Forța de Atracție (λ):** `{lambda_param:.2f} / 10`")
        st.write(f"* **Conectivitatea Structurală (C):** `{c_param:.2f} / 10`")
        st.write("###")
        st.info("Aceasta este valoarea curată a compatibilității voastre, calculată strict pe baza simțirii și a deschiderii tale interioare, înainte ca regulile lumii fizice să intervină.")

    with col2:
        st.markdown("### 🔴 Realitatea din Teren (Bariera de Fază)")
        st.write(f"* **Scor Real de Stres (H):** `{h_final:.2f}`")
        st.write(f"* **Penalizare Context:** `+{fs}.00 puncte`")
        st.write("###")
        if fs == 0:
            st.success("Sistemul este complet liber! Energia circulă tur-retur în ambele sensuri, fără obstacole. Nu există recul.")
        elif fs == 25:
            st.warning("Efect de Recul: Pentru că rețeaua este blocată în modul 'Amiciție', energia uriașă generată de notele tale de 9 și 10 se lovește de zidul contextului și este proiectată înapoi în biologia ta, generând o presiune statică.")
        else:
            st.error("Scurtcircuit Critic: Energia ta rulează în gol. Săgeata electromagnetică se lovește de un vid de răspuns, întorcându-se complet în sistemul tău nervos sub formă de epuizare.")

    st.markdown("---")
    st.subheader("🧠 Mesajul Sistemului (Interpretare TSC)")
    
    if fs == 25:
        st.markdown(f"**Atenție!** Nota ta maximă de la întrebările cheie acționează ca un generator de înaltă frecvență. În scenariul actual, corpul tău reabsoarbe zilnic o presiune de `+{fs}.00` puncte. Nu există conflicte deschise (Fluiditatea e mare), dar consumi combustibil interior pentru a inhiba manifestarea naturală a legăturii. Sistemul 'fierbe' mocnit sub masca de amiciție.")
    elif fs == 50:
        st.markdown("Apare un decalaj critic. Notele tale mari arată o disponibilitate uriașă, dar lipsa de fază din teren întoarce energia sub formă de undă de șoc de `+50.00` puncte. Rețeaua ta tremură violent (Încetinire Critică). Risc de epuizare biologică.")
    else:
        st.markdown("Aliniere perfectă. Energia ta se transformă în vitalitate și pace. Sistemul tău biologic nu consumă energie pentru a se apăra, ci se încarcă direct din relație. Menține frecvența!")

# Subsol permanent (Footer)
st.markdown("---")
st.centered = st.caption("✨ Aplicație bazată pe modelul matematic TSC dezvoltat de **Ciprian Axiniei**.")
