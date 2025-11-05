class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

class FileManager:
    @staticmethod
    def save_to_file(content, filename):
        with open(filename, 'w') as f:
            f.write(content)
    
file1 = 'file.txt'    

book = Book('voina i mir', 'tolstoi', 'qwerty')

fm = FileManager()

fm.save_to_file(book.content, file1)

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
class GradeCalculator:
    @staticmethod
    def calculate_averages(grades):
        return sum(grades) / len(grades) 
    
s = Student('gad', [1, 2, 3, 4, 5])

gc = GradeCalculator()

print(gc.calculate_averages(s.grades))

class Order:
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price
    
class InvoicePrinter:
    @staticmethod
    def print_invoice(items, total_price):
        print(items, total_price)

o = Order(['carrot', 'stick'], 13)

ip = InvoicePrinter()

ip.print_invoice(o.total_price, o.items)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
      
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        
    def area(self):
        return self.side1 * self.side2
    
class Payment:
    @staticmethod
    def pay(amount):
        print(amount)
        
class CreditCardPayment(Payment):
    pass

class PayPalPayment(Payment):
    pass

class CryptoPayment(Payment):
    pass

class Notifier:
    @staticmethod
    def send(message):        
        print(message)
        
class EmailNotifier(Notifier):
    pass

class SMSNotifier(Notifier):
    pass

class PushNotifier(Notifier):
    pass

class FlyingUnit:
    @staticmethod
    def fly():
        print('flying')

class GroundUnit:
    pass

class Drone(FlyingUnit):
    pass

class Tank(GroundUnit):
    pass

class IShooter:
    def shoot():
        pass

class INavigator:
    def navigate():
        pass

class IAirSupportCaller:
    def callAirSupport():
        pass

class Infantry(IShooter, INavigator):
    pass

class ForwardObserver(INavigator, IAirSupportCaller):
    pass

class Pilot(IAirSupportCaller):
    pass

class IDrive:
    def drive():
        pass
    
class IFly:
    def fly():
        pass
    
class ISail:
    def sail():
        pass
    
class Tank(IDrive):
    pass

class FighterJet(IDrive, IFly):
    pass

class Submarine(ISail):
    pass


class IMorseComm:
    def sendMorseCode():
        pass
    
class IRadioComm:
    def sendRadio():
        pass
    
class ISatelliteComm:
    def sendSatellite():
        pass
    
class FieldRadio(IRadioComm):
    pass

class SatelliteComm(ISatelliteComm):
    pass

class LegacyMorseUnit(IMorseComm):
    pass
        
    
    