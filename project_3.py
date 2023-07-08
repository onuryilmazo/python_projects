email = str(input("enter an email: "))
splitted = email.split("@")
username = splitted[0]
domain = splitted[1]
print(username, domain)

'''
without using format


email = input("Enter Your Email: ").strip() # strip methodu başta ve sondaki boşluklari siler
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

'''