import matplotlib.pyplot as plt
import numpy as np

def graph(x,y,label,title):
    for ypts,lab in zip(y,label):
        plt.plot(x,ypts,label=lab)
    plt.title(title)
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    plt.legend()
    
    plt.axvline(0,color="black")
    plt.axhline(0,color="black")
    plt.show()
def addpts(X,Y):
    for x,y in zip(X,Y):
        plt.plot(x,y,marker='o',color='black')
    
