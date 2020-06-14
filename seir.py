import streamlit as st
import run

infection_rate = 1
recovering_rate = 1/4
exposure_rate = 1/3
death_rate = 0.01
death_proportion_rate = 1/9

def main():
 
    st.markdown("Seir model")
    st.sidebar.number_input("Infection rate", infection_rate)
    st.sidebar.number_input("Recovering rate", recovering_rate)
    st.sidebar.number_input("Exposure rate", exposure_rate)
    st.sidebar.number_input("Death rate", death_rate)
    st.sidebar.number_input("Death proportional rate", death_proportion_rate)
    experiments = run.run()
    df = experiments.dataset[1]
    st.write(df)    
    df = df.filter(items=['susceptible', 'exposed', 'infected', 'recovered', 'dead'])
    st.line_chart(df)
    
if __name__=="__main__":
    main()