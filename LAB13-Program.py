from Programer_class import Programer
from Accounting_class import Accounting

# สร้างวัตถุ (Object) จากคลาส Programer
programer = Programer("Tom", 50000, 5, "Python")  # สร้าง instance ของคลาส Programer
programer._showData()  # เรียกใช้เมธอด _showData ที่ override แล้วของคลาส Programer