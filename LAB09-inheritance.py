#LAB09 Inheritance (การสืบทอดคุณสมบัติ)
"""
super class เช่น พนักงาน
sub class เช่น โปรแกรมเมอร์ นักบัญชี นักการตลาด
"""

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
        print(f"ชื่อพนักงาน = {self.__name}")
        print(f"เงินเดือน = {self.__salary}")
        print(f"ตำแหน่งงาน = {self.__department}")

# คลาสลูก (Subclass) ชื่อ Accounting สืบทอดจากคลาส Employee
class Accounting(Employee):  # สืบทอดคุณสมบัติมาจาก Employee class
    _departmentName = "บัญชี"  # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor ของคลาส Accounting (ไม่รับพารามิเตอร์)
    def __init__(self):
        pass  # ไม่ได้ทำอะไรใน constructor นี้ (เป็น empty constructor)
             # ไม่มีการเรียกใช้ constructor ของคลาสแม่

# คลาสลูก (Subclass) ชื่อ Marketing สืบทอดจากคลาส Employee
class Marketing(Employee):
    _departmentName = "การตลาด"  # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor ของคลาส Marketing (ไม่รับพารามิเตอร์)
    def __init__(self):
        pass  # ไม่ได้ทำอะไรใน constructor นี้ (เป็น empty constructor)

# คลาสลูก (Subclass) ชื่อ Programmer สืบทอดจากคลาส Employee
class Programmer(Employee):
    _departmentName = "โปรแกรมเมอร์"  # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor ของคลาส Programmer (ไม่รับพารามิเตอร์)
    def __init__(self):
        pass  # ไม่ได้ทำอะไรใน constructor นี้ (เป็น empty constructor)

# สร้างอ็อบเจกต์จากคลาสลูกทั้ง 3 คลาส
account = Accounting()      # สร้าง instance ของคลาส Accounting
programmer = Programmer()   # สร้าง instance ของคลาส Programmer
marketing = Marketing()     # สร้าง instance ของคลาส Marketing

# การเข้าถึง Class variable จากอ็อบเจกต์ของคลาสลูก
print(account.maxSalary)             # เข้าถึง Class variable แบบ public ที่สืบทอดมาจากคลาสแม่
print(programmer._minSalary)         # เข้าถึง Class variable แบบ protected ที่สืบทอดมาจากคลาสแม่
print(marketing._departmentName)     # เข้าถึง Class variable แบบ protected ของคลาสลูก Marketing