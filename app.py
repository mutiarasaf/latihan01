import streamlit as st

pages = [
    st.Page(page="Pages/page1.py", title="Home", icon="🏡"),
    st.Page(page="Pages/page2.py", title="Visualisasi Data", icon="📊"), 
    st.Page(Page(page="Pages/page3.py", title="Settings", icon="⚙️")
]

pg = st.navigation(
    Pages,
    positions="sidebar"
    expanded=True
)

pg.run()