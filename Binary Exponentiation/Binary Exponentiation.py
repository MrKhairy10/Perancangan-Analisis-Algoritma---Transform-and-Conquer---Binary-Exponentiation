# Fungsi binary exponentiation
def binary_exponentiation(base, exponent, modulus=None):
    """
    Fungsi untuk menghitung bilangan pangkat dengan algoritma binary exponentiation.

    Args:
        base (int): bilangan yang akan dipangkatkan
        exponent (int): pangkat dari bilangan
        modulus (int, optional): bilangan modulus untuk operasi modulo. Defaults to None.

    Returns:
        int: hasil pangkat bilangan
    """
    # Inisialisasi nilai result dengan 1
    result = 1

    # Jika modulus tidak diberikan, maka diambil modulo dengan 1
    base %= modulus if modulus else 1

    # Perulangan selama nilai exponent masih lebih besar dari 0
    while exponent > 0:
        # Jika exponent ganjil, maka result dikalikan dengan base
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus else result * base

        # Base dikuadratkan
        base = (base * base) % modulus if modulus else base * base

        # Exponent dibagi dua
        exponent //= 2

    # Hasil akhir diambil modulo dengan modulus jika modulus diberikan, atau tidak diambil modulo jika tidak ada modulus
    return result % modulus if modulus else result


# Contoh penggunaan program
if __name__ == '__main__':
    # Memasukkan bilangan yang akan dipangkatkan dan pangkatnya
    base = 237
    exponent = 919

    # Memasukkan bilangan modulus jika diperlukan
    modulus = 1057

    # Menghitung hasil pangkat dengan menggunakan binary exponentiation
    result = binary_exponentiation(base, exponent, modulus)

    # Menampilkan hasil pangkat
    print(f"Hasil dari {base}^{exponent} mod {modulus} adalah {result}")
