import pandas as pd
import streamlit as st


primaryColor="#F7CACA"

backgroundColor="#FFFFFF"
secondaryBackgroundColor="#93A9D1"
textColor="#F7CACA"
font="sans serif"



st.title("Formulario de Carat Membership")

form_values = {
    "name": None,
    "bday": None,
    "email": None,
    "telefono": None,
    "twitter": None,
    "instagram":None,
    "caratb": None,
    "bias": None,
    "biasss": None
}

with st.form(key="sample_form"):

    st.subheader("Datos Personales")
    name = st.text_input("Escribe tu nombre")
    bday = st.date_input("Seleccioná fecha de nacimiento")
    email = st.text_input("Escribe tu e-mail")
    telefono = st.text_input("Escribe tu número de teléfono")
    twitter = st.text_input("Escribe tu cuenta de twitter")
    instagram = st.text_input("Escribe tu cuenta de Instagram")

    st.subheader("Datos Carat")
    caratb = st.date_input("Soy Carat desde:")    
    bias = st.radio("Mi bias es:", ['S.Coups', 'Jeonghan', 'Joshua', 'Jun', 'Hoshi', 'Wonwoo', 'Woozi', 'DK', 'Mingyu', 'The8', 'Seungkwan', 'Vernon', 'Dino'])
    biasss = st.text_area("Si tenés más de un bias, escríbelo aquí:")


    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if not all(form_values()):
            st.warning("Ey,Carat! asegúrate de llenar todos los datos :)")

