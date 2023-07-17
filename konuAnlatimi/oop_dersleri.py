'''
#Opsiyonel argümanlar ve tip kontrolüyle çoklu yapıcıları taklit etme:

class Rectangle:
    def __init__(self, width, height=0):
        if height == 0:
            # Sadece bir argüman verildiyse kare oluşturulur
            self.width = width
            self.height = width
        else:
            # İki argüman verildiyse dikdörtgen oluşturulur
            self.width = width
            self.height = height

# Kare oluşturma
square = Rectangle(5)
print(square.width, square.height)  # Çıktı: 5 5

# Dikdörtgen oluşturma
rectangle = Rectangle(8, 4)
print(rectangle.width, rectangle.height)  # Çıktı: 8 4

#@classmethod dekoratörünü kullanarak birden fazla yapıcı yazma:

#@classmethod dekoratörü, Python'da sınıf metotları (class methods) tanımlamak için kullanılan bir araçtır. 
#Bir sınıf metodu, sınıfın kendisine değil, sınıfın kendisine referans veren bir argümana erişir.
#Sınıf metotları, sınıfın tüm örneklerine veya sınıfın kendisine ait verilere erişmek için kullanılabilir ve 
#genellikle sınıf seviyesindeki işlemleri gerçekleştirmek için kullanılırlar.

class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2): #Sınıf metotları, geleneksel olarak ilk argüman olarak cls adı verilen bir parametre alır. Bu parametre, sınıfın kendisini temsil eden bir referanstır. cls argümanı, sınıfın tüm örneklerine veya sınıf değişkenlerine erişmek için kullanılır.
        # Sınıf metodu içeriği
        pass
#Sınıf seviyesindeki işlemler için kullanılır:
#Sınıf metotları, sınıfın örneklerine bağlı olmayan ve sınıf seviyesindeki işlemleri gerçekleştirmek için kullanılır. 
#Örneğin, bir sınıf metodu, sınıfın belirli bir özelliğini değiştirebilir veya sınıf değişkenlerini kullanarak hesaplamalar yapabilir.

#Doğrudan sınıf üzerinden erişilebilir:
#Sınıf metotları, sınıfın kendisine erişmek için kullanılır ve bu nedenle sınıf üzerinden doğrudan çağrılabilirler.
#Örnek oluşturmadan sınıfın metotlarına erişebilirsiniz.

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def from_string(cls, name_string):
        names = name_string.split()
        return cls(names[0])

# Person sınıfından örnekler oluşturma
person1 = Person("Alice")
person2 = Person("Bob")

# Sınıf metodu kullanarak örnek sayısını alma
count = Person.get_count()
print(count)  # Çıktı: 2

# Sınıf metodu kullanarak stringden örnek oluşturma
person3 = Person.from_string("Charlie")
print(person3.name)  # Çıktı: Charlie

#@classmethod kullanmadan aynı işlemi yapan kod 
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

# Sınıf metodu kullanmadan count değişkenine erişim
print(Person.count)  # Çıktı: 0

person1 = Person("Alice")
person2 = Person("Bob")

print(Person.count)  # Çıktı: 2



class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        # Çapı kullanarak yarıçapı hesaplayan yapıcı
        radius = diameter / 2
        return cls(radius)

# Yarıçap ile daire oluşturma
circle = Circle(3)
print(circle.radius)  # Çıktı: 3

# Çap ile daire oluşturma
circle2 = Circle.from_diameter(10)
print(circle2.radius)  # Çıktı: 5





#@singledispatchmethod dekoratörünü kullanarak sınıf yapıcılarını aşırı yükleme:
class Shape:
    def __init__(self):
        pass

    @staticmethod
    def draw(shape):
        raise NotImplementedError("Bu şekli çizme yöntemi tanımlanmamış.")

    @staticmethod
    def draw_circle(circle):
        print("Daire çizildi.")

    @staticmethod
    def draw_rectangle(rectangle):
        print("Dikdörtgen çizildi.")

# Shape sınıfından örnek oluşturma
shape = Shape()

# Farklı şekiller çizme
circle = Circle(5)
shape.draw_circle(circle)  # Çıktı: Daire çizildi.

rectangle = Rectangle(4, 3)
shape.draw_rectangle(rectangle)  # Çıktı: Dikdörtgen çizildi.

'''
#Inhertiance (miras bırakma)

#Örnek bir sınıf oluşturalım

class Vehicle:
    def __init__(self,brand): #brand = attribute
        self.brand = brand

    def start_engine(self):
        print("Enigine started.")
'''
#Vehicle sınıfından bir örnek oluşturlarım
car = Vehicle("Toyota")
print(car.brand)
car.start_engine()
'''

#şimdi bu sınıftan bir alt sınıf oluşturucaz Vehicle sınıfı parent olacak.
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Üst sınıfın __init__ metotunu çağırma
        self.model = model

    def start_engine(self):
        super().start_engine()  # Üst sınıfın start_engine metotunu çağırma
        print("Car engine started.")


# Car sınıfından bir örnek oluşturma
car = Car("Toyota", "Camry")
print(car.brand)  # Çıktı: Toyota
print(car.model)  # Çıktı: Camry

car.start_engine()
# Çıktı:
# Engine started.
# Car engine started.

#Çoklu kalıtım 

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating.")


class Flyable:
    def fly(self):
        print("Flying...")


class Bird(Animal, Flyable):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan


# Bird sınıfından bir örnek oluşturma
bird = Bird("Eagle", 2)
print(bird.name)  # Çıktı: Eagle
print(bird.wingspan)  # Çıktı: 2

bird.eat()  # Çıktı: Animal is eating.
bird.fly()  # Çıktı: Flying...
