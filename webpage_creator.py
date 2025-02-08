import streamlit as st
import pyshorteners
import qrcode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


# Default message
default_message = "From the moment you entered my life, you've painted my world with colors I never knew existed. Your smile brightens my darkest days, and your love makes my heart dance with joy. Every moment spent with you feels like a beautiful dream I never want to wake up from."

# Function to generate a QR code with a love theme
def generate_love_qr(data):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR Code Image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Add Valentine-themed overlay (e.g., heart)
    heart = Image.open('/Users/dineshsayana/Code-Challenges/heart.png').resize((50, 50))  # Make sure to have a heart.png file
    pos = ((qr_img.size[0] - heart.size[0]) // 2, (qr_img.size[1] - heart.size[1]) // 2)
    qr_img.paste(heart, pos, heart)

    # Save QR Code
    qr_img.save("valentine_qr_code.png")

    return qr_img

# Streamlit app
st.title("Valentine's Day Website Creator :heart:")
st.write("Create a personalized message for your loved one :two_hearts:")

with st.form(key='valentine_form'):
    your_name = st.text_input("Your Name")
    valentine_name = st.text_input("Valentine's Name")
    message = st.text_area("Message", value=default_message)
    your_email = st.text_input("Your Email")
    submit_button = st.form_submit_button(label='Create Valentine Website')

if submit_button:
    if your_name and valentine_name and message and your_email:
        # Create the personalized URL
        base_url = "https://peaceful-manatee-f3201a.netlify.app/"
        personalized_url = f"{base_url}?name={valentine_name}&user={your_name}&message={message}&your_email={your_email}"

        # Shorten the URL
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(personalized_url)

        # Generate the QR code
        qr_image = generate_love_qr(short_url)

        # Display results
        st.success("Valentine's Day website created successfully!")
        st.write("**Shortened URL:**", short_url)

        # Display QR code
        st.image(qr_image, caption='Scan this QR code to visit your personalized Valentine website')

    else:
        st.error("Please fill in all fields.")