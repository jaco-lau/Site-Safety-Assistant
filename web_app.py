import streamlit as st
import pandas as pd 
import numpy as np
import base64

from pathlib import Path

from PIL import Image

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Function to read in import markdown file
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Import safety violation reports
carp1_markdown = read_markdown_file('./streamlit_app/carpentry_safety_violation_report_1.md')
carp2_markdown = read_markdown_file('./streamlit_app/carpentry_safety_violation_report_2.md')
carp3_markdown = read_markdown_file('./streamlit_app/carpentry_safety_violation_report_3.md')

elec1_markdown = read_markdown_file('./streamlit_app/electric_safety_violation_report_1.md')
elec2_markdown = read_markdown_file('./streamlit_app/electric_safety_violation_report_2.md')
elec3_markdown = read_markdown_file('./streamlit_app/electric_safety_violation_report_3.md')

hvac1_markdown = read_markdown_file('./streamlit_app/hvac_safety_violation_report_1.md')
hvac2_markdown = read_markdown_file('./streamlit_app/hvac_safety_violation_report_2.md')
hvac3_markdown = read_markdown_file('./streamlit_app/hvac_safety_violation_report_3.md')

plumb1_markdown = read_markdown_file('./streamlit_app/plumbing_safety_violation_report_1.md')
plumb2_markdown = read_markdown_file('./streamlit_app/plumbing_safety_violation_report_2.md')
plumb3_markdown = read_markdown_file('./streamlit_app/plumbing_safety_violation_report_3.md')

# Specify trades
trades = ['Select Trade','Carpentry','Electric','Mechanical/HVAC','Plumbing']

# Specify number of possible offenses
offense = ['Select Offense','1st Offense','2nd Offense','3rd Offense']

# Title of app
st.title("Site Safety Assistant")

# Upload and open image
fileUpload = st.file_uploader("Choose a file", type = ['jpg', 'png'])
if fileUpload:
    file = Image.open(fileUpload)
    resized = file.resize((416,416))
    st.image(resized, width = 416, height = 416)

    # Confirm or Cancel buttons
    result = st.button('Confirm Image')
    result_2 = st.button('Cancel')

    #Run model if image confirmed
    if result:
        # Load model
        model = load_model('./streamlit_app/models/site_safety/')
        # Convert image to array
        array = img_to_array(resized)
        # Reshape image so that the model can use it
        array = array.reshape((1,416,416,3))
        # Create prediction/analyze image
        pred = model.predict(array)
        # Return the class of the image
        pred = np.argmax(pred, axis = 1)

        # Confirm if a safety violation is occuring
        if pred == 1:
            st.write('All good, site safe')
        else:
            st.write('Safety Violation 29 CFR 1910.135: Hard hat not worn')
    else:
        pass

    # Ask for new image if Canceled
    if result_2:
        st.write('Please select upload another image')
    else: 
        result_2 = None

# If no image is uploaded request image
else:
    st.write('Please select a jpg or png file')

# Create dropdown menu of trades
result_3 = st.selectbox('Select Trade',trades)

# Select the trade responsible for safety infraction
if result_3 == 'Carpentry':
    # Create a dropdown for number of offenses to specify which report to load
    c_offense = st.selectbox('Select Offense',offense)
    if c_offense == '1st Offense':
        st.markdown(carp1_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(carp1_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif c_offense == '2nd Offense':
        st.markdown(carp2_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(carp2_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif c_offense == '3rd Offense':
        st.markdown(carp3_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(carp3_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)
        
# Select the trade responsible for safety infraction
elif result_3 == 'Electric':
    # Create a dropdown for number of offenses to specify which report to load
    e_offense = st.selectbox('Select Offense',offense)
    if e_offense == '1st Offense':
        st.markdown(elec1_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(elec1_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif e_offense == '2nd Offense':
        st.markdown(elec2_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(elec2_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif e_offense == '3rd Offense':
        st.markdown(elec3_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(elec3_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Select the trade responsible for safety infraction
elif result_3 == 'Mechanical/HVAC':
    # Create a dropdown for number of offenses to specify which report to load
    m_offense = st.selectbox('Select Offense',offense)
    if m_offense == '1st Offense':
        st.markdown(hvac1_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(hvac1_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif m_offense == '2nd Offense':
        st.markdown(hvac2_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(hvac2_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif m_offense == '3rd Offense':
        st.markdown(hvac3_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(hvac3_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Select the trade responsible for safety infraction
elif result_3 == 'Plumbing':
    # Create a dropdown for number of offenses to specify which report to load
    p_offense = st.selectbox('Select Offense',offense)
    if p_offense == '1st Offense':
        st.markdown(plumb1_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(plumb1_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

    elif p_offense == '2nd Offense':
        st.markdown(plumb2_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)
        b64 = base64.b64encode(plumb2_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    elif p_offense == '3rd Offense':
        st.markdown(plumb3_markdown, unsafe_allow_html=True)
        file = Image.open(fileUpload)
        st.image(file, width = 200, height = 200)

        b64 = base64.b64encode(plumb3_markdown.encode()).decode()
        href = f'<a href="data:file/md;base64,{b64}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

else:
    pass

























