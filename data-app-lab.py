import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

df = pd.read_csv('class_3\housing\housing.csv')

st.title("Jiao Ma")
st.title("California Housing Data (1990)")

# Multiselect for location type
location_types = df['ocean_proximity'].unique()
selected_locations = st.sidebar.multiselect('Choose the location type', location_types, default=location_types)

# Radio button for income level
income_level = st.sidebar.radio("Choose income level", ['Low', 'Medium', 'High'])
filtered_data = df[df['ocean_proximity'].isin(selected_locations)]

if income_level == 'Low':
    filtered_data = filtered_data[filtered_data['median_income'] <= 2.5]
elif income_level == 'Medium':
    filtered_data = filtered_data[(filtered_data['median_income'] > 2.5) & (filtered_data['median_income'] < 4.5)]
elif income_level == 'High (> 4.5)':
    filtered_data = filtered_data[filtered_data['median_income'] > 4.5]

# Create a price slider
max_price = int(df['median_house_value'].max())
price_slider = st.slider("Minimal Median House Value", 0, max_price, 200000)

# Filter data by price
filtered_data = filtered_data[filtered_data['median_house_value'] >= price_slider]

# show on map
st.subheader("See more filters in the sidebar")
st.map(filtered_data)   

# show the plot
fig, ax = plt.subplots(figsize=(15, 10))
ax.hist(filtered_data['median_house_value'], bins=30)
st.pyplot(fig)