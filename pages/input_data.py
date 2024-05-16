import streamlit as st
from pages.data import *
import pandas as pd
import time

st.set_page_config(
    page_title="GeoGenix",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)




st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.write("# 🌍 Wenner Digital Datasheet")
st.write("## Profile Metadata")
st.write("Profile Name: `",SurveyName,"`")
st.write("Longitude: ",Longitude,"    Lattitude: ",Lattitude,"Elevation :",Elevation)
st.write("### Electrode Position")
col4, col5, col6, col7 = st.columns(4)

with col4:
    st.write("C1: ",c1) 
    
with col5:
    st.write("P1: ",p1) 
    
with col6:
    st.write("P2: ",p2)
with col7:
    st.write("C2: ",c2) 

st.divider()
resistance = st.number_input("Resistance",key='rrd3',format="%.4f")
def clear_all_text_inputs():
    if resistance!=0:
        with st.spinner('Wait for it...'):
            add_data(resistance)
            time.sleep(1)
    else:
        st.error('Invalid Data Format', icon="🚨")

    
    st.session_state['rrd3'] = 0  # Clear inphase text input

st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    insert_button = st.button("Add Dataset", type='primary', key='insert_button', on_click=clear_all_text_inputs)
with col2:
    if (st.button("Datasheet View")):
        st.switch_page("pages/export_data.py")


