import streamlit as st
import run

R0 = 2.5

def main():
    st.markdown("# Seir Model")
    st.sidebar.number_input("R0", R0)
   
    st.sidebar.button("Rodar simulação")
    experiments = run.run()
    seir_df = experiments.dataset[0]
    st.write(seir_df)
    seir_df = seir_df.filter(items=['susceptible','exposed','infected','recovered','dead'])
    st.line_chart(seir_df)
	

if __name__=="__main__":
    main()