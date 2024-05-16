import streamlit as st
import pages.data as pg
import pandas as pd

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
st.write("# 🌍 GeoGenix")
st.write("## Profile Metadata")
st.write("Name: ",pg.SurveyName)
st.write("Longitude: ",pg.Longitude,"    Lattitude: ",pg.Lattitude,"Elevation :",pg.Elevation)


st.divider()
def update():
    pass
st.write("## Export Data")
df = pd.DataFrame(pg.dataset)
edited_df = st.data_editor(df,on_change=update)
pg.dataset =edited_df.to_dict(orient='list')
#st.write(pg.dataset)
#st.write(df)
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
    if (st.button("Form View")):
        st.switch_page("pages/input_data.py")
with col2:
    if (st.button("New Profile",type="primary")):
        st.switch_page("app.py")
