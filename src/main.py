import streamlit as st
import openai
from translator_ai import translator_ai
st.set_page_config(
    page_title = "Translator_Ai",
    page_icon="👤",
    layout="centered"
)

# Streamlit page title

st.title("👤Translator App-GPT")
col1,col2 = st.columns(2)
with col1:
    input_languages_list = ["English","French","German","latin","Spanish","Hindi","Telugu","Marathi"]
    input_language = st.selectbox(label="input_language",options=input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label = "Output_language",options=output_languages_list)

input_text = st.text_area("Type the text to be translator")
if st.button("Translator"):
    translate_text = translator_ai(input_language,output_language,input_text)
    st.success(translate_text)

