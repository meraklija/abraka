import streamlit as st
from openai import OpenAI

# Load API key safely from Streamlit Cloud Secrets
api_key = st.secrets.get("ltxv_qI4iY8OQPxqUuUnmdhQuQzSvkCx0yPopl-jj7AA89Xc")

if not api_key:
    st.error("Please add your OPENAI_API_KEY to Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

st.set_page_config(page_title="AI Image Studio", page_icon="🎨")
st.title("🎨 AI Image Studio")

prompt = st.text_input("Enter your prompt:", "A futuristic cyberpunk city at sunset, 8k resolution")

if st.button("Generate"):
    with st.spinner("Generating image..."):
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                n=1,
            )
            st.image(response.data[0].url, use_column_width=True)
        except Exception as e:
            st.error(f"Error: {e}")