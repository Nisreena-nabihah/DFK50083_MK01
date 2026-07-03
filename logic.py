from datetime import datetime

def sahkan_input(nama, nokp):
    # 1. Nama tak boleh kosong
    if not nama.strip():
        return False, "Nama tidak boleh kosong."

    # 2. No. KP mesti 12 digit angka
    if len(nokp) != 12 or not nokp.isdigit():
        return False, "Nombor kad pengenalan mestilah 12 digit angka."

    # 3. 6 digit pertama mesti tarikh sah (YYMMDD)
    try:
        datetime.strptime(nokp[:6], "%y%m%d")
    except ValueError:
        return False, "6 digit pertama No. KP mestilah tarikh yang sah (YYMMDD)."

    return True, ""


def dapatkan_nama_berformat(nama, nokp):
    # Tentukan gelaran ikut digit terakhir KP
    last_digit = int(nokp[-1])
    if last_digit % 2 == 1:   # ganjil = lelaki
        gelaran = "Encik"
    else:                     # genap = perempuan
        gelaran = "Cik"
    return f"{gelaran} {nama}"


def kira_umur(nokp):
    # Ambil YYMM dari KP
    yy = int(nokp[0:2])
    mm = int(nokp[2:4])

    today = datetime.now()
    current_year = today.year
    current_month = today.month

    # Tentukan abad (1900-an atau 2000-an)
    if yy <= int(str(current_year)[2:]):  # contoh: 26
        birth_year = 2000 + yy
    else:
        birth_year = 1900 + yy

    birth_month = mm

    # Kira beza bulan
    total_months_now = current_year * 12 + current_month
    total_months_birth = birth_year * 12 + birth_month
    diff_months = total_months_now - total_months_birth

    years = diff_months // 12
    months = diff_months % 12

    return f"Anda berumur {years} tahun {months} bulan"