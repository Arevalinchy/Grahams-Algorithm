# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:18:57 2024

@author: prestamour
"""
import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.name=name
        self.m=0
        
    def __str__(self):
        return self.name
    def showPoint(self):
        print(f"the point is: ({self.x},{self.y})")
        
      
def cross(P0,P1,P2): #Producto cruz con respecto a un origen común
    return (P1.x - P0.x) * (P2.y - P0.y) - (P2.x - P0.x) * (P1.y - P0.y)


def productoCruz(P1,P2): #Producto cruz con respecto al origen
    return (P1.x*P2.y) - (P2.x*P1.y)

def giro(P0,P1,P2):
    if cross(P0,P1,P2)>0:
        print(f"{P1} gira en sentido horario con respecto a {P2} con {P0} como origen")
    elif cross(P0,P1,P2)<0:
        print(f"{P1} gira en sentido anti-horario con respecto a {P2} con {P0} como origen" )
    else:
        print(f"{P1},{P2} y {P0} son colineales")


        
Points = [Point(0, 0, "P0"),Point(1, 0, "P1"),Point(0, 1, "P2"),Point(2, 3, "P3"),Point(4, 1, "P4"),Point(0, 2, "P5"),Point(3, 2, "P6"),Point(5, 2, "P7"),Point(7, 2, "P8")]

#Plotting example
P0 = Points[0]
P1 = Points[1]
P2 = Points[2]
#plt.figure(figsize=(2,2))
#plt.arrow(P0.x, P0.y, P1.x-P0.x,P1.y-P0.y, head_width=0.05,
          #head_length=0.05,color="blue", label=f"{P1}-{P0}")

#plt.arrow(P0.x, P0.y, P2.x-P0.x,P2.y-P0.y, head_width=0.05,
          #head_length=0.05,color="red", label=f"{P2}-{P0}")

#plt.legend()
#plt.show()     
        
def rotacion(P0,P1,P2):
    giro(P0,P1,P2)       
    plt.figure(figsize=(4,4))
    plt.arrow(P0.x, P0.y, P1.x-P0.x,P1.y-P0.y, head_width=0.05,
              head_length=0.05,color="blue", label=f"{P1}-{P0}")

    plt.arrow(P0.x, P0.y, P2.x-P0.x,P2.y-P0.y, head_width=0.05,
              head_length=0.05,color="red", label=f"{P2}-{P0}")

    plt.legend()
    plt.show()    
      
#rotacion(P0,P1,P2)
        
def turn(P0,P1,P2):
    if cross(P0,P1,P2)>0:
        print(f"En {P1} se hace un giro en sentido anti-horario")
    elif cross(P0,P1,P2)<0:
        print(f"En {P1} se hace un giro en sentido horario" )
    else:
        print(f"{P1},{P2} y {P0} son colineales")

def giraen(P0,P1,P2):
    turn(P0,P1,P2)
    plt.figure(figsize=(4,4))
    plt.arrow(P0.x, P0.y, P1.x-P0.x,P1.y-P0.y, head_width=0.05,
              head_length=0.05,color="blue", label=f"{P1}-{P0}")

    plt.arrow(P1.x, P1.y, P2.x-P1.x,P2.y-P1.y, head_width=0.05,
              head_length=0.05,color="red", label=f"{P2}-{P0}")

    plt.legend()
    plt.show()    
      
giraen(P0,P1,P2)


class Stack:
    def __init__(self):
        self.stack = list()
    def empty(self):
        return len(self.stack) > 0
    def size(self):
        return len(self.stack) 
    def add(self,element):
        self.stack.append(element)
    def pop(self):
        erasable = self.size()
        self.stack.pop(erasable)

            

        
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def hSort(lista):
    for element in range(len(lista)):
        for element2 in range(len(lista)):
            if lista[element].x > lista[element2].x:
                lista[element].x,lista[element2].x = swap(lista[element].x, lista[element2].x)
    return lista

def slopeSort(lista):
    for element in range(len(lista)):
        for element2 in range(len(lista)):
            if lista[element].m > lista[element2].m:
                lista[element].x,lista[element2].x = swap(lista[element].x, lista[element2].x)
    return lista



def graham(Points):
    #Ordenar los puntos 
    Points = hSort(Points)
    P0 = Points[0]
    
    #Slope
    for point in Points:
        if (P0.x - point.x)!=0:
            point.m = (P0.y - point.y)/(P0.x - point.x)
        
    Points = slopeSort(Points)
    
    stako = Stack()
    for i in range(3):
        stako.add(Points[i])
    
    
    for i in range(3,len(Points)):
        while cross(Points[i-1],Points[i-2],Points[i-1]) > 1:
            stako.pop()
        stako.add(Points[i])    
        
    return stako


    
    
    


#convexHull = graham(Points)
    
#print(f"{convexHull.stack}")
