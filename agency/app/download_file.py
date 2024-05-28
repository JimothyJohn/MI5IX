import streamlit as st
import os

# Define the path to your local HTML file
local_html_path = 'outputs/index.html'

# Read the file content
with open(local_html_path, 'r') as file:
    file_content = file.read()

# Streamlit app title
st.title('Streamlit Link to Local HTML File')

# Create a link to the local HTML file for opening in browser
file_url = f"file://{os.path.abspath(local_html_path)}"
st.markdown(f'[Open Local HTML File]({file_url})')

# Add some more elements to the app if needed
st.write('Click the link above to open the local index.html file in your default web browser.')

# Provide a download button for the local HTML file
st.download_button(
    label='Download Local HTML File',
    data=file_content,
    file_name='index.html',
    mime='text/html'
)
