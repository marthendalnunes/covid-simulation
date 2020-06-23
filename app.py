import streamlit as st
import run


def main():
    # Simulation parameters
    simulation_time_steps = 100    

    # Initial Values
    susceptible = 9900
    exposed = 100
    infected = 0
    dead = 0
    recovered = 0

    # Model parameters
    r0 = 2.5
    recovering_rate = 0.25
    exposure_rate = 0.3
    death_rate = 0.01
    death_proportion_rate = 0.11

    
    st.markdown("### Covid-19 SEIRD model")
    "This is the standard introductory model for Covid-19 spread. It is based on the following equations:"
    st.latex(r"""
    \frac {d}{dt}Susceptible = - \beta * Infected * {\frac {Susceptible}{Total Population}}
    """)
    st.latex(r"""
    \frac {d}{dt}Exposed = \beta * Infected * {\frac {Susceptible}{Total Population}} - \delta * Exposed 
    """)
    st.latex(r"""
    \frac{d}{dt}Infected = \delta * Exposed - (1 - \alpha) * \gamma * Infected - \alpha * \rho * Infected
    """)
    st.latex(r"""
    \frac {d}{dt}Recovered = (1 - \alpha) * \gamma *Infected
    """)
    st.latex(r"""
    \frac {d}{dt}Dead = \alpha * \rho * Infected
    """)

    r"""
    Where the parameters are:
    - 𝛽: expected amount of people an infected person infects per day
    - 𝛾: proportion of infected recovering per day [𝛾 = 1 / recovering days]
    - 𝛿: expected rate that exposed people turn into infected
    - 𝜌: rate at wich infected people die per day [𝜌 = 1 / amount of days to an infected person die]
    - 𝛼: death probability
    - 𝑅₀: total number of people an infected person infects (R₀ = 𝛽 / 𝛾)
    """

    st.sidebar.markdown("Simulation Parameters:")
    simulation_time_steps = st.sidebar.number_input("Simulation Lenght (days):", value=simulation_time_steps, min_value=2)
    st.sidebar.markdown("Initial States:")
    susceptible = st.sidebar.number_input("Susceptible", value=susceptible)
    exposed = st.sidebar.number_input("Exposed", value=exposed)
    infected = st.sidebar.number_input("Infected", value=infected)
    dead = st.sidebar.number_input("Dead", value=dead)
    recovered = st.sidebar.number_input("Recovered", value=recovered)
    st.sidebar.markdown("Model Parameters:")
    r0 = st.sidebar.number_input("Reproduction Rate [𝛽/𝛾]", value=r0)
    exposure_rate = st.sidebar.number_input("Exposure Rate [𝛿]", value=exposure_rate, max_value=1.0)
    recovering_rate = st.sidebar.number_input("Recovering Rate [𝛾]", value=recovering_rate, max_value=1.0)
    death_rate = st.sidebar.number_input("Death probability [𝛼]", value=death_rate, max_value=1.0)
    death_proportion_rate = st.sidebar.number_input("Daily death proportion [𝜌]", value=death_proportion_rate, max_value=1.0)
    if st.sidebar.button("Run simulaton"):
        import run
        experiments = run.run(simulation_time_steps, r0, recovering_rate, exposure_rate, death_rate, death_proportion_rate,susceptible, exposed, infected, recovered, dead)
        seir_df = experiments.dataset[len(experiments.index)-1] # get the last dataset
        st.write(seir_df)
        seir_df = seir_df.filter(items=['susceptible','exposed','infected','recovered','dead'])
        st.line_chart(seir_df)
	

if __name__=="__main__":
    main()
