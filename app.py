import wikipediaapi as wiki
import streamlit as st
import spacy


pagename = st.text_input("Enter The page Name")

nlp = spacy.load("en_core_web_sm")

if(st.button("Perform NER")):
    if(pagename != ""):
        data = nlp(getsummary(pagename))
        html =spacy.displacy.render(data,style="ent")
        st.write(html,unsafe_allow_html=True)



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





