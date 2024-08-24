from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
import streamlit as st
import os
import requests
from io import BytesIO

def decrypt_file_ui():
    st.title("Decrypt File")


    key=b'\xbf\x1b\xb3O\x8fB\x88e\x04\xea\xfb\xcd{.\xa9\xdc<\xef\xeb\xb9\x08\x10\xd3\x18\x92\x0f\xb6\x80\xe1 <V'

    # Function to retrieve file from IPFS using its hash
    def retrieve_file_from_ipfs(ipfs_link):
        

        # Send a GET request to the file URL
        response = requests.get(ipfs_link)

        if response.status_code == 200:
            # Return the content of the file
            return response.content
        else:
            # Return None if the file retrieval fails
            
            return None


    def image_to_data(image_path):
        img = Image.open(image_path).convert("L")
        width, height = img.size
        binary_str = ""
        for i in range(height):
            for j in range(width):
                pixel_value = img.getpixel((j, i))
                binary_str += "1" if pixel_value < 128 else "0"
        binary_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
        return binary_data


    def decrypt_image(encrypted_image_path, key, iv, output_file_path):
        # Read the encrypted message from the image
        encrypted_message = image_to_data(encrypted_image_path)

        # Create an AES cipher object with the key and IV
        cipher = AES.new(key,AES.MODE_CFB, iv)

        # Decrypt the encrypted message
        decrypted_message = cipher.decrypt(encrypted_message)

        # Unpad the decrypted message
        unpadded_message = pad(decrypted_message, AES.block_size)

        # Write the decrypted message to a text file
        with open(output_file_path, 'wb') as f:
            f.write(unpadded_message)

    # Read the key and IV used for encryption
    key2=st.text_input("Enter Key")
    iv = b'P\x05\x95\xac\xf5\x88\x9c\x1a\x89\x94 ^\x92i\xc8\xbc'

    # Add a section to input the IPFS link
    ipfs_link = st.text_input("Enter IPFS link")

        # Add a button to fetch the file from IPFS
    if st.button("Fetch File from IPFS"):
            if ipfs_link:
                
                    # Retrieve the file content from IPFS
                    file_content = retrieve_file_from_ipfs(ipfs_link)

                    if file_content:
                        # Open the file content as an image
                        img = Image.open(BytesIO(file_content))
                        
                        # Save the image as a PNG file
                        img.save("retrieved_file.png", "PNG")
                        
                        # Provide a download button for the retrieved PNG file
                        st.download_button(
                            label="Download IPFS File (PNG)",
                            data=open("retrieved_file.png", "rb").read(),
                            file_name="retrieved_file.png",
                            mime="image/png"
                        )
                    else:
                        st.write("Failed to retrieve file from IPFS. Please check the IPFS link.")
                
            else:
                st.write("Please enter the IPFS link.")

    # Decrypt the message from the image and write it to a text file
    output_file_path = 'Cell6.txt'

    # Code to decrypt the image file and process the result
    uploaded_file = st.file_uploader("Drag and drop an image here", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        decrypt_image(uploaded_file, key, iv, output_file_path)
    else:
        st.write("Drag and drop an image file to decrypt.")

    with open("Cell6.txt", "rb") as input_file, open("process.txt", "w") as output_file:
        # Read the contents of the input file as bytes
        input_bytes = input_file.read()

        # Convert bytes to string using utf-8 encoding
        input_str = input_bytes.decode("utf-8", errors="ignore")

        # Remove any characters other than 0 and 1
        filtered_str = ''.join(c for c in input_str if c in {'0', '1'})

        # Write the filtered string to the output file
        output_file.write(filtered_str)

    # Define the path and name of the binary TXT file
    binary_file_path = "process.txt"

    # Read the binary string from the TXT file
    with open(binary_file_path, "r") as f:
        binary_string = f.read()

    # Convert the binary string to binary data
    binary_data = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    # Get the file extension from the binary data header
    header_size = 4 # bytes
    extension_size = int.from_bytes(binary_data[:header_size], byteorder='big')
    original_file_ext = binary_data[header_size:header_size+extension_size].decode("utf-8")

    # Extract the original file data from the binary data
    original_data = binary_data[header_size+extension_size:]

    # Write the original file with the correct file extension
    with open("example3" + original_file_ext, "wb") as f:
        f.write(original_data)

    # Define a function that returns the content of the file as a byte string
    def get_file_content_as_string(file):
        content = file.read()
        return content

    # Define the Streamlit app
    def app():  


        
        # Add a download button
        st.download_button(
        label="Download",
        data=bytes(original_data),
        file_name="example3." + original_file_ext,
        mime="text/plain"
        )

    # Delete the files after execution
    # Clear the content of the files after execution
    with open("Cell6.txt", "w") as f:
        f.truncate(0)

    with open("process.txt", "w") as f:
        f.truncate(0)
    app()

# Call the Streamlit app
if __name__ == "__main__":
     decrypt_file_ui()