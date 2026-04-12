import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Deteksi Fraud", layout="wide")

st.title("Dashboard Analisis Transaksi Kartu Kredit Kelompok 7")
st.write("Aplikasi ini menampilkan visualisasi data transaksi untuk mendeteksi potensi penipuan.")

# 1. Memuat Data
@st.cache_data
def load_data():
    # Pastikan file creditcard.csv ada di folder yang sama
    data = pd.read_csv('creditcard.csv')
    return data

df = load_data()

# 2. Sidebar untuk Navigasi
st.sidebar.header("Navigasi")
menu = st.sidebar.radio("Pilih Visualisasi:", ["Ringkasan Data", "Distribusi Kelas", "Analisis Amount"])

if menu == "Ringkasan Data":
    st.subheader("Informasi Dataset")
    st.write(f"Total Baris: {df.shape[0]}")
    st.write(f"Total Kolom: {df.shape[1]}")
    st.dataframe(df)

elif menu == "Distribusi Kelas":
    st.subheader("Visualisasi Imbalance Data (Target)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='Class', data=df, palette='viridis', ax=ax)
    plt.title('Distribusi Kelas (0: Normal, 1: Fraud)')
    st.pyplot(fig)
    
    st.info("Catatan: Terlihat perbedaan sangat jauh antara transaksi normal dan fraud (Imbalance).")

elif menu == "Analisis Amount":
    st.subheader("Distribusi Jumlah Transaksi (Amount)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Statistik Deskriptif Amount:")
        st.write(df['Amount'].describe())
        
    with col2:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.histplot(df['Amount'], bins=50, kde=True, color='blue', ax=ax2)
        plt.title('Penyebaran Nilai Transaksi')
        plt.xlim([0, 2000]) # Batasi agar lebih jelas terlihat
        st.pyplot(fig2)

# Bagian Footer/Samping
st.sidebar.markdown("---")
st.sidebar.write("Projek Informatika - Detektif Digital")