import streamlit as st
import pandas as pd
from cocijo.plot_series import plot_yearly_rain, plot_cumulative_yearly_rain

st.title("Lluvia Diaria")
raw_data = pd.read_csv("data/registro_lluvias.csv")
st.subheader("Lluvia Anual")
st.pyplot(plot_yearly_rain(raw_data).figure)
st.subheader("Lluvia Acumulada")
st.pyplot(plot_cumulative_yearly_rain(raw_data).figure)
