# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:18:57 2024

@author: prestamour
"""

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.m=0
        
    def showPoint(self):
        print(f"the point is: ({self.x},{self.y})")
        
        

class Stack():
    def __init_(self):
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
                element.x,element2.x = swap(element.x > element2.x)
    return lista

def slopeSort(lista):
    for element in range(len(lista)):
        for element2 in range(len(lista)):
            if lista[element].m > lista[element2].m:
                element.m,element2.m = swap(element.m > element2.m)
    return lista

def productoCruz(v1,v2):
    return (v1.x*v2.y) - (v2.x*v1.y)
        
def graham(Points):
    #Ordenar los puntos 
    Points = hSort(Points)
    P0 = Points[0]
    
    for point in Points:
        point.m = (P0.y - point.y)/(P0.x - point.x)
        
    Points = slopeSort(Points)
    
    stako = Stack()
    for i in range(3):
        stako.add(Points[i])
    
    for i in range(3,len(Points)):
        while productoCruz(Points[i-1],Points[i]) and productoCruz(Points[i-1],Points[i]) and productoCruz(Points[i-1],Points[i]) 
    
    
    
    
    