def ehTriangulo(a,b,c):
    if (a>0 and b>0 and c>0) and ((a+b>=c) and (a+c>=b) and (b+c>=a)):
        return True
    else:
        return False

def tipoTriangulo(a,b,c):
    if a==b and b==c:
        return 'Eqüilátero'
    elif a!=b and b!=c and a!=c:
        return 'Escaleno'
    else:
        return 'Isóceles'

a = 4
b = 3
c = 5

if ehTriangulo(a,b,c):
    print(tipoTriangulo(a,b,c))
else:
    print("Não é um triângulo")



    