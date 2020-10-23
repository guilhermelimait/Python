# if

x = 2
y = 1
z = 0

if x < y:
    if y < z:
        print ("x é menor que y\ny e menor que z")
    else:
        print ("z menor que y")
else:
    print ("x e maior que y")

x = 1
y = 2

if x == y:
    print ("x igual a y")
elif x > y:
    print ("x maior que y")
elif x < y: 
    print ("x menor que y")
else:
    print ("valor nao reconhecido")