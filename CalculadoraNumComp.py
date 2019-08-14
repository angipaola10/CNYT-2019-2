#!/usr/bin/env python
# coding: utf-8

# Importacion de librerias 

# In[77]:


import numpy as np 
import matplotlib.pyplot as plt
import math 


# Función para imprimir numeros complejos ( imprimirNum )

# In[48]:


def imprimirNum (num):
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

# In[9]:


imprimirNum ([1,2])
imprimirNum ([0,0])
imprimirNum ([0,2])
imprimirNum ([2,0]) 


# A continuación se definen las funciones sumar, restar y multiplicar, las cuales reciben 2 números complejos representados en un arreglo. Ejemplo:
# 2 + 4i = [2,4]
# 8i = [0,8]
# 4 = [4,0]

# In[54]:


def sumar (x , y):
    resultado  = [ (x[0]+y[0]) , (x[1]+y[1]) ]
    imprimirNum(resultado)


# Pruebas para la función sumar:

# In[23]:


sumar ([1,2],[5,9])


# In[24]:


sumar([-8,7],[7,-6])


# In[25]:


sumar ([0,1],[0,-1])


# In[52]:


def restar (x , y):
    resultado  = [ (x[0]-y[0]) , (x[1]-y[1]) ]
    imprimirNum(resultado)


# Pruebas para la función restar:

# In[56]:


restar ([1,2],[5,9])


# In[57]:


restar ([-8,7],[7,-6])


# In[58]:


restar ([0,1],[0,-1])


# In[59]:


def multiplicar (x , y):
    resultado = [ (x[0]*y[0] - x[1]*y[1]) , (x[0]*y[1] + x[1]*y[0]) ] 
    imprimirNum(resultado)


# In[ ]:


Pruebas para la función multiplicar: 


# In[60]:


multiplicar ([-3,-1],[1,-2])


# In[61]:


multiplicar ([3,-2],[1,2])


# In[62]:


multiplicar ([0,5],[5,0])


# In[63]:


def dividir (x , y):
    if y[0] == 0 and y[1] == 0:
        print ("No es posible realizar esta división")
    else:
        temp = y[0]**2 + y[1]**2 
        temp1 = x[0]*y[0] + x[1]*y[1]
        temp2 = y[0]*x[1] - x[0]*y[1]
        resultado = [temp1/temp , temp2/temp]   
        imprimirNum(resultado)


# pruebas para la función dividir:

# In[64]:


dividir ([-2,1],[1,2])


# In[65]:


dividir ([5,4],[0,0])


# In[66]:


dividir ([0,3],[-1,-1])


# Ahora se definirán las funciones conjugar y módulo con sus respectivas pruebas 

# In[69]:


def conjugar (x):
    resultado = [x[0], x[1]*(-1)]
    imprimirNum(resultado)


# pruebas par la función conjugar:

# In[70]:


conjugar ([2,4])


# In[72]:


conjugar ([56,-2])


# In[73]:


def modulo (x):
    resultado = (x[0]**2 + x[1]**2)**(1/2)
    print(resultado)


# In[74]:


modulo ([3,4])


# In[75]:


modulo ([2,2])


# In[76]:


modulo ([0,25])


# In[ ]:


A continuación se definirán funciones para transformar de coordenadas cartesianas a polares (llamada cPolar) y de polares 
a cartesianas (llamada pCartesiana )


# In[114]:


def cPolar (x):
    r = (x[0]**2 + x[1]**2)**(1/2)
    tethaRadianes = math.atan(x[1]/x[0])
    tethaGrados = tethaRadianes * 180 / math.pi 
    resultado = [r,tethaGrados]
    imprimirNum (resultado)


# Pruebas para convertir de coordenadas cartesianas a polares:

# In[115]:


cPolar([2,5])


# In[116]:


cPolar ([56,87])


# In[117]:


cPolar ([1,1])


# In[118]:


def pCartesiana (x):
    a = x[0]*math.cos(x[1])
    b = x[0]*math.sen(x[1])
    resultado = [a,b]
    imprimirNum (resultado)


# In[ ]:


pCartesiana ([5,38,])

