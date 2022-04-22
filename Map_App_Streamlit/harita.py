import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

unesco1 = Path(__file__).parents[1] / 'Map_App_Streamlit/unesco.csv'
unesco=pd.read(unesco1)

ulkelist = []
ulkeler = unesco["Country name"].unique()
for i in ulkeler:
    ilist = i.split(",")
    for x in ilist:
        if x not in ulkelist:
          ulkelist.append(x)

ulkelist.insert(0,"Tüm Ülkeler")

ulkesec=st.sidebar.selectbox("Ülke seçiniz",ulkelist)

mirassec=st.sidebar.text_input("Miras ismi giriniz")

ulkedf = unesco[unesco["Country name"].str.contains(ulkesec)]

mirasdf=unesco[unesco["Name"].str.contains(mirassec)]

konumlar = ulkedf[["longitude","latitude"]]

if len(mirassec)>3:
     st.map(mirasdf[["longitude", "latitude"]])
     df=mirasdf
elif ulkesec == "Tüm Ülkeler":
     st.map(unesco[["longitude", "latitude"]])
     df = unesco
else:
     st.map(konumlar)
     df = ulkedf

# streamlit reference sayfasından download'a baktık
csv=df.to_csv().encode('utf-8')

st.sidebar.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='Data_Frame.csv',
     mime='text/csv',
 )

st.dataframe(df)

# share.streamlit ile url linki olarak paylaşabiliriz
