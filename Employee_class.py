class Employee:
    # Constructor (เมธอดสร้างวัตถุ) รับพารามิเตอร์ name และ salary
    def __init__(self, name, salary):
        self.__name = name    # Instance variable แบบ private เก็บชื่อพนักงาน
        self.__salary = salary    # Instance variable แบบ private เก็บเงินเดือน

    # เมธอดแสดงข้อมูลพนักงาน (protected method สังเกตจาก _ นำหน้า)
    # เมธอดนี้จะถูก override โดยคลาสลูก (Accounting และ Programer)
    def _showData(self):
        print(f"ชื่อพนักงาน = {self.__name}")
        print(f"เงินเดือนของพนักงาน = {self.__salary}")
    
    # เมธอดสำหรับดึงค่าเงินเดือน (protected method)
    def _getincome(self):
        return self.__salary
    
    # Destructor (เมธอดที่ทำงานเมื่อวัตถุถูกทำลาย)
    def __del__(self):
        print()  # ทำการขึ้นบรรทัดใหม่เมื่อวัตถุถูกทำลาย