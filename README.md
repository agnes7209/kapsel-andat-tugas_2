schemas.py
    data: Optional[UserResponse] = None
        memungkinkan data pada UserResponse untuk bernilai null/None
        contoh: perintah delete atau terjadi error saat memasukan data, artinya tidak ada data yang dikembalikan
    email: EmailStr = Field(..., description='must be a valid email address') 
        ketentuan email masih sangat sederhana. 
        hanya error kalau tidak menyertakan @.
        tidak error saat .com tidak ada.
        perlu pengembangan
    