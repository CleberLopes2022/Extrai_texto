import streamlit as st
from PIL import Image
import pytesseract
import fitz

# Defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'pytesseract.exe'  # Exemplo para Windows


# Função para extrair texto de imagens
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# Função para extrair texto de PDFs
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page in doc:
        text += page.get_text()
    return text

# Configuração do Streamlit
st.title("Extração de Texto de Imagens e PDFs")
st.write("Envie uma imagem ou um arquivo PDF para extrair o texto.")

# Opção para upload de arquivos
uploaded_file = st.file_uploader("Escolha uma imagem ou um arquivo PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        # Para imagens
        image = Image.open(uploaded_file)
        text = extract_text_from_image(image)
        st.subheader("Texto Extraído da Imagem:")
        st.text_area("Texto:", text, height=300)
        
    elif uploaded_file.type == "application/pdf":
        # Para PDFs
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("Texto Extraído do PDF:")
        st.text_area("Texto:", text, height=300)


