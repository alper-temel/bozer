import pandas as pd
import numpy as np
import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

st.markdown("# :violet[SATIŞ KANALLARI BİRLEŞTİRME] 	chart_with_upwards_trend: :alien: money_with_wings")

bozer = st.file_uploader("**Dosya Yükleyin** ", type = ["xls", "xlsx", "csv"])
if bozer is not None:
     st.dataframe(pd.read_excel(bozer))
else:
    st.caption("Lütfen Excel Dosyasını Kontrol Edin")

def burc():
    if bozer is not None:
         bozer.seek(0)
         bozer_1 = pd.read_excel(bozer, header = 5, sheet_name = "E-Ticaret")
         bozer_2 = pd.read_excel(bozer, header = 5, sheet_name = "Tele-Satış")
         bozer_3 = pd.read_excel(bozer, header = 5, sheet_name = "Geleneksel")

         bozer_1["Satış Kanalı"] = "E-Ticaret"
         bozer_2["Satış Kanalı"] = "Tele-Satış"
         bozer_2["Satış Kanalı"] = "Geleneksel"

         data = pd.concat([bozer_1, bozer_2, bozer_3], axis = 0)
         data = data.dropna()
    return data

if bozer is not None:
    df = burc()

    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0.00'}) 
        worksheet.set_column('A:A', None, format1)  
        writer.close()
        processed_data = output.getvalue()
        return processed_data

    df_xlsx = to_excel(df)
    st.download_button(label='📥 Dosyayı İndir',
                       data=df_xlsx,
                       file_name= 'Bozer_TSB.xlsx')

else:
    st.download_button(label = '📥 Dosyayı İndir', data = ' ')

st.markdown("Akılda Kalan v1.0 ~ CAT :robot_face: 2025")
