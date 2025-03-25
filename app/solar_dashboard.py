import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from datetime import datetime

# Load the three datasets
files = {
    "Benin-Malanville": r'C:\Users\Eyor.G\Pictures\Projects\solar-site-optimizer\data\benin-malanville.csv',
    "SierraLeone-Bumbuna": r'C:\Users\Eyor.G\Pictures\Projects\solar-site-optimizer\data\sierraleone-bumbuna.csv',
    "Togo-Dapaong": r'C:\Users\Eyor.G\Pictures\Projects\solar-site-optimizer\data\togo-dapaong_qc.csv'
}

datasets = {name: pd.read_csv(file, parse_dates=['Timestamp']) for name, file in files.items()}

# Define geospatial coordinates for map visualization
location_coords = {
    "Benin-Malanville": [11.868, 3.383],
    "SierraLeone-Bumbuna": [9.057, -11.746],
    "Togo-Dapaong": [10.862, 0.205]
}

# Streamlit UI
st.title('Solar Site Analysis Dashboard - MoonLight Energy Solutions')
st.sidebar.header('Options')

# Location Selection
location = st.sidebar.selectbox('Select Location', list(datasets.keys()))
df = datasets[location]

# Data Filter
start_date = st.sidebar.date_input('Start Date', df['Timestamp'].min().date())
end_date = st.sidebar.date_input('End Date', df['Timestamp'].max().date())

# Convert to Timestamp for correct filtering
df_filtered = df[(df['Timestamp'] >= pd.Timestamp(start_date)) & (df['Timestamp'] <= pd.Timestamp(end_date))]

# KPI Metrics
avg_ghi = df_filtered['GHI'].mean()
max_dni = df_filtered['DNI'].max()

# Fixing `cleaning_effect` calculation to avoid errors
if df_filtered['Cleaning'].nunique() > 1:
    cleaning_effect = df_filtered.groupby('Cleaning')['ModA'].mean().diff().dropna().iloc[-1]
else:
    cleaning_effect = 0  # Default to 0 if there's no variation

col1, col2, col3 = st.columns(3)
col1.metric("Average GHI (W/m²)", f"{avg_ghi:.2f}")
col2.metric("Max DNI (W/m²)", f"{max_dni:.2f}")
col3.metric("Cleaning Impact (ModA)", f"{cleaning_effect:.2f}")

# Time-series plots
fig = px.line(df_filtered, x='Timestamp', y=['GHI', 'DNI', 'DHI'], title=f"Solar Irradiance Trends in {location}")
st.plotly_chart(fig)

# Map Visualization
st.subheader('Geospatial View')
m = folium.Map(location=location_coords[location], zoom_start=6)
folium.Marker(location=location_coords[location], popup=f'{location}').add_to(m)
st_folium(m, width=700, height=500)

# Data Preview
st.write('### Data Preview')
st.dataframe(df_filtered.head())
