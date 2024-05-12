
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
  
"""
)
def switching():
    st.balloons()

st.subheader("Resistivity [Wenner Array] Survey↭")
SurveyName = st.text_input("Interval Name")
Longitude = st.number_input(label= "Longitude ", placeholder="Degree Decimal",format="%.4f")
Lattitude=st.number_input("Lattitude", placeholder="Degree Decimal",format="%.4f")
Elevation=st.number_input("Elevation", placeholder="Metres",format="%.4f")
Interval_Spacing=st.number_input("Spacing Interval(a)",min_value=1)
if(st.button("Proceed",type='primary')):
    md.SurveyName=SurveyName
    md.Longitude=Longitude
    md.Lattitude=Lattitude
    md.Intervals=Interval_Spacing
    md.Elevation=Elevation
    md.dataset={"C1":[],"P1":[],"C2":[],"P2":[],"Resistance":[],"K Factor":[],"Resistivity":[],"Lattitude":[],"Longitude":[]}
    md.Station=0
    md.c1=0
    md.p1=md.Intervals
    md.p2= md.p1 + md.Intervals
    md.c2= md.p2 + md.Intervals
    md.config()
    st.switch_page("pages/input_data.py")

    





