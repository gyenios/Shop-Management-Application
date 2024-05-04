from functions import *
print('''
   Login as:
    [1] Admin
    [2] Customer
''')
response = input()
if response == '1':
    if get_password() == True:
        admin = Admin()
        admin.menu()
        
elif response == '2':
    customer = Customer()
    customer.menu()
    
    
