# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
st.title("Research Profile")
st.title("Oluchi Vivian Nkwachukwu")

st.write("Postdoctoral Research Fellow, University of Johannesburg, South Africa")
st.write("Contacts: oluviv2000@yahoo.com,  +27836385031")      
st.title("Research Interest")
st.write("Electrochemistry, Photo-electrochemistry, Electroanalytical Chemistry, Environmental Electrochemistry, Electrochemical Technologies for Water Treatment, Physical Chemistry, Nanoscience, Materials Chemistry, Green energy generation")

st.title("Education")
st.write("PhD, Physical/Electrochemistry, University of Johannesburg, South Africa	                   2023")
st.write("MSc, Polymer and Inorganic Chemistry, University of Johannesburg, South Africa               2019")
st.write("BSc (Honours) with second class upper at Abia State University, Nigeria 	                   2007")   
st.title("Work Experience") 
st.header("Postdoctoral Research Fellow, University of Johannesburg (UJ), South Africa")  
st.write("Preparation and characterisation of different semiconductors for photocatalysis, photoelectrocatalysis, and energy generation")
st.write("Designing research methodology and approach for MSc and PhD students") 	   

st.header("Oluchi Nkwachukwu Google Scholar Profile")
st.title("Oluchi Vivian Nkwachukwu Google Scholar Profile")

# st.write("Hello, Streamlit!")

# st.header("Oluchi Vivian Nkwachukwu Google Scholar Profile")

data = pd.DataFrame({"x": [2021, 2022, 2023, 2024,2025, 2026], "y": [10, 60, 120, 450, 550, 565]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x ="x", y="y", title="Google citation profile")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

# number = st.slider("Pick a number", 1, 100)

# st.write(f"You picked: {number}")
