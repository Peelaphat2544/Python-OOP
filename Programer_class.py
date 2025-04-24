
from Employee_class import Employee

class Programer(Employee):  # คลาส Programer สืบทอดจากคลาส Employee
    departmentName = "นักพัฒนาซอฟแวร์"  # Class variable (ตัวแปรระดับคลาส) แบบ public เก็บชื่อแผนก
    bonusperyear = 50000  # Class variable (ตัวแปรระดับคลาส) แบบ public เก็บโบนัสต่อปี
    
    # Constructor รับพารามิเตอร์ name, salary, experience และ skill
    # เป็นการ overloading constructor จากคลาสแม่ โดยเพิ่มพารามิเตอร์ experience และ skill
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary)  # เรียกใช้ constructor ของคลาสแม่
        self.experience = experience  # Instance variable (ตัวแปรระดับอินสแตนซ์) แบบ public เก็บประสบการณ์ทำงาน
        self.skill = skill  # Instance variable (ตัวแปรระดับอินสแตนซ์) แบบ public เก็บทักษะ
    
    # Method Overriding - การเขียนทับเมธอด _showData จากคลาสแม่ (Polymorphism)
    # เมธอดมีชื่อเดียวกับคลาสแม่แต่มีการทำงานที่ต่างกัน
    def _showData(self):
        print("==================แผนก {}====================".format(self.departmentName))
        super()._showData()  # เรียกใช้เมธอด _showData ของคลาสแม่
        print(f"ประสบการณ์ : {self.experience} ปี")
        print(f"ทักษะ : {self.skill}")
        print(f"ตำแหน่งงาน : {self.departmentName}")
        print(f"เงินเดือนรวมกับโบนัสต่อปี : {super()._getincome() + self.bonusperyear} บาท")