import numpy as np 
import random
from matplotlib import pyplot as plt
def createSwarm(n):
    xpos = np.random.uniform(0,1,n)
    swarm = []
    for i in range(n):
            swarm.append([xpos[i],random.getrandbits(1)])
    return swarm
# def testSwarm():
#     return [[0.98,1],[0.99,1],[0.01,0], [0.02,0]]

def sim(n, timesteps, r):

    
    swarm = createSwarm(n)
    swarmRange=range(0,n)
    
    lefties=[]
    for i in range(0,timesteps):

        leftGoers=0 
        for j in swarmRange:
            if swarm[j][1]:
                 leftGoers+=1  
        lefties.append(leftGoers)

        

        neighbourhood = getNeighbourhood(swarm, swarmRange)
        
        switchers = getSwitchers(neighbourhood, swarm, swarmRange)
        
        
     
        for j in switchers:
            swarm[j][1] = 1-swarm[j][1]
       
        
        print(leftGoers)

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
            #half=np.floor(len(neighbourhood[i])/2)
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
                
                if(j!=i):
                    if(abs(swarm[i][0] - swarm[j][0]) < 0.045):
                    
                        ncount.append(j)
            
        elif(swarm[i][0] <= 0.045):

            for j in swarmRange:
                if(j!=i):

                    xi = swarm[i][0]

                    xj = swarm[j][0]

                    dist1 = xi - xj

                    dist2 = 1-xi - xj

                    if(abs(dist1) < 0.045 or abs(dist2) < 0.045):

                        ncount.append(j) 

        elif(swarm[i][0] >= 0.955):

            for j in swarmRange:
                if(j!=i):
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

n = 20
timesteps=500
r = 0.045
x = []
for i in range(timesteps): 
    x.append(i)
plt.xlim(0,timesteps)
plt.ylim(0,20)
plt.plot(x,sim(n, timesteps, r))


plt.show()


 
