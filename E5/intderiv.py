from scipy import integrate
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcolo distanza percorsa da velocità e tempo')
    parser.add_argument('-f', '--file',    action='store',      default='vel_vs_time.csv', help='File di input')
    parser.add_argument('-v', '--vel',     action='store_true',                            help='Grafico Velocità vs Tempo')
    parser.add_argument('-d', '--dist',    action='store_true',                            help='Grafico Distanza vs Tempo')
    return  parser.parse_args()
def distanza():
    args = parse_arguments()
    print(args)
    data1=pd.read_csv('/home/samu1019/MCF/MCF/E5/vel_vs_time.csv')
    if(args.vel):
        plt.plot(data1['t'],data1['v'])
        plt.show()
        
    if(args.dist):
       spazio=integrate.simpson(data1['v'],data1['t'])
       print(spazio)
       spazio_i = np.empty(0)

       for i in range(1,len(data1['v'])+1): 
        spazio_i = np.append(spazio_i, integrate.simpson(data1['v'][:i],   dx=0.5))
        print(spazio_i)
    plt.plot(data1['t'],spazio_i)
    plt.show()
if __name__ == "__main__":

    distanza()
    