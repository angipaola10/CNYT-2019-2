#!/usr/bin/env python
# coding: utf-8

# Importacion de librerias 

# In[274]:


import math 


# Función para imprimir numeros complejos ( imprimirNum )

# In[275]:


def imprimirNum (num):
    if num != "No es posible realizar esta operación":
        x = num[0]
        y = num[1]
        if x == 0:
            if y == 0:
                print (0)
            elif y == 1: 
                print ("i")
            else:
                print (str(y)+"i")
        elif y == 0:
            print (x)
        elif num[1] < 0:
            print(str(x)+ " - "+str(y*(-1))+"i")
        else:
            print(str(x)+ " + "+str(y)+"i")


# A continuación se realizarán pruebas, para determinar que la función imprimirNum funcione correctamente 
imprimirNum ([1,2])
imprimirNum ([0,0])
imprimirNum ([0,2])
imprimirNum ([2,0])
# 
# *NOTA : Tenga en cuenta que para usar funciones que requieran grados, dichos grados debe ingresarlos en radianes*
#     

# A continuación se definen las funciones sumar, restar y multiplicar, las cuales reciben 2 números complejos representados en un arreglo.
# Ejemplo:  2 + 4i = [2,4],  8i = [0,8], 4 = [4,0]
# 

# In[276]:


def sumar (x , y):
    resultado  = [ (x[0]+y[0]) , (x[1]+y[1])]
    return resultado


# Pruebas para la funcion sumar :

# In[277]:


imprimirNum(sumar ([1,2],[5,9]))


# In[278]:


imprimirNum(sumar ([-8,7],[7,-6]))


# In[279]:


imprimirNum(sumar ([0,1],[0,-1]))


# In[280]:


def restar (x , y):
    resultado  = [ (x[0]-y[0]) , (x[1]-y[1])]
    return resultado


# Pruebas para la función restar :

# In[281]:


imprimirNum(restar ([1,2],[5,9]))


# In[282]:


imprimirNum(restar ([-8,7],[7,-6]))


# In[283]:


imprimirNum(restar ([0,1],[0,-1]))


# In[284]:


def multiplicar (x , y):
    resultado = [ (x[0]*y[0] - x[1]*y[1]) , (x[0]*y[1] + x[1]*y[0])] 
    return resultado


# pruebas para la función multiplicar:

# In[285]:


imprimirNum(multiplicar ([-3,-1],[1,-2]))


# In[286]:


imprimirNum(multiplicar ([3,-2],[1,2]))


# In[287]:


imprimirNum(multiplicar ([0,5],[5,0]))


# In[288]:


def dividir (x , y):
    if y[0] == 0 and y[1] == 0:
        print ("No es posible realizar esta operación")
        return "No es posible realizar esta operación"
    else:
        temp = y[0]**2 + y[1]**2 
        temp1 = x[0]*y[0] + x[1]*y[1]
        temp2 = y[0]*x[1] - x[0]*y[1]
        temp1 = round(temp1, 2)
        temp2 = round(temp2, 2)
        resultado = [temp1/temp , temp2/temp]   
        return resultado


# pruebas para la función dividir:

# In[289]:


imprimirNum(dividir ([-2,1],[1,2]))


# In[290]:


imprimirNum(dividir ([5,4],[0,0]))


# In[291]:


imprimirNum(dividir ([0,3],[-1,-1]))


# Ahora se definirán las funciones conjugar y módulo con sus respectivas pruebas

# In[292]:


def conjugar (x):
    resultado = [x[0], x[1]*(-1)]
    return resultado


# pruebas para la función conjungar:

# In[293]:


imprimirNum(conjugar ([2,4]))


# In[294]:


imprimirNum(conjugar ([56,-2]))


# In[295]:


def modulo (x):
    resultado = (x[0]**2 + x[1]**2)**(1/2)
    if resultado != None:
        resultado = round(resultado,2)
        return resultado


# pruebas para la función modulo:

# In[296]:


print (modulo ([3,4]))


# In[297]:


print(modulo ([2,2]))


# In[298]:


print(modulo ([0,25]))


# A continuación se definirán funciones para transformar de coordenadas cartesianas a polares (llamada cPolar) y de polares 
# a cartesianas (llamada pCartesiana )

# In[299]:


def cPolar (x):
    r = (x[0]**2 + x[1]**2)**(1/2)
    tethaRadianes = math.atan(x[1]/x[0])
    tethaGrados = tethaRadianes * 180 / math.pi 
    r  = round(r, 2)
    tethaGrados = round(tethaGrados,2)
    resultado = [r,tethaGrados]
    return resultado


# Pruebas para convertir de coordenadas cartesianas a polares:

# In[300]:


print(cPolar([2,5]))


# In[301]:


print(cPolar ([56,87]))


# Para reprentar un número complejo en coordenadas polares, usando la fórmula de Euler a continuación se define la
# función imprimirPolar

# In[302]:


def imprimirPolar(x):
    str1 = "("+"i"+"·"+str(x[1])+"˚"+")"
    str2 = "e" + "^" + str1
    str3 = str(x[0])+" · "+str2
    print(str3)


# pruebas para la función imprimirPolar usando operaciones realizadas anteriormente:

# In[303]:


imprimirPolar(cPolar ([1,1]))


# In[304]:


imprimirPolar(cPolar ([56,87]))


# In[305]:


def pCartesiana (x):
    a = x[0]*math.cos(x[1])
    b = x[0]*math.sin(x[1])
    a = round(a,2)
    b = round(b,2)
    resultado = [a,b]
    return resultado


# Pruebas para convertir de coordenadas polares a cartesianas:

# In[306]:


imprimirNum(pCartesiana ([5,38]))


# In[307]:


imprimirNum(pCartesiana([50,(math.pi)/6]))


# Por ultimo se definira la funcion faseComplejo : 

# In[308]:


def faseComplejo(x):
    if x[0] >= 0 and x[1] > 0:
        tetha = (x[1]*180) / math.pi
        
    elif x[0] < 0 and x[1] > 0:
        angulo = math.atan(x[1])
        angulo = (angulo * 180)/math.pi
        tetha =  180 - angulo 
    
    elif x[0] < 0 and x[1] < 0:
        a = x[1]*(-1)
        angulo = math.atan(a)
        angulo = (angulo * 180)/math.pi
        tetha =  270 - angulo
        
    elif x[0] >= 0 and x[1] < 0:
        angulo = math.atan(x[1]*(-1))
        angulo = (angulo * 180)/math.pi
        tetha = 360 - angulo
        
    return tetha
    


# Ahora se añadirá una función para imprimir la fase del número complejo y además la función gRadianes
# para convertir grados a radiames y rGrados para el proceso inverso, que serán utiles para el manejo de 
# otras funciones

# In[309]:


def imprimirFase(x):
    radianes = gRadianes(x)
    radianes = round(radianes, 2)
    print(str(radianes)+" Rad")
    print(str(x)+"˚")


# In[310]:


def gRadianes (x):
    return x*math.pi/180


# In[311]:


def rGrados (x):
    return x*math.pi/180


# Pruebas para la función faseComplejo

# In[312]:


imprimirFase(faseComplejo([1,math.sqrt(3)*(-1)]))


# In[313]:


imprimirFase(faseComplejo([0,math.pi/2]))


# In[315]:


imprimirFase(faseComplejo([1,-1]))






