'''
Bu kod attribute anlasilmasi icin yazilmis bir koddur. Attribute bir class in ozelliklerini belirtir.
Mesela bu ornekte marka model renk ve hiz birer attribute dur. 
'''
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0
    
    def accelerate(self, acceleration):
        self.speed += acceleration
    
    def brake(self, deceleration):
        self.speed -= deceleration
        if self.speed < 0:
            self.speed = 0
    
    def print_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Speed:", self.speed)


# Örnek kullanım
car1 = Car("BMW", "X5", "Black")
car1.print_info()  # Marka: BMW, Model: X5, Renk: Siyah, Hız: 0

car1.accelerate(20)
car1.print_info()  # Marka: BMW, Model: X5, Renk: Siyah, Hız: 20

car1.brake(10)
car1.print_info()  # Marka: BMW, Model: X5, Renk: Siyah, Hız: 10

'''
Lambda expressions:

Evet, tabii ki! Python'da lambda ifadesi, anonim (isimsiz) fonksiyonlar oluşturmak için kullanılan bir işlevsel programlama aracıdır. 
Lambda ifadesi, kısa ve tek satırlık fonksiyonları daha kolay bir şekilde tanımlamamıza olanak sağlar.
Genel gösterim şu şekilde 

lambda arguments: expression

Burada arguments, lambda fonksiyonuna geçirilen parametrelerin listesidir ve expression, lambda fonksiyonunun dönüş değerini ifade eden bir ifadedir.

Lambda ifadesi, küçük ve basit fonksiyonları hızlıca tanımlamak için kullanılır. Özellikle, bir fonksiyonu yalnızca bir kez kullanmayı planlıyorsanız 
ve ona özel bir isim vermek istemiyorsanız, lambda ifadesi oldukça kullanışlıdır.

'''
print("***************************")

# İki sayıyı toplayan lambda fonksiyonu
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Bir sayının karesini alan lambda fonksiyonu
square = lambda x: x**2
print(square(4))  # 16

# İki sayı arasındaki en büyük sayıyı bulan lambda fonksiyonu
max_num = lambda x, y: x if x > y else y
print(max_num(10, 7))  # 10

# Liste elemanlarını ikiye bölen lambda fonksiyonu
numbers = [1, 2, 3, 4, 5]
halve = lambda x: x / 2
halved_numbers = list(map(halve, numbers))
print(halved_numbers)  # [0.5, 1.0, 1.5, 2.0, 2.5]


add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b
'''
while True:
    print("""\nEnter
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit""")
    try:
        choice = int(input('\nEnter choice: '))
    except:
        print('Enter integer values only!')
        continue
    if 1<=choice<=5:
        if choice==5:
            print('Exiting...\n')
            break
        numbers = [int(i) for i in input('Enter numbers: ').split()]
        if choice==1:
            print('\nResult is: ', add(numbers[0], numbers[1]), '\n')
            continue
        if choice==2:
            print('\nResult is: ', subtract(numbers[0], numbers[1]), '\n')
            continue
        if choice==3:
            print('\nResult is: ', multiply(numbers[0], numbers[1]), '\n')
            continue
        if choice==4:
            print('\nResult is: ', divide(numbers[0], numbers[1]), '\n')
            continue
    else:
        print('Enter choice between 1 and 5')
'''
print("***************************")

from enum import Enum
#NOTE: By convention, The name of the members of this class should be in upper-case as they are constants.
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
favorite_color = Color.RED
print(type(favorite_color))
#Asagıdaki uc kodda ayni islemi goruyor
print(favorite_color.name, "=", favorite_color.value)
print(Color.RED.name + " = " + str(Color.RED.value))
print(Color['RED'].name + " = " + str(Color['RED'].value))

'''
Python'da generator ve iterator kavramları, tekrarlanabilir ve yinelemeli işlemleri gerçekleştirmek için kullanılan önemli araçlardır.

Iterator (Yineleyici): Bir objenin veya bir veri yapısının elemanlarına sırayla erişmemizi sağlayan bir arayüzdür. 
Iteratorler, __iter__() ve __next__() metodlarını uygulayan objelerdir. __iter__() metodunun çağrılması, iterator objesini döndürürken,
 __next__() metodunun çağrılması ise sıradaki elemanı döndürür. Her __next__() çağrısı, bir sonraki elemana ilerler. İterasyon sonlandığında, StopIteration hatası fırlatılır.

'''
print("***************************")
class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Iterator objesini oluşturma
my_iterator = MyIterator(5)

