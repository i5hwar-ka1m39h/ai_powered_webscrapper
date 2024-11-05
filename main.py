import streamlit as st
from scrapper import (site_scrapper, clean_html_content, clean_content, split_cleaned_content)
from parser import parseing_for_ollama


st.title("AI Web Scrapper")
url = st.text_input("Enter website url that you want to scrape")

if st.button("Scrape the site"):
    st.write("Scraping the website")
    result = site_scrapper(url)
    
    body_of_content = clean_html_content(result)
    cleaned_body_content = clean_content(body_of_content)

    st.session_state.dom_content = cleaned_body_content

    with st.expander("View the DOM content"):
        st.text_area("DOM content:",cleaned_body_content, height=300 )

if "dom_content" in st.session_state:
    parse_description = st.text_area("describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_cleaned_content(st.session_state.dom_content)
            result = parseing_for_ollama(dom_chunks, parse_description)
            st.write(result)