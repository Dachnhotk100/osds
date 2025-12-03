import sqlite3

#1. kết nối tới cơ sở dữ liệu
conn = sqlite3.connect("inventory.db")

#tạo đối tượng ' corsor để thực thi các câu lếnhql

cursor = conn.cursor()

#thao tác vs database và table 

# lenh SQL de tao bang product 
sql1 = """CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , name TEXT NOT NULL
    , price NUMERIC NOT NULL
    , quantity INTEGER NOT NULL
)"""

#thuc thi lenh tao bang
cursor.execute(sql1)
conn.commit() # luu thay doi vao db

#3. CRUD
#3.1 them(insert)

prodcuts_data = [
    ("Iphone 14", 25000000, 10),
    ("Samsung S23", 20000000, 15),
    ("Xiaomi 13", 15000000, 20)]

#lenh SQL de chen du lieu . dung "? " de tranh loi tan cong SQL Injection
sql2 = """INSERT INTO product (name, price, quantity) VALUES (?, ?, ?)"""

#them nhieu bang ghi cung luc
cursor.executemany(sql2, prodcuts_data)
conn.commit()#luu thay doi

#3.2 doc (select)
sql3 = """SELECT * FROM product"""

#thuc thi lenh truy van 
cursor.execute(sql3)

#lay all ket qua
all_products = cursor.fetchall()

#in tieu de
print (f"{'ID':<4} {'Ten San Pham':<20} {'Gia ':<15} {'So Luong':<10}")

#lap va in ra 
for p in all_products  :
    print (f"{p[0]:<4} {p[1]:<20} {p[2]:<15} {p[3]:<10}")

#3.3 cap nhat (update)
sql4 = """ UPDATE Ten Sap Pham  
            SET Gia = ?, So Luong = ?
            WHERE id = ?"""
cursor.execute(sql4)
conn. commit()#luu thay doi

#3.4 xoa (delete)
sql5 = """ DELETE FROM Ten San Pham 
            WHERE id = ?"""
cursor.execute(sql5)
conn. commit()#luu thay doi

# khi tạo hàm phải có lệnh lưu thay đổi là cursor.execute(sqln) và conn.commit()
