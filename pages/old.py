import streamlit as st

import pages.seir
import pages.about

PAGES = {
    "Seir": pages.seir,
    "About": pages.about
}

def main():
    st.markdown("# Covid-19 model simulator")
    
    st.sidebar.markdown("# Navegação")
    goto = st.sidebar.radio("Ir para", list(PAGES.keys()))
    PAGES[goto].main()

if __name__=="__main__":
    main()
