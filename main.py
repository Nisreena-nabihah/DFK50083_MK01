import logic

def main():
    while True:
        nama = input("Masukkan nama: ")
        nokp = input("Masukkan nombor kad pengenalan: ")

        sah, mesej_ralat = logic.sahkan_input(nama, nokp)
        if sah:
            break
        print(f"Ralat: {mesej_ralat}\n")

    nama_format = logic.dapatkan_nama_berformat(nama, nokp)
    info_umur = logic.kira_umur(nokp)

    print(f"{nama_format},")
    print(f"{info_umur}.")

if __name__ == "__main__":
    main()