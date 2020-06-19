import streamlit as st
import run




def main():
    # Initial Values
    susceptible = 990
    exposed = 7
    infected = 1
    dead = 1
    recovered = 1

    # Sys parameters
    r0 = 2.5
    recovering_rate = 0.25
    exposure_rate = 0.3
    death_rate = 0.01
    death_proportion_rate = 0.11

    st.markdown("# SEIR Model")
    st.sidebar.markdown("Variáveis iniciais:")
    susceptible = st.sidebar.number_input("Suscetívceis", value=susceptible)
    exposed = st.sidebar.number_input("Expostos", value=exposed)
    infected = st.sidebar.number_input("Infectados", value=infected)
    dead = st.sidebar.number_input("Mortos", value=dead)
    recovered = st.sidebar.number_input("Recuperados", value=recovered)
    st.sidebar.markdown("Parâmetros:")
    r0 = st.sidebar.number_input("R0", value=r0)
    exposure_rate = st.sidebar.number_input("Taxa de exposição", value=exposure_rate, max_value=1.0)
    recovering_rate = st.sidebar.number_input("Taxa de recuperação", value=recovering_rate, max_value=1.0)
    death_rate = st.sidebar.number_input("Taxa de mortalidade", value=death_rate, max_value=1.0)
    death_proportion_rate = st.sidebar.number_input("Taxa proporcional de mortalidade", value=death_proportion_rate, max_value=1.0)
    
   
    if st.sidebar.button("Rodar simulação"):
        experiments = run.run(r0, recovering_rate, exposure_rate, death_rate, death_proportion_rate,susceptible, exposed, infected, recovered, dead)
        seir_df = experiments.dataset[0]
        st.write(seir_df)
        seir_df = seir_df.filter(items=['susceptible','exposed','infected','recovered','dead'])
        st.line_chart(seir_df)
	

if __name__=="__main__":
    main()