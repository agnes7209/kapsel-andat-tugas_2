schemas.py
    data: Optional[UserResponse] = None
        memungkinkan data pada UserResponse untuk bernilai null/None
        contoh: perintah delete atau terjadi error saat memasukan data, artinya tidak ada data yang dikembalikan
    email: EmailStr = Field(..., description='must be a valid email address') 
        ketentuan email masih sangat sederhana. 
        hanya error kalau tidak menyertakan @.
        tidak error saat .com tidak ada.
        perlu pengembangan
    
read.py 
    @router.get("/users/{user_id}", response_model=ResponseModel) 
    async def read_user(
        user_id: str,
        role: str = Header(...),
        user_id_confirmed: Optional[str] = Header(None)
    )
        kekurangannya, staff bisa sajah memasukan user_id secara asal-asalan untuk role admin. 
        ide pengembangan: semua user juga wajib mengisi password 

update.py
        perlu ditambahkan syarat mengisi password
        
delete.py
        perlu ditambahkan syarat mengisi password
