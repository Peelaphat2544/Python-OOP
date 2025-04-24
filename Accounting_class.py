from Employee_class import Employee
class Accounting(Employee):  # คลาส Accounting สืบทอดจากคลาส Employee
    __departmentName = "การเงินและการบัญชี"  # Class variable (ตัวแปรระดับคลาส) แบบ private เก็บชื่อแผนก
    __bonusperyear = 10000  # Class variable (ตัวแปรระดับคลาส) แบบ private เก็บโบนัสต่อปี
    
    # Constructor รับพารามิเตอร์ name, salary และ age
    # เป็นการ overloading constructor จากคลาสแม่ โดยเพิ่มพารามิเตอร์ age
    def __init__(self, name, salary, age):
        super().__init__(name, salary)  # เรียกใช้ constructor ของคลาสแม่
        self.age = age  # Instance variable (ตัวแปรระดับอินสแตนซ์) แบบ public เก็บอายุ
    
    # Method Overriding - การเขียนทับเมธอด _showData จากคลาสแม่ (Polymorphism)
    # เมธอดมีชื่อเดียวกับคลาสแม่แต่มีการทำงานที่ต่างกัน
    def _showData(self):
        print("==================แผนก {}====================".format(self.__departmentName))
        super()._showData()  # เรียกใช้เมธอด _showData ของคลาสแม่
        print(f"อายุ : {self.age} ปี")
        print(f"ตำแหน่งงาน : {self.__departmentName}")
        print(f"เงินเดือนรวมกับโบนัสต่อปี : {super()._getincome() + self.__bonusperyear} บาท")