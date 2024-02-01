from pathlib import Path # Para las rutas de archivos
#import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image  # pip install pillow

# --- PATHS O RUTAS DE ACCESO A LOS ARCHIVOS ---
DIR_ACTUAL = Path(__file__).parent if "__file__" in locals() else Path.cwd() #Path.cwd sirve para obtener el directorio actual, en caso de que no estuviera disponible
DIR_ADJUNTOS = DIR_ACTUAL / "assets"
DIR_ESTILOS = DIR_ACTUAL / "styles"
ARCH_CSS = DIR_ESTILOS / "main.css"


# --- CONFIGURACIONES DE VARIABLES GENERALES ---
ENLACE_DONACION = "https://buy.stripe.com/8wM17J2J5fgD2A0eUU"
EMAIL_CONTACTO = "GUZTAVO.MEJIA@GMAIL.COM"
VIDEO_TUTORIAL = "https://www.youtube.com/watch?v=HQdZgEL2Xbs"
NOMBRE_PRODUCT = "Présentation du projet"
NOMBRE_PRODUCT1 = "Technologie pour les débutants"
SLOGAN_PRODUCTO = "L'intelligence Artificiale pour les débutants. 🫵"
DESCRIPCION_PRODUCTO = """
Page Internet conçue pour faciliter l'approche 
des personnes extérieures à la technologie, qui 
souhaitent rendre leur entreprise visible sur Internet:



- Avec des instructions simples
- Sans rien installer sur votre ordinateur
- Accompagnement personnalisé
- S'appuyer sur des outils d'intelligence artificielle
- ... Et bien d’autres options incroyables à explorer




**Vous acquérez un nouveau super pouvoir. Qu'allez-vous faire pour le développer?**
"""

#Una vez teniendo el CSS se define la función y se ejecuta justo después de la config de pestaña
def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- CONFIGURACIÓN GENERAL DE LA PÁGINA (PESTAÑA, DISTRIBUCIÓN, BARRA) ---
st.set_page_config(
    page_title = NOMBRE_PRODUCT1,
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded",
)
load_css_file(ARCH_CSS)


# --- SECCIÓN PRINCIPAL ---
logo_image = Image.open(DIR_ADJUNTOS / "rosko_internet.png")
st.image(logo_image, width=450)
st.header(NOMBRE_PRODUCT)
st.subheader(SLOGAN_PRODUCTO)

left_col, right_col = st.columns((1, 1))
with left_col:
    st.text("")
    st.write(DESCRIPCION_PRODUCTO)
    #Se inserta un enlace HTML usando el elemento Markdown. Una opción para hacer el botón más atractivo con CSS, que se llamarpa más adelante
    #st.markdown(
        #f'<a href={ENLACE_DONACION} class="button"> 👉 Envoie-moi un petite café </a>',
        #unsafe_allow_html=True, #Desea incluir HTML unsafe? True
    #)
with right_col:
    product_image = Image.open(DIR_ADJUNTOS / "_78b21d3a-8a30-41e0-b5e0-9407987b880c.jpg")
    st.image(product_image, width=400)
    
# --- MAYORES CARACTERÍSTICAS ---
st.write("")
st.write("---")
st.subheader(":rocket: Ce que nous pouvons réaliser avec la generation des images.")
#Creamos un diccionario que contiene la información de 3 secciones de características. Cada una debe tener: imagen, encabezado y descripción.
#Nombre de la imágen, como clave del diccionario. El valor de esa clave será una lista[Dos elementos dentro, encabezado y explicación],
features = {
    "chachi.jpg": [
        "Créer des stickers",
        "Créez des images amusantes de votre animal pour créer de nombreux autocollants et collez-les où vous le souhaitez.",
    ],
    "_e7cf7aa0-d5f6-431e-b39a-6e40146f13ff.jpg": [
        "Votre marque dans des produits incroyables",
        "Créez des personnages géniaux en utilisant les produits de vos rêves grâce à la génération d'images.",
    ],
    "french_guajolote2.jpg": [
        "Des photographies presque réelles",
        "Faites ressembler vos idées les plus folles à une vraie photo. Des instructions simples pour matérialiser les idées dans votre esprit.",
    ],
}
for image, description in features.items():
    image = Image.open(DIR_ADJUNTOS / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True) #Mismo ancho
    right_col.write(f"**{description[0]}**") #Fuente en negritas
    right_col.write(description[1])


# --- VIDEO DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Nous pouvons faire une vidéo où nous parlons différentes langues")
st.video(VIDEO_TUTORIAL, format="video/mp4", start_time=0)#Se puede modificar la hora de inicio
#youtube_image = Image.open(DIR_ADJUNTOS / "Te regalo una.png")
#st.image(youtube_image)


# --- SECCIÓN DE PREGUNTAS Y RESPUESTAS ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ Section")
#Este es un diccionario donde la clave es la pregunta y su respuesta será su valor
faq = {
    "Est-il nécessaire de payer quelque chose pour utiliser tout cela?": "Dans ce projet, nous cherchons à rapprocher les gens de la technologie sans avoir à dépenser un seul euro",
    "Dois-je installer un certain type de programme sur mon ordinateur?": "Absolument rien, tous les outils que nous présentons ici sont disponibles sur internet",
    "Puis-je utiliser cet exemple de page pour créer mon propre projet?": "Bien entendu, il vous suffit d’inclure vos propres images et de décrire votre projet avec vos propres mots.",
    "Où puis-je contacter le créateur pour poser une question spécifique ?": "Toutes les informations de contact figurent dans la section suivante",
}
#Recorremos el diccionario y mostramos respuesta en elemento expandible
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


# --- FORMULARIO DE CONTACTO ---
#Colocamos un formulario HTML en modo streamlit usando un elemento de rebajas
#Más información en: https://youtu.be/FOULV9Xij_8
st.write("---")
st.subheader(":mailbox: N'hésitez pas à m'envoyer un message. Je serai heureux de vous aider.!")
contact_form = f"""
<form action="https://formsubmit.co/{EMAIL_CONTACTO}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Votre nome" required>
     <input type="email" name="email" placeholder="Votre email" required>
     <textarea name="message" placeholder="Votre question ou message ici"></textarea>
     <button type="submit" class="button">Envoyer ✉</button>
</form>
"""
#Por sí solo, el botón no está presentable. Recurrimos al archivo CSS

#Para los detalles del fondo blanco, se crea una nueva carpeta llamada .streamlit con un archivo "config.toml
st.markdown(contact_form, unsafe_allow_html=True)



# --- OPCIÓN DE DONACIÓN ---
st.write("")
st.write("---")
st.subheader("🧌 Offre-moi un petite café.")

columna1, columna2 = st.columns((2, 1))
with columna1:
    st.text("")
    st.write("Si vous avez aimé ce contenu ou le jugez utile, n'hésitez pas à m'offrir un délicieux café.")
    #Se inserta un enlace HTML usando el elemento Markdown. Una opción para hacer el botón más atractivo con CSS, que se llamarpa más adelante
    st.markdown(
        f'<a href={ENLACE_DONACION} class="button"> 👉 Envoie-moi un petite café </a>',
        unsafe_allow_html=True, #Desea incluir HTML unsafe? True
    )
with columna2:
    cafecito_image = Image.open(DIR_ADJUNTOS / "_3bcabb31-19ce-46e1-a942-103e4e2c1921.jpg")
    st.image(cafecito_image, width=200)
