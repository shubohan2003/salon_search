#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st

df = pd.read_csv("cleaned_salon_data.csv")



# In[3]:


selected_salon = st.selectbox('サロンを選んで詳細を確認', df['name'])

if selected_salon:
    url = df[df['name'] == selected_salon]['link'].values[0]
    st.markdown(f"[{selected_salon}のページへ移動]({url})", unsafe_allow_html=True)


# In[ ]:


st.subheader("座席数によるランキング（上位10件）")

ranking_df = df.sort_values(by="seats", ascending=False).head(10)

st.dataframe(ranking_df[["name", "seats", "price", "review", "access"]])

