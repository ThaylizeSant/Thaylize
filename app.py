import streamlit as st

st.title("Fahrenheit -> Celsius")

num1 = st.number_input("Digite o primeiro número: ")

if st.button("Calcular"):
    resultado = (num1 - 32) / 1,8
    st.text("Resultado:")
    st.title(resultado)