import random

def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c = ['1','2','3','4','5','6','7','8','9','0']
    pas = ''
    for i in range(11):
        pas += random.choice(a + b + c)
    return pas

d = password()
print ("Пароль:",d)
