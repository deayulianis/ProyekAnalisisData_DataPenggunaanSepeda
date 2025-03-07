import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Data Loading ---
@st.cache
def load_data():
    # Menggunakan path yang sudah Anda tentukan untuk file CSV
    hour_df = pd.read_csv(r"https://raw.githubusercontent.com/deayulianis/submission-DBS-1-/refs/heads/main/Bike-sharing-dataset/hour.csv")
    day_df = pd.read_csv(r"https://raw.githubusercontent.com/deayulianis/submission-DBS-1-/refs/heads/main/Bike-sharing-dataset/day.csv")
    return hour_df, day_df

# --- Data Preparation ---
hour_df, day_df = load_data()

# --- Data Cleaning & Transformation ---
# Mengubah nilai 'season' dan 'weathersit' menjadi nama musim dan cuaca yang lebih mudah dipahami
hour_df['season'] = hour_df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
hour_df['weathersit'] = hour_df['weathersit'].replace({1: 'Clear', 2: 'Cloudy', 3: 'Rainy', 4: 'Stormy'})

# --- Display Raw Data ---
st.title("Bike Sharing Dashboard")

st.write("### Hour Data Sample:")
st.write(hour_df.head())

# --- Exploratory Data Analysis (EDA) ---

# 1. Pola penggunaan sepeda berdasarkan musim dan cuaca
st.write("### Pola Penggunaan Sepeda Berdasarkan Musim dan Cuaca")

fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='season', hue='weathersit', data=hour_df, palette='Set1', ax=ax)
ax.set_title('Penggunaan Sepeda Berdasarkan Musim dan Cuaca')
st.pyplot(fig)

# 2. Pola penggunaan sepeda berdasarkan jam dan cuaca
st.write("### Pola Penggunaan Sepeda Berdasarkan Jam dan Cuaca")

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.countplot(x='hr', hue='weathersit', data=hour_df, palette='Set2', ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Jam dan Cuaca')
st.pyplot(fig2)

# --- Insights ---
st.write("### Insight dari Data:")
st.write("""
1. **Pola Penggunaan Sepeda Berdasarkan Musim dan Cuaca**: 
   - Penggunaan sepeda lebih tinggi di musim panas dan musim gugur (Summer & Fall).
   - Cuaca cerah lebih sering dikaitkan dengan penggunaan sepeda yang lebih tinggi dibandingkan dengan cuaca mendung atau hujan.
   
2. **Pola Penggunaan Sepeda Berdasarkan Jam dan Cuaca**:
   - Penggunaan sepeda lebih tinggi pada jam-jam sibuk, seperti jam 7-9 pagi dan 5-7 sore.
   - Cuaca cerah cenderung meningkatkan penggunaan sepeda pada jam-jam sibuk.
""")

# --- Maximizing Bike Availability During Peak Times ---
st.write("### Memaksimalkan Jumlah Sepeda yang Tersedia pada Waktu-Waktu Sibuk")

# Data analisis untuk waktu sibuk berdasarkan jam
hourly_usage = hour_df.groupby('hr').agg({'cnt': 'sum'}).reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_usage, marker='o', ax=ax3)
ax3.set_title('Jumlah Sepeda yang Tersedia Berdasarkan Jam')
st.pyplot(fig3)

# --- Displaying Dashboard Complete ---
st.write("### Dashboard Lengkap Selesai.")
