import streamlit as st
import pages.data as md;
st.set_page_config(
    page_title="Wenner Array Digital Datasheet",
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

st.write("# 🌍 GeoElectrical Resistivity!")
st.write("  ### Wenner Array Configuration Digital Datasheet")

def switching():
    st.balloons()

st.subheader("New Profile")
SurveyName = st.text_input("Profile Name",placeholder="Traverse One")
Longitude = st.number_input(label= "Longitude (Degree Decimal) ", placeholder="Degree Decimal",format="%.4f")
Lattitude=st.number_input("Lattitude (Degree Decimal) ", placeholder="Degree Decimal",format="%.4f")
Elevation=st.number_input("Elevation", placeholder="Metres",format="%.4f")
Interval_Spacing=st.number_input("Spacing",placeholder="Metres",format="%.2f",min_value=1.0)
if(st.button("Proceed",type='primary')):
    if isinstance(Interval_Spacing, float): 
        md.SurveyName=SurveyName
        md.Longitude=Longitude
        md.Lattitude=Lattitude
        md.Intervals=Interval_Spacing
        md.Elevation=Elevation
        md.dataset={"C1":[],"P1":[],"C2":[],"P2":[],"Resistance":[],"K Factor":[],"Resistivity":[]}
        md.Station=0
        md.c1=0
        md.p1=md.Intervals
        md.p2= md.p1 + md.Intervals
        md.c2= md.p2 + md.Intervals
        md.config()
        st.switch_page("pages/input_data.py")
    else:
    	st.error('Invalid Format For Spacing', icon="🚨")
    
