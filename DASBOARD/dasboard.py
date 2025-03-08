import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data dari GitHub
URL = "https://raw.githubusercontent.com/DcCode46/submission/main/dashboard/all_data.csv"
@st.cache_data
def load_data():
    return pd.read_csv(URL)

df = load_data()

# Tampilkan beberapa data awal untuk memastikan data ter-load
st.write("Data awal:", df.head())

# Title
st.title("Dashboard Analisis Penggunaan Sepeda 🚴")

# --- Visualisasi 1: Pola Penggunaan Sepeda Sepanjang Hari ---
st.subheader("Pola Penggunaan Sepeda Sepanjang Hari")
hourly_trend = df.groupby('hr').agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': 'mean'
}).reset_index()

# Membuat plot
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y='casual', data=hourly_trend, label='Casual', marker='o', ax=ax)
sns.lineplot(x='hr', y='registered', data=hourly_trend, label='Registered', marker='o', ax=ax)
sns.lineplot(x='hr', y='cnt', data=hourly_trend, label='Total', marker='o', ax=ax)

# Menambahkan judul dan label
ax.set_title('Pola Penggunaan Sepeda Sepanjang Hari', fontsize=14)
ax.set_xlabel('Jam dalam Sehari', fontsize=12)
ax.set_ylabel('Jumlah Pengguna', fontsize=12)
ax.set_xticks(range(0, 24))  # Menampilkan semua jam (0-23)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

# Menampilkan plot di Streamlit
st.pyplot(fig)

# ---kesimpulan---
st.subheader("Kesimpulan")
st.write("""
Dari visualisasi, terlihat bahwa:
- **Penggunaan sepeda meningkat signifikan pada jam pagi (07:00 - 09:00) dan sore (17:00 - 19:00)**, yang kemungkinan besar berkaitan dengan jam berangkat dan pulang kerja/sekolah.
- **Penggunaan sepeda paling rendah terjadi pada dini hari (00:00 - 05:00)**, yang dapat disebabkan oleh kondisi gelap dan aktivitas masyarakat yang minim pada waktu tersebut.
""")

# --- Visualisasi 2: Pengaruh Musim terhadap Penggunaan Sepeda ---
st.subheader("Pengaruh Musim terhadap Penggunaan Sepeda")
season_trend = df.groupby('season').agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': 'mean'
}).reset_index()

# Mapping label musim
season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_trend['season'] = season_trend['season'].map(season_labels)

# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_trend, palette='coolwarm', ax=ax)

# Menambahkan label dan judul
ax.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda', fontsize=14)
ax.set_xlabel('Musim', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Menampilkan plot di Streamlit
st.pyplot(fig)

# --- Kesimpulan ---
st.subheader("Kesimpulan")
st.write("""
Dari visualisasi, terlihat bahwa:
- **Jumlah peminjaman sepeda tertinggi** terjadi pada musim gugur (**Fall**), diikuti oleh musim panas (**Summer**).
- **Peminjaman sepeda paling rendah** terjadi pada musim semi (**Spring**) dan musim dingin (**Winter**).
- Hal ini kemungkinan karena kondisi cuaca yang kurang mendukung, seperti hujan atau suhu dingin yang ekstrem.
""")
