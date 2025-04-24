#LAB11 Obj to string

class Employee:
    _minSalary = 10000    # Class variable แบบ protected (สังเกตจาก _ นำหน้า) กำหนดเงินเดือนขั้นต่ำ
    maxSalary = 50000     # Class variable แบบ public กำหนดเงินเดือนสูงสุด
    companyName = "พีลพัทร์ เทคโนโลยี จำกัด"    # Class variable แบบ public เก็บชื่อบริษัท
    
    # Constructor (เมธอดสร้างวัตถุ) รับพารามิเตอร์ name, salary และ department
    def __init__(self, name, salary, department):
        self.__name = name            # Instance variable แบบ private เก็บชื่อพนักงาน
        self.__salary = salary        # Instance variable แบบ private เก็บเงินเดือนพนักงาน
        self.__department = department    # Instance variable แบบ private เก็บแผนกของพนักงาน
    
    # เมธอดแสดงรายละเอียดพนักงาน (protected method สังเกตจาก _ นำหน้า)
    def _showData(self):
        print("-------------------------------")
        print(f"ชื่อพนักงาน = {self.__name}")
        print(f"เงินเดือน = {self.__salary}")
        print(f"ตำแหน่งงาน = {self.__department}")
        print("-------------------------------")
    
    # เมธอดคำนวณรายได้ต่อปี (protected method)
    def _getincome(self):
        return self.__salary * 12
    
    # เมธอดพิเศษ __str__ สำหรับแสดงข้อความเมื่อมีการแปลงอ็อบเจกต์เป็น string
    # เช่น เมื่อใช้ print(object) หรือ str(object)
    def __str__(self):
        return (f"ชื่อพนักงาน = {self.__name}\n"
                f"เงินเดือน = {self.__salary}\n"
                f"ตำแหน่งงาน = {self.__department}\n"
                f"รายได้ต่อปี = {self._getincome()}")

# คลาสลูก (Subclass) ชื่อ Accounting สืบทอดจากคลาส Employee
class Accounting(Employee):
    _departmentName = "บัญชี"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        super().__init__(name, salary, self._departmentName)    # เรียกใช้ constructor ของคลาสแม่ โดยส่งค่า _departmentName จากคลาสตัวเอง

# คลาสลูก (Subclass) ชื่อ Marketing สืบทอดจากคลาส Employee
class Marketing(Employee):
    _departmentName = "การตลาด"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        super().__init__(name, salary, self._departmentName)    # เรียกใช้ constructor ของคลาสแม่ โดยส่งค่า _departmentName จากคลาสตัวเอง

# คลาสลูก (Subclass) ชื่อ Programmer สืบทอดจากคลาส Employee
class Programmer(Employee):
    _departmentName = "โปรแกรมเมอร์"    # Class variable แบบ protected เก็บชื่อแผนก
    
    # Constructor overloading - รับพารามิเตอร์น้อยกว่าคลาสแม่
    def __init__(self, name, salary):
        super().__init__(name, salary, self._departmentName)    # เรียกใช้ constructor ของคลาสแม่ โดยส่งค่า _departmentName จากคลาสตัวเอง
        super()._showData()    # เรียกใช้เมธอด _showData จากคลาสแม่เพื่อแสดงข้อมูลทันทีที่สร้างอ็อบเจกต์

# สร้างอ็อบเจกต์จากคลาส Accounting
account = Accounting("P", 12000)    # สร้าง instance ของคลาส Accounting
print("รายได้ต่อปี = ", account._getincome())    # เรียกใช้เมธอด _getincome จากคลาสแม่

# สร้างอ็อบเจกต์จากคลาส Programmer
programmer = Programmer("P", 12000)    # สร้าง instance ของคลาส Programmer (มีการแสดงข้อมูลทันทีจาก super()._showData())

# สร้างอ็อบเจกต์จากคลาส Marketing
marketing = Marketing("P", 12000)    # สร้าง instance ของคลาส Marketing
print(marketing.__str__())    # เรียกใช้เมธอด __str__ จากคลาสแม่เพื่อแสดงข้อมูลในรูปแบบ string (เทียบเท่ากับ print(marketing))