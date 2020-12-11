import numpy as np 
import random
from matplotlib import pyplot as plt
import concurrent.futures
from itertools import repeat



def createSwarm(n):
    xpos = np.random.uniform(0,1,n)
    swarm = []
    for i in range(n):
            swarm.append([xpos[i],random.getrandbits(1)])
    return swarm
# def testSwarm():
#     return [[0.98,1],[0.99,1],[0.01,0], [0.02,0]]

def sim(n, timesteps, r, swarm):

    
    
    swarmRange=range(0,n)
    
    lefties=[]
    leftChanges=[]
    for i in range(0,timesteps):

        leftGoers=0 
        for j in swarmRange:
            if swarm[j][1]:
                 leftGoers+=1  
        lefties.append(leftGoers)

        

        neighbourhood = getNeighbourhood(swarm, swarmRange)
        
        switchers = getSwitchers(neighbourhood, swarm, swarmRange)
        
        
        switchedLeft = 0
        for j in switchers:
            swarm[j][1] = 1-swarm[j][1]

        leftChanges.append(switchedLeft)

        for j in swarmRange:
            
            #move swarm         

            #right
            if(swarm[j][1]):

                if(swarm[j][0] == 1):

                    swarm[j][0] == 0

                swarm[j][0] += 0.001
                
            #left
            else:

                if(swarm[j][0] == 0):

                    swarm[j][0] == 1

                swarm[j][0] -= 0.001
    return lefties

def getSwitchers(neighbourhood, swarm, swarmRange):
    #switch?
    switchers = []
    
    for i in swarmRange:
        p=np.random.uniform(0,100,1)[0]
        if p <= 0.15:
            switchers.append(i)

        else:
            count = 0
            for n in neighbourhood[i]:

                if(swarm[n][1]!=swarm[i][1]):
                    count+=1
            
            half=len(neighbourhood[i])/2
            if (count>half):
                switchers.append(i)
    return switchers

def getNeighbourhood(swarm, swarmRange):

    neighbourhood=[]

    for i in swarmRange:

        ncount=[]

        if(swarm[i][0] > 0.045 and swarm[i][0] < 0.955):

            for j in swarmRange:
                
                
                if(abs(swarm[i][0] - swarm[j][0]) < 0.045):
                
                    ncount.append(j)
            
        elif(swarm[i][0] <= 0.045):

            for j in swarmRange:

                xi = swarm[i][0]

                xj = swarm[j][0]

                dist1 = xi - xj

                dist2 = 1-xi - xj

                if(abs(dist1) < 0.045 or abs(dist2) < 0.045):

                    ncount.append(j) 

        elif(swarm[i][0] >= 0.955):

            for j in swarmRange:
                xi = swarm[i][0]
                xj = swarm[j][0]

                dist1 =abs(xi - xj)

                dist2 = abs(xi - 1 - xj)

                if(dist1 < 0.045): 
                
                    ncount.append(j) 

                elif (dist2< 0.045):

                    ncount.append(j) 

        neighbourhood.append(ncount)
    return  neighbourhood






def task1a():
    n = 20
    timesteps=500
    r = 0.045
    x = []
    for i in range(timesteps): 
        x.append(i)
    plt.xlim(0,timesteps)
    plt.ylim(0,20)
    plt.plot(x,sim(n, timesteps, r, createSwarm(n)))
    plt.show()
 




def task1b():
    n = 20
    timesteps=500
    r = 0.045
    a = [0]*20
    lefties=[]
    for i in range(0,1000):
        lefties=sim(n, timesteps, r, createSwarm(n))
        for i in range(0, len(lefties)-1):
            change = lefties[i+1]-lefties[i]
            a[change]+=1
    for i in range(0,20):
        a[i]=a[i]

    
    x = []
    for i in range(20): 
        x.append(i)
    plt.xlim(0,20)
    #plt.ylim(0,20)
    plt.scatter(x,a)
    plt.show()

def task1c():
    n = 20
    timesteps=500
    r = 0.045
    a = [0]*20
    m = [0]*20
    lefties=[]
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        lefties = pool.map(sim(repeat(n), repeat(timesteps), repeat(r), repeat(createSwarm(n))))
    end = time.time()

    print("oneD time needed in parallel: ")
    print(end - start)
    for i in range(0, len(lefties)-1):
        change = lefties[i+1]-lefties[i]
        m[lefties[i]]+=1
        a[change]+=1
        a[i]=a[i]
    m[lefties[len(lefties)-1]]+=1

    for i in range(0,20):
        m[i]=m[i]/1000
        a[i]=a[i]/1000

    
    x = []
    for i in range(20): 
        x.append(i)
    plt.xlim(0,20)
    #plt.ylim(0,20)
    plt.scatter(x,a,m)
    plt.show()



if __name__ == "__main__":
    task1a()
