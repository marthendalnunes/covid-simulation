import streamlit as st

import pages.seir
import pages.about

PAGES = {
    "Seir": pages.seir,
    "Sobre": pages.about
}

def main():
    st.markdown("test")
    
    st.sidebar.markdown("# Navegação")
    goto = st.sidebar.radio("Ir para", list(PAGES.keys()))
    PAGES[goto].write()

if __name__=="__main__":
    main()