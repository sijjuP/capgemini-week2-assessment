class Electronics:
    def __init__(self):
        self.type="Electronics"
    def display(self):
        print(f"Electronics type:{self.type}")

class MobileDevice(Electronics):
    def __init__(self):
        self.type="MobileDevice"
    def display(self):
        print(f"MobileDevice type:{self.type}")

class SmartPhone(MobileDevice):
    def __init__(self):
        self.type="SmartPhone"
    def display(self):
        print(f"SmartPhone type:{self.type}")

smart_phone=SmartPhone()
smart_phone.display()