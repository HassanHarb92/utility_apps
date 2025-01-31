import streamlit as st
from rembg import remove
from PIL import Image
import io

# Streamlit App
st.title("🖼️ Background Remover App")

st.write("Upload an image, and this app will remove its background.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    input_image = Image.open(uploaded_file)
    
    st.subheader("Original Image")
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    # Remove background
    with st.spinner("Processing..."):
        output_image = remove(input_image)

    st.subheader("Image with Background Removed")
    st.image(output_image, caption="Processed Image", use_column_width=True)

    # Convert output image to bytes for download
    img_bytes = io.BytesIO()
    output_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Download button
    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="background_removed.png",
        mime="image/png",
    )

st.write("Built with ❤️ using Streamlit & rembg!")

