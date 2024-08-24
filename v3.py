# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad
# import math
# import os
# import requests
# from PIL import Image
# import streamlit as st
# import webbrowser
# import base64
# from db_utils import save_file_details
# import json
# import base64
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad
# import webbrowser


# def encrypt_file_ui():

#     # Encryption key
#     key=b'\xbf\x1b\xb3O\x8fB\x88e\x04\xea\xfb\xcd{.\xa9\xdc<\xef\xeb\xb9\x08\x10\xd3\x18\x92\x0f\xb6\x80\xe1 <V'
#     user_id = st.session_state.get('user_id')

#     # Function to convert data to image
#     def data_to_image(data, image_path):
#         binary_data = "".join(format(byte, "08b") for byte in data)
#         data_len = len(binary_data)
#         img_width = int(math.sqrt(data_len)) + 1
#         img_height = int(math.ceil(data_len / img_width))
#         img = Image.new("L", (img_width, img_height), color=255)
#         for i, bit in enumerate(binary_data):
#             x = i % img_width
#             y = i // img_width
#             pixel_value = 255 - int(bit) * 255
#             img.putpixel((x, y), pixel_value)
#         img.save(image_path)

#     # Streamlit UI
#     st.title("Encrypt File")

#     # Upload the original image file
#     original_file = st.file_uploader("Upload the original file", type=["docx", "pdf", "jpg", "jpeg", "png", "gif", "mp3", "mp4", "avi", "zip", "rar", "pptx", "xlsx", "html", "css", "js", "php", "exe", "dll", "txt", "rtf"])
#     if original_file:
#         # Save the original file data to a variable
#         original_data = original_file.read()

#         # Get the file extension from the original file name
#         original_file_ext = os.path.splitext(original_file.name)[1]

#         # Reserve space for the file extension in the binary data
#         header_size = 4  # bytes
#         extension_size = len(original_file_ext)
#         reserved_data_size = header_size + extension_size
#         binary_data = bytearray(reserved_data_size + len(original_data))

#         # Add the file extension to the header
#         binary_data[:header_size] = extension_size.to_bytes(header_size, byteorder='big')
#         binary_data[header_size:header_size + extension_size] = original_file_ext.encode("utf-8")

#         # Add the original file data to the binary data
#         binary_data[reserved_data_size:] = original_data

#         # Convert the binary data to a binary string
#         binary_string = "".join(format(byte, "08b") for byte in binary_data)

#         # Write the binary string to a TXT file
#         with open("example.txt", "w") as f:
#             f.write(binary_string)

#         # Read the message from the text file
#         with open('example.txt', 'rb') as f:
#             message = f.read()

#         # Generate a random 16-byte initialization vector (IV)
#         iv = b'P\x05\x95\xac\xf5\x88\x9c\x1a\x89\x94 ^\x92i\xc8\xbc'

#         # Create an AES cipher object with the key and IV
#         cipher = AES.new(key, AES.MODE_CFB, iv)

#         # Pad the message so that its length is a multiple of 16
#         padded_message = pad(message, AES.block_size, style='pkcs7')

#         # Encrypt the padded message
#         encrypted_message = cipher.encrypt(padded_message)

#         # Convert the encrypted message to an image and save it
#         encrypted_image_path = 'encrypted_image.png'
#         data_to_image(encrypted_message, encrypted_image_path)

#         # Display the encrypted image
#         encrypted_image = Image.open(encrypted_image_path)
#         st.image(encrypted_image)

#         # Upload the encrypted image to IPFS
#         url = "https://api.verbwire.com/v1/nft/store/file"
#         files = {"filePath": ("encrypted_image.png", open(encrypted_image_path, "rb"), "image/png")}
#         headers = {
#             "accept": "application/json",
#             "X-API-Key": "sk_live_d9d9b80c-ff6a-4361-b396-39de40e3b6d7"
#         }
#         response = requests.post(url, files=files, headers=headers)
#         if response.status_code == 200:
#             ipfs_link = response.text  # Use .get() to avoid KeyError
#             if ipfs_link:
#                 st.success("Encrypted image uploaded to IPFS successfully!")
#                 st.write(f"IPFS Link: {ipfs_link}")
#                 if user_id:
#                         save_file_details(user_id, original_file.name, ipfs_link, key)
#                 else:
#                         st.error("User not logged in.")
#             else:
#                 st.error("IPFS link not found in the response.")
#         else:
#             st.error(f"Failed to upload encrypted image to IPFS. Error: {response.text}")
    
    

#     # Display the encryption key
#     st.subheader('Key')
#     st.code(key)

#     # Function to download a file
#     def download_file(file_path, file_name):
#         with open(file_path, "rb") as f:
#             file_bytes = f.read()
#         st.download_button(label="Download", data=file_bytes, file_name=file_name)

#     # Download button for the encrypted image
#     if 'encrypted_image_path' in globals():
#         download_file(encrypted_image_path, 'encrypted_image.png')

#     # Input for WhatsApp number
#     phone_number = st.text_input("Enter WhatsApp Number")

