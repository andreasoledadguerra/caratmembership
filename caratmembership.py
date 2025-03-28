import pandas as pd
import streamlit as st
import gspread 

from oauth2client.service_account import ServiceAccountCredentials


# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo (reemplaza con el nombre de tu hoja)
spreadsheet = client.open("MiBaseDeDatos")
sheet = spreadsheet.sheet1


st.set_page_config(page_title="Formulario de Carat Membership", theme={"primaryColor": "#ffc3c5", "backgroundColor": "#FFFFFF"})

primaryColor="#ffc3c5"

backgroundColor="#FFFFFF"
secondaryBackgroundColor="#92a8d1"




textColor="#ffc3c5"
font="Playfair Display"



#st.title("Formulario de Carat Membership")

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
    twitter = st.text_input("Escribe tu cuenta de twitter(X)")
    instagram = st.text_input("Escribe tu cuenta de Instagram")

    if st.button("Guardar"):
        sheet.append_row([name, bday, email, telefono, twitter(X), instagram])
        st.success("Datos guardados exitosamente!")

    st.subheader("Datos Carat")
    caratb = st.date_input("Soy Carat desde:")    
    bias = st.radio("Mi bias es:", ['S.Coups', 'Jeonghan', 'Joshua', 'Jun', 'Hoshi', 'Wonwoo', 'Woozi', 'DK', 'Mingyu', 'The8', 'Seungkwan', 'Vernon', 'Dino'])
    biasss = st.text_area("Si tenés más de un bias, escríbelo aquí:")


    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if not all(form_values()):
            st.warning("Ey,Carat! asegúrate de llenar todos los datos :)")




