import streamlit as st

R0 = 2.5

def main():
    st.markdown("# Seir Model")
    st.sidebar.number_input("R0", R0)

    if st.sidebar.button("Rodar simulação"):
        st.write("Rodando")

if __name__=="__main__":
    main()