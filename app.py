
import streamlit as st
import pages.data as md;

st.set_page_config(
    page_title="GeoGenix Digital Datasheet",
    page_icon="👋",
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

st.write("# Welcome To GeoGenix ! 👋")
st.write("  ### Electrical Resistivity(Wenner Configuration) Survey Digital Datasheet")

st.markdown(
    """
   Welcome to Geogenix, your go-to resource for geophysical exploration and insights. 
   Our mission is to bridge the gap between theory and practice, providing geoscientists, 
   researchers, and enthusiasts with valuable information and tools. 
    ### Want  more tools?
    - Check out [GeoGenix HomePage](https://geogenix.000webhostapp.com/)
    ### How To Use
    - Click On `New Survey Profile`
    - Fill In The Form With Accurate Data
    - Click On `Proceed` To Enter Form View 
    - In The Form View Electrode Configuration/Spacing/Position Will Be Shown
    - Enter Resistance Value And Click On `Add Dataset` To Datapoint
    - When You Are Done Recording All Your Datapoints Click On `DataSheet View` Button To View All Your Data
    - You Can Search, Edit And Download Your Data As A CSV File
"""
)
if (st.button("New Survey Profile",type='primary')):
        st.switch_page("pages/setup.py")





