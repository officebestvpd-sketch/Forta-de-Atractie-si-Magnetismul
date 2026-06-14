if submit_button:
    # Calcul mediilor
    lambda_param = (q1 + q2 + q3 + q4 + q5) / 5.0
    c_param = (q6 + q7 + q8 + q9 + q10) / 5.0
    
    # Determinare penalizare
    fs = 0 if "Aliniere Deschisă" in context else (25 if "Canal Blocat" in context else 50)
    
    # Calcul Hamiltonian
    h_teoretic = 100 - (lambda_param * c_param)
    h_final = min(max(h_teoretic + fs, 0.0), 100.0)
    
    # Afișare rezultate
    st.header("📊 Raport de Diagnostic Biofizic")
    st.metric(label="Hamiltonianul Final (Scor de Stres H)", value=f"{h_final:.2f}")
    
    # ==========================================
    # NOU: GRAFICUL DE REZULTATE
    # ==========================================
    import pandas as pd
    
    data = {
        "Indicator": ["Forța Atracție (λ)", "Conectivitate (C)", "Stres Structural (H)"],
        "Valoare": [lambda_param * 10, c_param * 10, h_final]
    }
    df = pd.DataFrame(data).set_index("Indicator")
    
    st.subheader("📈 Vizualizarea Sistemului")
    st.bar_chart(df)
    
    if h_final < 40:
        st.success("Analiza grafică indică o rețea stabilă (Stres scăzut).")
    elif h_final < 70:
        st.warning("Analiza grafică indică fluctuații. Există presiune în sistem.")
    else:
        st.error("Analiza grafică indică un stres critic. Rețeaua este suprasolicitată!")

    st.markdown("---")
    # ... restul codului tău (Dinamica Sistemului / Mesajul Sistemului) ...
