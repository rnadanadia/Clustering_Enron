import webbrowser
import pandas as pd
import streamlit as st

@st.cache
def load_dfs_in_cache():
    # read vals from csv
    df = pd.read_csv("./data/emails_lemmatized_clustered.csv", sep=";")
    df = df.rename(columns={"label": "cluster"})
    df = df.dropna()
    return df

df = load_dfs_in_cache()

def runapp():
    keyword = st.sidebar.text_input("enter keyword:")
    label = st.sidebar.text_input("refine by cluster number (optional):")
    if st.sidebar.button("search"):
        wordlist = df[df["words"].str.contains(keyword)].sort_values(by="cluster")
        if label:
            wordlist = wordlist[wordlist["cluster"] == int(label)]
        wordlist = wordlist.drop('words', axis=1)
        wordlist = wordlist.rename(columns={"body": "email body"})
        st.dataframe(wordlist, width=1000, height=400)
    if st.sidebar.button('Open Keyword analysis'):
        url = "/home/becode2/Desktop/Clustering_Enron/assets/lda.html"
        webbrowser.open_new_tab(url)

runapp()
