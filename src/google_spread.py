from datetime import datetime
from typing import Dict

from gspread.models import Worksheet


def next_available_row(sheet: Worksheet) -> int:
    return len(sheet.col_values(1)) + 1


def update_google_spread(sheet: Worksheet, data: Dict[str, str]) -> None:
    row_num: int = next_available_row(sheet)
    row = f"A{row_num}:O{row_num}"
    semua_nama_kolom = [
        "agency",
        "id partner",
        "track id",
        "nama pelanggan",
        "alamat lengkap",
        "cp utama",
        "cp alternatif",
        "id pln",
        "email",
        "odp rekomendasi",
        "tag odp",
        "tag pelanggan",
    ]
    datetime_now = datetime.now().strftime("%m/%d/%Y")
    new_value = [datetime_now, datetime_now, "1/1/1900"]
    for nama_kolom in semua_nama_kolom:
        try:
            new_value.append(data[nama_kolom.lower()])
        except KeyError as e:
            raise ValueError(f"Mohon masukkan data {str(e)}.")
    sheet.update(row, [new_value])