#     # Function to open WhatsApp URL
#     def open_url(message):
#         whatsapp_url = f"https://api.whatsapp.com/send/?phone={phone_number}&text={message}&type=phone_number&app_absent=1"
#         webbrowser.open_new_tab(whatsapp_url)

#     # Button to send the key and IPFS link to WhatsApp
#     if st.button('Send Key and IPFS Link to WhatsApp'):
#         # Encode the encryption key
#         #encoded_key = base64.b64encode(key).decode('utf-8')
#         # Construct the message
#         message = f"Encoded Encryption Key: {key}\n IPFS Link: {ipfs_link}"
#         open_url(message)
    
#     # Add margin
#     margin = '50px'
#     st.write(f'<div style="margin: {margin}"></div>', unsafe_allow_html=True)
import streamlit as st
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import math
import os
import requests
import webbrowser
from db_utils import save_file_details

def encrypt_file_ui():
    key = b'\xbf\x1b\xb3O\x8fB\x88e\x04\xea\xfb\xcd{.\xa9\xdc<\xef\xeb\xb9\x08\x10\xd3\x18\x92\x0f\xb6\x80\xe1 <V'
    user_id = st.session_state.get('user_id')

    def data_to_image(data, image_path):
        binary_data = "".join(format(byte, "08b") for byte in data)
        data_len = len(binary_data)
        img_width = int(math.sqrt(data_len)) + 1
        img_height = int(math.ceil(data_len / img_width))
        img = Image.new("L", (img_width, img_height), color=255)
        for i, bit in enumerate(binary_data):
            x = i % img_width
            y = i // img_width
            pixel_value = 255 - int(bit) * 255
            img.putpixel((x, y), pixel_value)
        img.save(image_path)

    st.title("Encrypt File")

    original_file = st.file_uploader("Upload the original file", type=["docx", "pdf", "jpg", "jpeg", "png", "gif", "mp3", "mp4", "avi", "zip", "rar", "pptx", "xlsx", "html", "css", "js", "php", "exe", "dll", "txt", "rtf"])
    if original_file:
        original_data = original_file.read()
        original_file_ext = os.path.splitext(original_file.name)[1]

        header_size = 4
        extension_size = len(original_file_ext)
        reserved_data_size = header_size + extension_size
        binary_data = bytearray(reserved_data_size + len(original_data))

        binary_data[:header_size] = extension_size.to_bytes(header_size, byteorder='big')
        binary_data[header_size:header_size + extension_size] = original_file_ext.encode("utf-8")
        binary_data[reserved_data_size:] = original_data

        binary_string = "".join(format(byte, "08b") for byte in binary_data)

        with open("example.txt", "w") as f:
            f.write(binary_string)

        with open('example.txt', 'rb') as f:
            message = f.read()

        iv = b'P\x05\x95\xac\xf5\x88\x9c\x1a\x89\x94 ^\x92i\xc8\xbc'
        cipher = AES.new(key, AES.MODE_CFB, iv)
        padded_message = pad(message, AES.block_size, style='pkcs7')
        encrypted_message = cipher.encrypt(padded_message)

        encrypted_image_path = 'encrypted_image.png'
        data_to_image(encrypted_message, encrypted_image_path)

        encrypted_image = Image.open(encrypted_image_path)
        st.image(encrypted_image)

        # Save the encrypted image path in session state
        st.session_state.encrypted_image_path = encrypted_image_path

        url = "https://api.verbwire.com/v1/nft/store/file"
        files = {"filePath": ("encrypted_image.png", open(encrypted_image_path, "rb"), "image/png")}
        headers = {
            "accept": "application/json",
            "X-API-Key": "sk_live_d9d9b80c-ff6a-4361-b396-39de40e3b6d7"
        }
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            ipfs_link = response.json().get('ipfs_link')
            if ipfs_link:
                st.success("Encrypted image uploaded to IPFS successfully!")
                st.write(f"IPFS Link: {ipfs_link}")
                if user_id:
                    save_file_details(user_id, original_file.name, ipfs_link, key)
                else:
                    st.error("User not logged in.")
            else:
                st.error("IPFS link not found in the response.")
        else:
            st.error(f"Failed to upload encrypted image to IPFS. Error: {response.text}")

    st.subheader('Key')
    st.code(key)

    def download_file(file_path, file_name):
        with open(file_path, "rb") as f:
            file_bytes = f.read()
        st.download_button(label="Download", data=file_bytes, file_name=file_name)

    # Show download button if encrypted image exists in session state
    if 'encrypted_image_path' in st.session_state:
        download_file(st.session_state.encrypted_image_path, 'encrypted_image.png')

    phone_number = st.text_input("Enter WhatsApp Number")

    def open_url(message):
        whatsapp_url = f"https://api.whatsapp.com/send/?phone={phone_number}&text={message}&type=phone_number&app_absent=1"
        webbrowser.open_new_tab(whatsapp_url)

    if st.button('Send Key and IPFS Link to WhatsApp'):
        message = f"Encoded Encryption Key: {key}\n IPFS Link: {st.session_state.get('ipfs_link', '')}"
        open_url(message)

    margin = '50px'
    st.write(f'<div style="margin: {margin}"></div>', unsafe_allow_html=True)

# Run the Streamlit app
encrypt_file_ui()
