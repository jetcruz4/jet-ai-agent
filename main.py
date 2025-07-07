import streamlit as st
import openai
import os

st.set_page_config(page_title="JetCruz AI Agent", layout="centered")

st.title("JetCruz AI Agent")
st.markdown("Enter a name or company and let the agent generate an outreach email.")

openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

name = st.text_input("Name or Company")
fuel_type = st.selectbox("Fuel Type", ["JET-A1", "EN-590", "D2", "Gasoil", "JP-54"])
region = st.text_input("Region (Optional)")
role = st.selectbox("Contact Role", ["Buyer", "Seller", "Mandate", "Unknown"])

if st.button("Generate Email"):
    with st.spinner("Thinking..."):
        prompt = f"Write a professional outreach email from Randy Avila at JetCruz Trading Co to a potential {role} of {fuel_type} in {region or 'their region'}, related to {name}."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        email = response['choices'][0]['message']['content']
        st.subheader("Generated Email")
        st.code(email)
