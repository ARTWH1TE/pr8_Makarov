import random

def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c = ['1','2','3','4','5','6','7','8','9','0']
    pas = ''
    for i in range(11):
        pas += random.choice(a + c)
    return pas

d = password()
print ("Пароль:",d)
