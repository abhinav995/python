# class Car:
#      def __init__(self,name,price,colour):
#           self.name=name
#           self.price=price
#           self.colour=colour
#      def start(self):
#           print("n")     
# car1=Car(name="sonet",price="ten_lakh",colour="red")
# car2=Car(name="alto",price="four_lakh",colour="white")
# print(car1.name) 
# car1.start()

# class Food:
#      def __init__(self,name,price,count):
#           self.name=name
#           self.price=price
#           self.count=count
#      def start(self):
#           print("eat")
# food1=Food(name="chapathi",price="ten_rupees",count="three")
# food2=Food(name="porotta",price="twelve_rupees",count="five")
# print(food1.count)
# food1.start()
          
#inheritance
# class Person:
#       def __init__(self,name,contact):
#             self.name=name
#             self.contact=contact
# class Doctor(Person):
#       pass 
# class Patient(Person):
#       pass
# doctor1=Doctor(name="abhinav",contact=8921410392)
# print(doctor1.name)
      
#
class Shape:
      def display(self):
            print("this is shape")
class Rectangle(Shape):
      def display(self):
           print("this is rectangular shape")
class Circle(Shape):
      def display(self):
           print("this is circular shape")   
class Square(Rectangle):
      def display(self):
           print("this is square shape")         
circle1=Circle() 
circle1.display()    
                  
            
