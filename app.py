import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/jacoblongthon/GDP-Data/main/GDP%20Data%20By%20Country%20CSV.csv")
    return data


def main():
    data = load_data()

    st.title('World GDP Data')

    pays = st.selectbox('Select a country', data['Country'].unique())

    donnees_pays = data[data['Country'] == pays]

    st.write(f"The GDP of {pays} is: {donnees_pays['Nominal'].iloc[0]}")
    st.write(f"The GDP per capita of {pays} is: {donnees_pays['Per capita '].iloc[0]}")
    st.write(f"The GDP growth of {pays} is: {donnees_pays['GDP Growth'].iloc[0]}")

if __name__ == "__main__":
    main()

