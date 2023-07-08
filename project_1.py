user_input = str(input("Enter a Phrase: "))
text = user_input.split()
acronymus = []
'''
for i in text:
    acronymus.append(i[0])
Ayni işlemi yapan kod
'''
acronymus = [item[0] for item in text]
a = " "
for harf in range(0,len(acronymus)):
    a = a+ acronymus[harf].upper()
print(a)

'''
Kodun kolay çözümü

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

'''
