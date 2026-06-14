import streamlit as st

# Configurare pagină - standard și stabilă
st.set_page_config(page_title="Analizor de Rezonanță TSC", page_icon="📊", layout="centered")

# ==========================================
# BARA LATERALĂ (CREDITS & METODOLOGIE - FORMAT CURAT)
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

# Folosim un container izolat pentru formular ca să protejăm randarea în browser
with st.container():
    st.subheader("1. Contextul Real al Legăturii")
    context = st.radio(
        "Care este starea actuală a relației în teren?",
        (
            "Aliniere Deschisă (Suntem împreună / Sentimente confirmate reciproc)",
            "Canal Blocat (Conexiune profundă, dar suntem doar amici / alte relații)",
            "Emisie Asimetrică (Simt conexiunea, dar cealaltă persoană nu o împărtășește/nu știe)"
        ),
        key="context_input"
    )

    st.markdown("---")
    st.subheader("2. Secțiunea λ – Forța de Atracție și Magnetismul")
    st.caption("Măsoară intensitatea câmpului electromagnetic și cât de puternic te trage această persoană în orbita sa.")

    q1 = st.slider("1. Dorul și Gândul: Cât de des apar gânduri legate de această persoană când nu sunteți în același loc?", 1, 10, 5, key="q1")
    q2 = st.slider("2. Chimia și Atingerea: Cât de puternic este magnetismul sau emoția intensă în corp la o apropiere fizică?", 1, 10, 5, key="q2")
    q3 = st.slider("3. Focalizarea Informațională: Cât de prima persoană este când vrei să împarți o bucurie sau o problemă?", 1, 10, 5, key="q3")
    q4 = st.slider("4. Declanșatorul de Bucurie: Cât de ușor reușește să te facă să zâmbești dintr-o privire sau un mesaj?", 1, 10, 5, key="q4")
    q5 = st.slider("5. Model și Sprijin: În ce măsură este un exemplu din care înveți, te stimulează să evoluezi și e un sprijin emoțional?", 1, 10, 5, key="q5")

    st.markdown("---")
    st.subheader("3. Secțiunea C – Conectivitatea Structurală")
    st.caption("Măsoară curățenia canalelor de comunicare și cât de profund sunt cuplate sistemele voastre biologice.")

    q6 = st.slider("6. Deschiderea și Destăinuirea: Cât de ușor îți este să te destăinui și să îți arăți vulnerabilitățile fără frică?", 1, 10, 5, key="q6")
    q7 = st.slider("7. Empatia Biologică / Co-rezonanța: Cât de mult te influențează direct în corp starea ei de spirit sau de sănătate?", 1, 10, 5, key="q7")
    q8 = st.slider("8. Telepatia și Intuiția: Cât de des experimentați momente de sincron (spuneți același lucru, vă căutați în același timp)?", 1, 10, 5, key="q8")
    q9 = st.slider("9. Fluiditatea și Rezoluția: Cât de repede și curat se dizolvă neînțelegerile fără să rămână răceală/noduri energetice?", 1, 10, 5, key="q9")
    q10 = st.slider("10. Siguranța în Rețea: Cât de profundă este starea de liniște, siguranță și pace pe care o simți în prezența sa?", 1, 10, 5, key="q10")

st.markdown("---")

# Zonă complet separată pentru buton și generarea raportului
calculat = st.button("🔮 Calculează Rezonanța TSC", type="primary", key="btn_calcul")

if calculat:
    # Rezultatele sunt plasate într-un container separat dedicat, prevenind suprapunerea elementelor DOM
    with st.container():
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
        
        # Afișare rezultate pe ecran
        st.header("📊 Raport de Diagnostic Biofizic")
        st.write(f"**Status Context:** {status_text}")
        st.metric(label="Hamiltonianul Final (Scor de Stres H)", value=f"{h_final:.2f}")
        
        # Starea sistemului
        if 0 <= h_final <= 15:
            st.success(f"**Nivel de Conexiune detectat:** Rezonanță Absolută (Suflet Pereche)")
        elif 16 <= h_final <= 35:
            st.success(f"**Nivel de Conexiune detectat:** Aliniere de Fază (Potrivire Înaltă)")
        elif 36 <= h_final <= 50:
            st.warning(f"**Nivel de Conexiune detectat:** Echilibru Stabil (Atracție și Conexiune)")
        elif 51 <= h_final <= 70:
            st.warning(f"**Nivel de Conexiune detectat:** Încetinire Critică (Zonă de Fluctuație)")
        elif 71 <= h_final <= 85:
            st.error(f"**Nivel de Conexiune detectat:** Disonanță de Aliniere (Conveniență)")
        else:
            st.error(f"**Nivel de Conexiune detectat:** Haos Total (Colapsul Rețelei)")
        
        st.markdown("---")
        st.subheader("🔀 Dinamica Sistemului: Potențial vs. Realitate")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🟢 Potențialul Teoretic (Nucleul Curat)")
            st.write(f"* Scor de compatibilitate nativă: **{h_teoretic:.2f}**")
            st.write(f"* Forța de Atracție (λ): **{lambda_param:.2f} / 10**")
            st.write(f"* Conectivitatea Structurală (C): **{c_param:.2f} / 10**")
            st.info("Aceasta este valoarea curată a compatibilității voastre, calculată strict pe baza simțirii și a deschiderii tale interioare, înainte ca regulile lumii fizice să intervină.")

        with col2:
            st.markdown("### 🔴 Realitatea din Teren (Bariera de Fază)")
            st.write(f"* Scor Real de Stres (H): **{h_final:.2f}**")
            st.write(f"* Penalizare Context: **+{fs}.00 puncte**")
            if fs == 0:
                st.success("Sistemul este complet liber! Energia circulă tur-retur în ambele sensuri, fără obstacole. Nu există recul.")
            elif fs == 25:
                st.warning("Efect de Recul: Pentru că rețeaua este blocată în modul 'Amiciție', energia uriașă generată de notele tale de 9 și 10 se lovește de zidul contextului și este proiectată înapoi în biologia ta, generând o presiune statică.")
            else:
                st.error("Scurtcircuit Critic: Energia ta rulează în gol. Săgeata electromagnetică se lovește de un vid de răspuns, întorcându-se complet în sistemul tău nervos sub formă de epuizare.")

        st.markdown("---")
        st.subheader("🧠 Mesajul Sistemului (Interpretare TSC)")
        
        if fs == 25:
            st.write(f"**Atenție!** Nota ta maximă de la întrebările cheie acționează ca un generator de înaltă frecvență. În scenariul actual, corpul tău reabsoarbe zilnic o presiune de **+{fs}.00** puncte. Nu există conflicte deschise (Fluiditatea e mare), dar consumi combustibil interior pentru a inhiba manifestarea naturală a legăturii. Sistemul 'fierbe' mocnit sub masca de amiciție.")
        elif fs == 50:
            st.write("Apare un decalaj critic. Notele tale mari arată o disponibilitate uriașă, dar lipsa de fază din teren întoarce energia sub formă de undă de șoc de **+50.00** puncte. Rețeaua ta tremură violent (Încetinire Critică). Risc de epuizare biologică.")
        else:
            st.write("Aliniere perfectă. Energia ta se transformă în vitalitate și pace. Sistemul tău biologic nu consumă energie pentru a se apăra, ci se încarcă direct din relație. Menține frecvența!")

# Subsol fixat în mod securizat prin format text nativ
st.markdown("---")
st.markdown("✨ Aplicație bazată pe modelul matematic TSC dezvoltat de **Ciprian Axiniei**.")
