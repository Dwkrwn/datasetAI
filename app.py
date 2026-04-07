import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle # Jika Anda ingin memuat model yang sudah disimpan

# --- 1. PEMBACAAN DATA ---
# Pastikan file csv berada di folder yang sama dengan file .py ini
@st.cache_data # Gunakan ini agar data tidak dibaca berulang-ulang (performa lebih cepat)
def load_data():
    data = pd.read_csv('creditcard.csv')
    # Tambahkan preprocessing singkat jika perlu (seperti di notebook Anda)
    return data

df = load_data() # SEKARANG VARIABEL 'df' SUDAH TERDEFINISI

# --- 2. TAMPILAN WEB STREAMLIT ---
st.title("Sistem Deteksi Fraud")

if st.checkbox("Tampilkan Dataset"):
    st.write(df.head())

# --- 3. VISUALISASI ---
st.subheader("Visualisasi Data")
fig, ax = plt.subplots()
sns.countplot(x='Class', data=df, ax=ax) # 'df' sudah bisa dibaca di sini
st.pyplot(fig)