import streamlit as st

import pages.covid_19.seir
import pages.about

PAGES = {
    "Seir": pages.covid_19.seir,
    "Sobre": pages.about
}

def main():
    st.markdown("test")
    
    st.sidebar.markdown("# Navegação")
    goto = st.sidebar.radio("Ir para", list(PAGES.keys()))
    PAGES[goto].main()

if __name__=="__main__":
    main()