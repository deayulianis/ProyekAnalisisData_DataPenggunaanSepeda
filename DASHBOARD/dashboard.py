import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_df = pd.read_csv("https://raw.githubusercontent.com/deayulianis/submission-DBS-1-/refs/heads/main/Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/deayulianis/submission-DBS-1-/refs/heads/main/Bike-sharing-dataset/hour.csv")

# Convert date column
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Dashboard Title
st.title("📊 Dashboard Analisis Peminjaman Sepeda 🚲")

# ========================== DATA AWAL ==========================
st.subheader("📂 Data Awal")

st.write("### Data Harian (day.csv)")
st.dataframe(day_df.head())

st.write("### Data Per Jam (hour.csv)")
st.dataframe(hour_df.head())

# ========================== INTERAKTIF: FILTER RENTANG WAKTU ==========================
st.subheader("⏳ Analisis Pola Peminjaman Berdasarkan Jam")
selected_hours = st.slider("Pilih Rentang Jam", 0, 23, (6, 18))

filtered_hourly = hour_df[(hour_df['hr'] >= selected_hours[0]) & (hour_df['hr'] <= selected_hours[1])]
hourly_trend = filtered_hourly.groupby('hr').agg({'casual': 'mean', 'registered': 'mean', 'cnt': 'mean'}).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hr', y='casual', data=hourly_trend, label='Casual', marker='o')
sns.lineplot(x='hr', y='registered', data=hourly_trend, label='Registered', marker='o')
sns.lineplot(x='hr', y='cnt', data=hourly_trend, label='Total', marker='o')
ax.set_title("Pola Penggunaan Sepeda Sepanjang Hari")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Pengguna")
ax.set_xticks(range(0, 24))
ax.grid(True, linestyle="--", alpha=0.5)
st.pyplot(fig)

# Kesimpulan dari visualisasi
st.markdown(
    """
    **🔍 Kesimpulan:**
    - Peminjaman sepeda meningkat pada pagi hari (**07:00 - 09:00**) dan sore hari (**17:00 - 19:00**).
    - Hal ini menunjukkan bahwa peminjaman sepeda **berkorelasi dengan jam kerja**, di mana banyak orang menggunakan sepeda sebagai moda transportasi.
    - Pengguna **casual** lebih banyak meminjam pada siang hari, sedangkan pengguna **terdaftar** cenderung meminjam saat jam sibuk kerja.
    """
)

# ========================== INTERAKTIF: MUSIM ==========================
st.subheader("🌦️ Pengaruh Musim terhadap Peminjaman Sepeda")

season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df['season_label'] = day_df['season'].map(season_labels)

selected_seasons = {}
for season in season_labels.values():
    selected_seasons[season] = st.checkbox(f"Tampilkan {season}", value=True)

filtered_season = day_df[day_df['season_label'].isin([s for s, v in selected_seasons.items() if v])]

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season_label', y='cnt', data=filtered_season, palette="coolwarm", estimator=lambda x: sum(x) / len(x))
ax.set_title("Pengaruh Musim terhadap Jumlah Peminjaman Sepeda")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
ax.grid(axis='y', linestyle='--', alpha=0.5)
st.pyplot(fig)


# Kesimpulan dari visualisasi
st.markdown(
    """
    **🔍 Kesimpulan:**
    - **Musim gugur (Fall) memiliki jumlah peminjaman tertinggi**, kemungkinan karena cuaca lebih nyaman untuk bersepeda.
    - **Musim semi (Spring) memiliki jumlah peminjaman terendah**, kemungkinan karena curah hujan yang lebih tinggi.
    - Perubahan musim memengaruhi jumlah peminjaman, dengan tren yang lebih tinggi saat cuaca lebih baik.
    """
)

st.write("Dashboard dibuat menggunakan Streamlit 🚀")
