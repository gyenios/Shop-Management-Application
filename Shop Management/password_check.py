Password = 'gyenios'
tries = 3

def authenticate(password):
    if password == Password:
        print('--Login successful--')
        return True
    else:
        print('Wrong Password')
        return False
    return True

while tries > 0:
    password = input('Enter password >> ').lower()
    value = authenticate(password)
    if value == False:
        tries -= 1
    elif value == True:
        break
if tries == 0 and value == False:
    print('Too many wrong inputs')
        
