import streamlit as st
from rag import process_urls,generate_answer
st.title("Neutrino: Scientific Knowledge Retrieval System")

url1=st.sidebar.text_input("URL1")
url2=st.sidebar.text_input("URL2")
url3=st.sidebar.text_input("URL3")

process_url_button=st.sidebar.button("Process URLs")

placeholder=st.empty()
if process_url_button:
    urls=[url for url in (url1,url2,url3) if url!='']
    if len(urls)==0:
        placeholder.text("No URLs found")
    else:
        process_urls(urls)
query=placeholder.text_input("Query: ")
if query:
    answer=generate_answer(query)
    st.header("Answer: ")
    st.write(answer)


