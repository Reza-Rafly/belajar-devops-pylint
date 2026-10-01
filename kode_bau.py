"""Modul contoh yang sudah diperbaiki sesuai PEP 8."""


def jumlahkan(a, b, c, d, e, f):
    """Menjumlahkan enam nilai."""
    total = a + b + c + d + e + f
    return total


def main():
    """Fungsi utama."""
    hasil = jumlahkan(1, 2, 3, 4, 5, 6)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
