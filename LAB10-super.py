#LAB10 Super - โจทย์เกี่ยวกับการใช้ super() ในการเรียกเมธอดของคลาสแม่

class Employee:
    _minSalary = 10000     # Class variable แบบ protected (สังเกตจาก _ นำหน้า) กำหนดเงินเดือนขั้นต่ำ
    maxSalary = 50000      # Class variable แบบ public กำหนดเงินเดือนสูงสุด
    companyName = "พีลพัทร์ เทคโนโลยี จำกัด"    # Class variable แบบ public เก็บชื่อบริษัท
    
    # Constructor (เมธอดสร้างวัตถุ) รับพารามิเตอร์ name, salary และ department
    def __init__(self, name, salary, department):
        self.__name = name             # Instance variable แบบ private เก็บชื่อพนักงาน
        self.__salary = salary         # Instance variable แบบ private เก็บเงินเดือนพนักงาน
        self.__department = department # Instance variable แบบ private เก็บแผนกของพนักงาน
    
    # เมธอดแสดงรายละเอียดพนักงาน (protected method สังเกตจาก _ นำหน้า)
    def _showData(self):
        print("-------------------------------")
        print(f"ชื่อพนักงาน = {self.__name}")
        print(f"เงินเดือน = {self.__salary}")
        print(f"ตำแหน่งงาน = {self.__department}")
        print("-------------------------------")

# คลาสลูก (Subclass) ชื่อ Accounting สืบทอดจากคลาส Employee
class Accounting(Employee):
    _departmentName = "บัญชี"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        # ใช้ super() เพื่อเรียกเมธอด __init__ จากคลาสแม่ (Employee)
        # และส่งค่า self._departmentName เป็นพารามิเตอร์ตัวที่ 3
        super().__init__(name, salary, self._departmentName)

# คลาสลูก (Subclass) ชื่อ Marketing สืบทอดจากคลาส Employee
class Marketing(Employee):
    _departmentName = "การตลาด"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        # ใช้ super() เพื่อเรียกเมธอด __init__ จากคลาสแม่ (Employee)
        super().__init__(name, salary, self._departmentName)

# คลาสลูก (Subclass) ชื่อ Programmer สืบทอดจากคลาส Employee
class Programmer(Employee):
    _departmentName = "โปรแกรมเมอร์"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        # ใช้ super() เพื่อเรียกเมธอด __init__ จากคลาสแม่ (Employee)
        super().__init__(name, salary, self._departmentName)
        # เรียกใช้เมธอด _showData จากคลาสแม่เพื่อแสดงข้อมูลทันทีที่สร้างอ็อบเจกต์
        super()._showData() 

# สร้างอ็อบเจกต์จากคลาส Accounting
account = Accounting("P", 12000)    # สร้าง instance ของคลาส Accounting

# สร้างอ็อบเจกต์จากคลาส Programmer
programmer = Programmer("P", 12000)    # สร้าง instance ของคลาส Programmer 
                                      # (มีการแสดงข้อมูลทันทีจาก super()._showData() ในคอนสตรักเตอร์)

# สร้างอ็อบเจกต์จากคลาส Marketing
marketing = Marketing("P", 12000)    # สร้าง instance ของคลาส Marketing

# เรียกใช้เมธอด _showData() กับอ็อบเจกต์ account
account._showData()    # เรียกเมธอด _showData() ที่สืบทอดมาจากคลาสแม่

# เรียกใช้เมธอด _showData() กับอ็อบเจกต์ marketing
marketing._showData()    # เรียกเมธอด _showData() ที่สืบทอดมาจากคลาสแม่