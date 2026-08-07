import datetime
import random
import time
import streamlit as st

# --- KODE WARNA / TAMPILAN ESTETIK ---
# Di Streamlit kita pakai Markdown untuk pewarnaan dan styling teks
PINK_COLOR = "#d63384"
RED_COLOR = "#dc3545"

# --- BAGIAN 1: SAPAAN & PESAN ACAK (DARI SCRIPT KEDUA) ---
st.title("🌟 KIODAPZ SAPA FANS 😹 🌟")

# 1. Tentukan ucapan berdasarkan jam (Waktu Indonesia)
jam = datetime.datetime.now().hour
if jam < 12:
  salam_waktu = "Sugeng enjing"
elif jam < 15:
  salam_waktu = "Sugeng Siang"
elif jam < 18:
  salam_waktu = "Sugeng Sonten"
else:
  salam_waktu = "Sugeng Dalu"

# 2. Pilihan pesan acak
daftar_pesan = [
    (
        "Hasil yang besar tidak pernah lahir dari keajaiban semalam, melainkan"
        " dari tumpukan usaha kecil yang konsisten setiap hari."
    ),
    (
        "Kegagalan terbesar bukan saat kamu kalah, tetapi pada saat kamu"
        " memutuskan untuk berhenti mencoba."
    ),
    (
        "Kamu tidak harus hebat untuk memulai, tetapi kamu harus memulai untuk"
        " menjadi hebat"
    ),
    (
        "Masa depanmu ditentukan oleh apa yang kamu lakukan hari ini, bukan apa"
        " yang kamu rencanakan hari ini"
    ),
    (
        "Jangan pernah meragukan potensimu hanya karena orang lain tidak bisa"
        " melihatnya, yang menjalani hidup ini adalah kamu bukan mereka."
    ),
    (
        "Pelaut yang tangguh tidak lahir dari laut yang tenang, nikmati"
        " prosesnya, karena kesulitan hari ini adalah pembentuk kekuatanmu"
        " esok hari."
    ),
    (
        "Satu satunya orang yang harus kamu kalahkan adalah dirimu yang"
        " kemarin, tetaplah melangkah di jalurmu sendiri."
    ),
    (
        "Rasa lelah karena belajar dan bekerja keras itu sementara, tapi rasa"
        " penyesalan karena menyia nyiakan waktu bisa bertahan selamanya."
    ),
    (
        "Ketika kamu merasa ingin menyerah, ingat kembali alasan mengapa kamu"
        " memulainya sejak awal."
    ),
    (
        "Jangan lupa berterima kasih pada dirimu sendiri, Kamu sudah bertahan"
        " sejauh ini, dan kamu lebih kuat dari yang kamu bayangkan."
    ),
    "Hadapi segala rintangannya capai tujuanmu dengan penuh rasa hormat",
    "Semoga semua urusanmu dilancarkan hari ini ya.",
    "Kamu hebat sudah berjuang sejauh ini, semangat terus!",
    "Jangan lupa istirahat yang cukup kalau sudah lelah.",
]
pesan_acak = random.choice(daftar_pesan)

# Form Input Nama Pengunjung
nama_input = st.text_input(
    "Masukkan nama Anda:", placeholder="Ketik nama di sini..."
).strip()

if nama_input:
  # Bentuk Hati Presisi (Ditampilkan dalam code block atau markdown agar rapi)
  gambar_hati = """
	 ***   ***
	***** *****
   *************
	***********
	 *********
	   *****
	     *
	"""
  st.markdown(
      f"<pre style='color: {RED_COLOR}; text-align: center; font-weight:"
      f" bold;'>{gambar_hati}</pre>",
      unsafe_allow_html=True,
  )

  # Sapaan Interaktif
  st.markdown(
      f"<h3 style='color: {PINK_COLOR}; text-align: center;'>Hiiii, {nama_input}!"
      f" 💖</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<h4 style='color: {RED_COLOR}; text-align: center;'>{salam_waktu},"
      f" {nama_input}!</h4>",
      unsafe_allow_html=True,
  )
  st.markdown("---")

  # Pesan Inspiratif
  st.info(f"**PESAN UNTUKMU:** {pesanicak if 'pesanicak' in locals() else pesan_acak}")

  st.write("\n")
  st.subheader("   ◌⑅⃝ᵐᶦˢˢ♡ KUALIFIKASI NILAI KIOUDAPZ ♡ʸᵒᵘ⑅⃝◌")
  st.write("Silakan masukkan nilaimu di bawah ini:")

  # --- BAGIAN 2: KUALIFIKASI NILAI (DARI SCRIPT PERTAMA) ---
  # Mengganti input() terminal dengan st.number_input / st.text_input
  input_nilai = st.number_input(
      "Lebokkan nilai (0 - 100):",
      min_value=0.0,
      max_value=100.0,
      step=1.0,
      value=0.0,
  )

  if st.button("Proses Kualifikasi Nilai"):
    nilai = float(input_nilai)

    # 1. Kualifikasi Nilai
    if 80 <= nilai <= 100:
      kualifikasi = "SANGAT BAGUSS👍🤩👍"
    elif 70 <= nilai < 80:
      kualifikasi = "BAGUSS😁👍"
    elif 60 <= nilai < 70:
      kualifikasi = "LUMAYAN BAGUSS😊👌"
    elif 45 <= nilai < 60:
      kualifikasi = "KURANG BAGUSS🙂🤏"
    else:  # 0 <= nilai < 45
      kualifikasi = "PERLU BELAJAR LAGI😌✊"

    # Tampilkan Hasil
    st.success(f"Hasil Kualifikasi: **{kualifikasi}**")

    # Opsi Cetak Nilai
    cetak = st.checkbox("Cetak / Tampilkan Kartu Nilai")
    if cetak:
      st.markdown("---")
      st.markdown("### 📜 KARTU NILAI")
      st.write(f"**NAMA**        : {nama_input}")
      st.write(f"**NILAI**       : {nilai}")
      st.write(f"**KUALIFIKASI** : {kualifikasi}")
      st.markdown("---")

  # Penutup Program Sederhana
  st.write("\n")
  st.markdown(
      "<h4 style='text-align: center; color: gray;'>MATURNUWUNNN 🙏</h4>",
      unsafe_allow_html=True,
  )
else:
  st.warning("👈 Masukkan nama Anda di atas untuk memulai program!")