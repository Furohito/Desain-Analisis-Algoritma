PROSEDUR hitung_volume_tabung
    variabel jari-jari, tinggi, volume : real
    konstanta pi = 3.14159
    
    # Inisialisasi nilai
    jari-jari ← 3
    tinggi ← 5
    
    # Hitung volume tabung
    volume ← pi * jari-jari^2 * tinggi
    
    # Tampilkan hasil
    tulis("Volume tabung adalah", volume)
AKHIR PROSEDUR
