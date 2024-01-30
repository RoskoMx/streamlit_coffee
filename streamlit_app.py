from pathlib import Path # Para las rutas de archivos

import streamlit as st  # pip install streamlit
from PIL import Image  # pip install pillow

# --- PATHS O RUTAS DE ACCESO A LOS ARCHIVOS ---
DIR_ACTUAL = Path(__file__).parent if "__file__" in locals() else Path.cwd() #Path.cwd sirve para obtener el directorio actual, en caso de que no estuviera disponible
DIR_ADJUNTOS = DIR_ACTUAL / "assets"
DIR_ESTILOS = DIR_ACTUAL / "styles"
ARCH_CSS = DIR_ESTILOS / "main.css"


# --- CONFIGURACIONES DE VARIABLES GENERALES ---
ENLACE_DONACION = "https://buy.stripe.com/8wM17J2J5fgD2A0eUU"
EMAIL_CONTACTO = "GUZTAVO.MEJIA@GMAIL.COM"
VIDEO_TUTORIAL = "https://youtu.be/PmJ9rkKGqrI"
NOMBRE_PRODUCT = "Présentation du projet"
NOMBRE_PRODUCT1 = "L'internet pour mes parents"
SLOGAN_PRODUCTO = "Internet pour les débutants. 🫵"
DESCRIPCION_PRODUCTO = """
Page Internet conçue pour faciliter l'approche 
des personnes extérieures à la technologie, qui 
souhaitent rendre leur entreprise visible sur Internet.

- Avec des instructions simples
- Sans rien installer sur votre ordinateur
- Accompagnement personnalisé
- S'appuyer sur des outils d'intelligence artificielle
- ... Et bien d’autres options incroyables à explorer
** Vous acquérez un nouveau super pouvoir. Qu'allez-vous faire pour le développer? **
"""


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- CONFIGURACIÓN DE LA PESTAÑA ---
st.set_page_config(
    page_title = NOMBRE_PRODUCT1,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(ARCH_CSS)


# --- SECCIÓN PRINCIPAL ---
logo_image = Image.open(DIR_ADJUNTOS / "rosko_internet.jpg")
st.image(logo_image, width=450)
st.header(NOMBRE_PRODUCT)
st.subheader(SLOGAN_PRODUCT)

left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(DESCRIPCION_PRODUCT)
    #Se inserta un enlace HTML usando el elemento Markdown. Una opción para hacer el botón más atractivo con CSS, que se llamarpa más adelante
    st.markdown(
        f'<a href={ENLACE_DONACION} class="button"> 👉 Envoie-moi un petite café </a>',
        unsafe_allow_html=True, #Desea incluir HTML unsafe? True
    )
with right_col:
    product_image = Image.open(DIR_ADJUNTOS / "rosko2.jpg")
    st.image(product_image, width=450)


# --- MAYORES CARACTERÍSTICAS ---
st.write("")
st.write("---")
st.subheader(":rocket: Ce que nous pouvons réaliser")
#Creamos un diccionario que contiene la información de 3 secciones de características. Cada una debe tener: imagen, encabezado y descripción.
#Nombre de la imágen, como clave del diccionario. El valor de esa clave será una lista[Dos elementos dentro, encabezado y explicación],
features = {
    "Feature_1.png": [
        "Run Python Files From Excel",
        "After locating your Python interpreter, you can execute Python files directly from Excel. In the Pro Version, you can also add several Python interpreter paths. This is helpful when you need to execute your Python code from different virtual environments.",
    ],
    "Feature_2.png": [
        "Create Pandas Dataframes",
        "Generate Python files with a click of a button. Select the cell range you want to transform, and the add-in creates the Python code to read in the Excel data as a pandas dataframe.Instead of messing around with all of the available options in the pandas ‘read_excel’ method, the add-in does it for you.",
    ],
    "Feature_3.png": [
        "Create Jupyter Notebooks",
        "Have you ever wanted to do some quick analysis of your Excel data in a Jupyter Notebook? MyToolBelt can convert an Excel cell range into a Jupyter Notebook. Just select the cell range, and the add-in will create a new Jupyter Notebook in the workbook’s directory. Inside the Jupyter Notebook, you will find your ready-to-use dataframe based on your selection. This feature is a real time saver!",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)


# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1": "Some text goes here to answer question 1",
    "Question 2": "Some text goes here to answer question 2",
    "Question 3": "Some text goes here to answer question 3",
    "Question 4": "Some text goes here to answer question 4",
    "Question 5": "Some text goes here to answer question 5",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


# --- CONTACT FORM ---
# video tutorial: https://youtu.be/FOULV9Xij_8
st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
