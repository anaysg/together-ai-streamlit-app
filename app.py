import streamlit as st
import together

# Set page title
st.set_page_config(page_title="Python Code Generator with Together AI")

# App title
st.title("🐍 Python Code Generator")
st.write("Enter a prompt below and Together AI will generate Python code for you.")

# Get API key from Streamlit Secrets
together.api_key = st.secrets["TOGETHER_API_KEY"]

# Prompt input
prompt = st.text_area("📝 Prompt", "Write a Python script to reverse a string.")

# Button
if st.button("Generate Code"):
    with st.spinner("Generating code..."):
        response = together.Complete.create(
            prompt=prompt,
            model="togethercomputer/CodeLlama-13b-Instruct",
            max_tokens=256,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.1,
            stop=["</s>"]
        )
        generated_code = response['output'].strip()
        st.code(generated_code, language="python")
