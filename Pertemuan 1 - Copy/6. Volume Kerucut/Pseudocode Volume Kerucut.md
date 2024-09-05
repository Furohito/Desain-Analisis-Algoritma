PROSEDUR hitung_volume_kerucut
    variabel diameter, tinggi, jari-jari, volume : real
    konstanta pi = 3.14159
    
    # Inisialisasi nilai
    diameter ← 5
    tinggi ← 4
    
    # Hitung jari-jari
    jari-jari ← diameter / 2
    
    # Hitung volume kerucut
    volume ← (1/3) * pi * jari-jari^2 * tinggi
    
    # Tampilkan hasil
    tulis("Volume kerucut adalah", volume)
AKHIR PROSEDUR
