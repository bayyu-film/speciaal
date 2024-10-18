# Fungsi untuk menghitung hasil dari 1 + 1 dan mengubahnya menjadi "I LOVE YOU"
def kalkulator():
    result = 1 + 1
    
    # Jika hasilnya adalah 2, cetak "I LOVE YOU"
    if result == 2:
        return "I LOVE YOU"
    else:
        return f"Hasilnya adalah {result}"

# Menampilkan hasil
print(kalkulator())