# İterasyon yapma
for item in my_iterator:
    print(item)

# Çıktı:
# 0
# 1
# 2
# 3
# 4
# 5

'''
Generator (Üreteç): Bir fonksiyonun veya ifadenin, işleme devam etmeden geçici olarak duraklatılabilmesini ve daha sonra devam edebilmesini sağlayan bir yapıcıdır. 
Generator fonksiyonları yield ifadesini içerir ve her bir yield ifadesi, fonksiyonun çağrıldığında bir değer döndürmesini ve duraklamasını sağlar. 
Bir sonraki çağrıda, duraklama yerinden devam eder ve sonraki değeri döndürür.
Generator'lar, büyük veri kümesi oluşturmak veya bellek kullanımını azaltmak gibi durumlarda kullanışlıdır.
Her döngüde sadece bir değer hesaplandığından, büyük miktarda bellek kullanımı gerektiren işlemlerde verimli bir şekilde çalışabilirler.
Ayrıca, iterasyonun duraklatılmasına ve istendiğinde devam ettirilmesine olanak sağlarlar.
'''
def my_generator(max_value):
    current = 0
    while current <= max_value:
        yield current
        current += 1 #return ile yapsak burayı çalıştırmazdı

# Generator objesini oluşturma
my_generator_obj = my_generator(5)

# İterasyon yapma
for item in my_generator_obj:
    print(item)

# Çıktı:
# 0
# 1
# 2
# 3
# 4
# 5
print("***************************")
'''
Python'da "regular expressions" veya kısaltmasıyla "regex" olarak bilinen düzenli ifadeler, metinlerde desen eşleştirmeleri yapmak ve metinleri işlemek için kullanılan güçlü bir araçtır. Python, re modülü aracılığıyla regex desteği sağlar.

Regex ifadeleri, metinlerde arama, eşleştirme, dönüşüm ve metin manipülasyonu gibi birçok farklı amaç için kullanılabilir. Regex, belirli bir deseni tanımlamak için özel karakterler ve semboller kullanır.
 Bu desenler, metin içinde aranan kalıpları ifade eder. Regex ifadeleri, bir metinde desenin eşleştiği pozisyonları veya eşleşen metinleri bulmak için kullanılabilir.

Python'da regex kullanımı için re modülü kullanılır. re modülü, regex ifadelerini oluşturmak ve regex işlemlerini gerçekleştirmek için gerekli fonksiyonları ve yöntemleri sağlar. İşte bazı temel regex fonksiyonları ve yöntemleri:

re.search(pattern, string): Bir metinde belirtilen desenin ilk eşleşmesini arar ve bir match nesnesi döndürür.
re.match(pattern, string): Bir metnin başlangıcında belirtilen desenle eşleşme arar ve bir match nesnesi döndürür.
re.findall(pattern, string): Metinde belirtilen desenle eşleşen tüm alt dizeleri bulur ve bir liste olarak döndürür.
re.finditer(pattern, string): Metinde belirtilen desenle eşleşen tüm alt dizeleri bulur ve bir iterator olarak döndürür.
re.sub(pattern, repl, string): Metinde belirtilen desenle eşleşen alt dizeleri belirtilen bir değerle değiştirir.
re.split(pattern, string): Metni belirtilen desene göre böler ve bir liste olarak döndürür.

'''

import re

# Metinde "apple" kelimesini arama
text = "I have an apple and a banana"
pattern = r"apple"  # r ifadesiyle raw string olarak tanımlanır
result = re.search(pattern, text)
if result:
    print("Eşleşme bulundu.")
else:
    print("Eşleşme bulunamadı.")

# Çıktı: Eşleşme bulundu.


'''
Python'da "raw string" veya "ham dizge" olarak adlandırılan bir ifade, kaçış dizilerini yorumlamadan doğrudan içerdikleri karakterleri temsil eden bir dizgedir.
 Raw string ifadesi, özellikle düzenli ifadeler (regex) gibi metinlerde kaçış dizilerinin etkisiz hale getirilmesi gerektiği durumlarda kullanılır.
'''
path = r"C:\Users\Username\Documents"
print(path)

