#LAB07 Setter Getter Methode

class Animal:
    def __init__(self,name,limb):
        self.__name = name #protected attribuit
        self.__limb = limb
    def _showDataAnimal(self): #protected Methode
        print("===============Protected=======================")
        print("สัตว์มีชื่อว่า = {}".format(self.__name))
        print("มีจำนวนขา = {} ขา".format(self.__limb))
        print("===============Protected=======================")
    def __del__(self):
        print("Call destructor")
    
    #setter methode #แก้ไขข้อมูลใหม่ได้ แม่ protected หรือ private
    def setName(self,name):
        self.__name = name
    
    def setLimb(self,limb):
        self.__limb = limb
    
    #getter methode #เรียกใช้งาน methode แล้วส่งข้อมูลไปยังภายนอก
    def getName(self):
        return self.__name
    
    def getLimb(self):
        return self.__limb

animal = Animal("สุนัข",4)
print("สัตว์ มีชื่อว่า",animal.getName())
print("มีจำนวน",animal.getLimb(),"ขา")

'''
animal.setName("สิงโต")
animal.setLimb(4)
animal._showDataAnimal()
'''
