#definimos y creamos cada operación básica
def plus (n1,n2):
    return n1+n2
def minus (n1,n2):
    return n1-n2
def multiplication (n1,n2):
    return n1*n2
def division (n1,n2):
#controlamos que no se divida entre 0
   if n2 == 0:
       return 0
   else:
       return n1/n2