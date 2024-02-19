# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(
    page_title="Patent Search App",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title('Patent Search App')
st.sidebar.title('Instructions')
st.sidebar.markdown('Enter a query and click the "Search" button to find relevant patents.')

query = st.text_input('Enter your query:')
if st.button('Search'):
    response = requests.get(f'http://127.0.0.1:5000/search?query={query}')

    results = response.json()

    st.subheader('Search Results:')
    for result in results:
        # st.write(f"**Patent Number:** {result[0]}, **Title:** {result[1]}, **Similarity:** {result[2]:.4f}")
        st.write(f"**Patent Number:** {result[0]}, **Title:** {result[1]}")
        st.markdown("---")
