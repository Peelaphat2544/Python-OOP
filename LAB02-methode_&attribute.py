#LAB02 การนิยาม methode and Attribute
#โปรแกรมจัดการข้อมูลเกี่ยวกับพนักงาน ชื่อและเงินเดือน
#การสร้าง Class คือตัวแม่พิม ตัวต้นแบบ และตัวแรกต้องเป็นตัวพิมพ์ใหญ่เสมอ

class Employee:
    #สร้าง methode
    def detail (self):#ต้องใส่ self ด้วย เพื่อให้รู้ว่าเป็น Methode
        print("เรียกใช้งาน Method ใน Class Employee")
        self.name ="นายพีลพัทร์ แก้วคง" #กำหนด Attribute
        self.salary = 50000
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))


#สร้างวัตถุจากคลาส employee
emp1 = Employee() #นำชื่อคลาสมาระบุ
emp1.detail()#เรียกใช้งาน Methode ในคลาส Employee
