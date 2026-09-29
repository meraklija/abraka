import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client ltxv_qI4iY8OQPxqUuUnmdhQuQzSvkCx0yPopl-jj7AA89Xc
# Alternatively, set it as an environment variable: os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key="ltxv_qI4iY8OQPxqUuUnmdhQuQzSvkCx0yPopl-jj7AA89Xc")

# Configure the web page
st.set_page_config(page_title="AI Image Studio", page_icon="🎨", layout="centered")

st.title("🎨 AI Image Studio")
st.write("Craft your prompts and generate high-resolution images.")

# Application UI Components
with st.form("image_gen_form"):
    # Text input for the main prompt
    prompt = st.text_area(
        "Enter your prompt:", 
        value="A highly detailed backyard treehouse with a swing, photorealistic, cinematic lighting, 8k resolution",
        height=100
    )
    
    # Options for aspect ratio (DALL-E 3 supports these specific dimensions)
    size_option = st.selectbox(
        "Select Size & Aspect Ratio:", 
        [
            "1024x1792 (Vertical 9:16)", 
            "1792x1024 (Landscape 16:9)",
            "1024x1024 (Square 1:1)"
        ]
    )
    
    # Submit button
    submitted = st.form_submit_button("Generate Image")

# Logic to run when the button is clicked
if submitted:
    if not prompt.strip():
        st.warning("Please enter a prompt to generate an image.")
    else:
        with st.spinner("Generating your image... this usually takes 10-15 seconds."):
            try:
                # Extract just the resolution string (e.g., "1024x1792")
                resolution = size_option.split(" ")[0]
                
                # Call the Image Generation API
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=resolution,
                    quality="hd", # High definition for photorealism
                    n=1,
                )
                
                # Fetch and display the resulting image
                image_url = response.data[0].url
                st.image(image_url, caption="Generated Result", use_column_width=True)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
