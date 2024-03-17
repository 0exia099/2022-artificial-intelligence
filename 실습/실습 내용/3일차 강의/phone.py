class PhoneBook:
    def __init__(self):
        self.contact = {}
        
    def add(self, name, phone=None, email=None):
        self.contact[name] = (phone, email)
        
    def get(self, name):
        return self.contact[name]
    
    def __str__(self):
        msg = ""
        for key, value in self.contact.items():
            msg += f"{key}\n"
            msg += f"전화번호: {value[0]}\n이메일: {value[1]}\n"
        return msg
    
pb = PhoneBook()
pb.add("Cho", phone="010-1234-5678", email="cho@yu.ac.kr")
pb.add("Kim", phone="010-2345-6789", email="lee@korea.com")
print(pb)
print("Cho의 주소록 =", pb.get("Cho"))
