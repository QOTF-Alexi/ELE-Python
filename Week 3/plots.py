import numpy as np
import matplotlib.pyplot as plt

def sincos():
    x = np.linspace(0,4*np.pi,200)
    s = np.sin(x)
    c = np.cos(x)

    fig,ax = plt.subplots()
    ax.set_title('Goniometrische functies')
    ax.set_xlabel('x in rad', rotation=0, loc='right')
    ax.set_ylabel('y', rotation=0, loc='top')
    plt.plot(x,s,'r',label='y = sin(x)')
    plt.plot(x,c,'g',label='y = cos(x)')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()
    
def meetresultaten():
    vin = 1
    vout = [0.99, 0.98, 0.87, 0.68, 0.14, 0.02]
    f = [10, 100, 1000, 1590, 10000, 100000]
    cnt = 0
    Adblist = list()
    
    while len(vout)>cnt:
        Adb = 20*np.log10(vout[cnt]/vin)
        cnt=cnt+1
        Adblist.append(Adb)
        
    fig,ax = plt.subplots()
    ax.set_title('Passief LDL met R=100 en C=1uF')
    ax.set_xlabel('Frequentie [Hz]')
    ax.set_ylabel('Versterkingsfactor [dB]')
    plt.xscale('log')
    plt.grid(which='both', ls='-')
    plt.plot(f, Adblist, 'rx')
    plt.show()
        
meetresultaten()