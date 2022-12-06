import random

def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pas = ''
    for i in range(11):
        pas += random.choice(a)
    return pas

d = password()
print ("Пароль:",d)
