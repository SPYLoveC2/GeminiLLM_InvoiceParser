import streamlit as st
import os
import time
import io

from PIL import Image
from google import  generativeai as genai
from dotenv import load_dotenv

from template import get_system_prompt

load_dotenv()
system_prompt = get_system_prompt()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
models = ["gemini-1.5-pro", "gemini-2.0-flash", "gemini-1.5-flash-latest", "gemini-2.0-pro-exp"]
model = genai.GenerativeModel(models[2])  ### Use gemini 1.5 pro for proper functioning


def get_res(query, image, system_prompt):
    res = model.generate_content([system_prompt,image,query], stream=True)
    return res


st.set_page_config(page_title="LLM Powered Invoice Parser")
st.header("LLM Powered Invoice Parser")

uploaded_image = st.file_uploader("Choose Invoice", type=['jpg', 'jpeg', 'png'])
image = None
query = None
text_placeholder = st.empty()

if uploaded_image:
    text_placeholder.empty()
    image = Image.open(uploaded_image)
    st.image(image=image, caption='Uploaded Image', width=250)
    query = st.text_input("Input Prompt...", key="input")
    # byte_converter = io.BytesIO()
    # image.save(byte_converter, format='JPEG')
    # image = byte_converter.getvalue()s

submit = st.button("Ask Me")

if submit and query and image:
    response = get_res(query, image, system_prompt)
    st.subheader("The response is.")
    placeholder = st.empty()
    text = ""
    for chunk in response:
        for char in chunk.text:
            text+=char
            placeholder.write(text)
            time.sleep(0.005)

elif query and not image and submit:
    text_placeholder.write("Please upload a image")

elif image and not query and submit:
    text_placeholder.write("Plese raise a query")

elif submit and not image and not query:
    text_placeholder.write("Please choose a image first")


