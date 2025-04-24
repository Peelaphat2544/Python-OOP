# LAB12 polymorphism - โจทย์เกี่ยวกับการใช้หลักการ Polymorphism (พหุรูป) ในการเขียนโปรแกรม

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


class Marketing(Employee):  # คลาส Marketing สืบทอดจากคลาส Employee
    pass  # ยังไม่มีการกำหนดเมธอดหรือแอตทริบิวต์เพิ่มเติม (เป็นคลาส empty)
          # หากมีการสร้าง instance ของคลาสนี้ จะใช้เมธอดจากคลาสแม่ทั้งหมด (ไม่มีการ override)


# สร้างวัตถุ (Object) จากคลาส Accounting
accounting = Accounting("Jone", 12000, 20)  # สร้าง instance ของคลาส Accounting
accounting._showData()  # เรียกใช้เมธอด _showData ที่ override แล้วของคลาส Accounting
print()  # ขึ้นบรรทัดใหม่

# สร้างวัตถุ (Object) จากคลาส Programer
programer = Programer("Tom", 50000, 5, "Python")  # สร้าง instance ของคลาส Programer
programer._showData()  # เรียกใช้เมธอด _showData ที่ override แล้วของคลาส Programer