import wikipediaapi
import streamlit as st
import spacy

st.set_page_config(layout='wide')

st.title("Named Entity Recognition")
pagename = st.text_input("Enter The page Name")

nlp = spacy.load("en_core_web_sm")



def getsummary(pageName):
    if(pageName ==""):
        return ""
    
    wikipedia = wikipediaapi.Wikipedia('en')
    page = wikipedia.page(pageName)
    if(page.exists()):
        print("Getting data from wikipedia page\nLink :: ",page.fullurl,"\n\n\n")
        return page.text
    else:
        print("Page doesnot exists");




if(st.button("Perform NER")):
    if(pagename != ""):
        data = nlp(getsummary(pagename))
        html =spacy.displacy.render(data,style="ent")
        st.write(html,unsafe_allow_html=True)

