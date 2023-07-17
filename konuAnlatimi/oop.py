class MyClass:
    #constructor method 
    def __init__(self, x):   
        self.x = x

    #instance methodu   
    def print_x(self):
        print(self.x)
    
    #instance methodu 
    def set_x(self, new_x):
        self.x = new_x

#Aşağıdaki kod, MyClass sınıfından my_obj adında bir örnek(instance) oluşturur. Oluşturduğunuz her bir örnek, sınıfın özelliklerini ve methodlarını taşır.
my_obj = MyClass(10)
my_obj.print_x()  # 10
my_obj.set_x(20)
my_obj.print_x()  # 20
