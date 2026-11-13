# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class upipayement(Payment):
#     def pay(self,amount):
#         print("paying via UPI",amount)


#area and perimeter

# from abc import ABC,abstractmethod
# from turtle import width

# class shape (ABC):

#     def __init__(self,name):
#         self.name=name

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class rectangle(shape):
#     def __init__(self,length,width):
#         super().__init__("rectangle")
#         self.length=length
#         self.width=width
    
#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius
# circle1=circle(5)
# print("area of circle:",circle1.area())
# print("perimeter of circle:",circle1.perimeter())

# rectangle1=rectangle(4,6)
# print("area of rectangle:",rectangle1.area())
# print("perimeter of rectangle:",rectangle1.perimeter())

#blinkit order

from abc import ABC,abstractmethod

class order(ABC):
    def __init__(self,customer_name,order_amount):
        self.customer_name=customer_name
        self.order_amount=order_amount
@abstractmethod
def calculate_delivery_charge(self):
    pass

class restrauantorder(order):
    def calculate_delivery_charge(self):
        return 40
    def desplay_order(self):
        delivery = self.calculate_delivery_charge()
        print("restraunt order ")
        print("customer:", self.customer_name)
        print("food amount:", self.order_amount)
        print("delivery charge:", delivery)
        print("total amount:", self.order_amount + delivery)

# 

class groceryorder(order):
    def calculate_delivery_charge(self):
        return 50
    def desplay_order(self):
        delivery = self.calculate_delivery_charge()
        print("grocery order ")
        print("customer:", self.customer_name)
        print("food amount:", self.order_amount)
        print("delivery charge:", delivery)
        print("total amount:", self.order_amount + delivery)

class medicineorder(order):
    def calculate_delivery_charge(self):
        return 60
    def desplay_order(self):
        delivery = self.calculate_delivery_charge()
        print("medicine order ")
        print("customer:", self.customer_name)
        print("food amount:", self.order_amount)
        print("delivery charge:", delivery)
        print("total amount:", self.order_amount + delivery)

print("welcome to blinkit order")
name=input("enter your name:")
amount=int(input("enter your order amount:"))
