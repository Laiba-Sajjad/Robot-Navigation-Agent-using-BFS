import numpy as np
from collections import deque
import copy
import time
#import pandas as pd
t=time.time()
class index:
    x=0
    y=0
    cost=0
    path=[]

def next_into_stack(maxr,maxc,arr,ind=index(),st=deque(),vis=deque()):
    index_to_app=index()

    #up
    index_to_app.y=ind.y
    index_to_app.x=ind.x-1

    if index_to_app.x>=0 and not check_if_visited(index_to_app,vis):
        #print("pushing :x=",index_to_app.x," y=",index_to_app.y,"\n")
        if arr[index_to_app.x][index_to_app.y]!='1':
            index_to_app.cost=ind.cost+1
            #index_to_app.path.clear()
            index_to_app.path=copy.copy(current.path)
            index_to_app.path.append(copy.copy((index_to_app.x,index_to_app.y)))
            #index_to_app.path=copy.copy(ind.path)
            #index_to_app.path=list.append([str(ind.x),str(ind.y)])
            st.append(copy.copy(index_to_app))
    #Dup
    index_to_app.y=ind.y+1
    index_to_app.x=ind.x-1

    if index_to_app.x>=0 and index_to_app.y<maxc  and not check_if_visited(index_to_app,vis):
        #print("pushing :x=",index_to_app.x," y=",index_to_app.y,"\n")
        if arr[index_to_app.x][index_to_app.y]!='1':
            index_to_app.cost=ind.cost+2
            #index_to_app.path.clear()
            index_to_app.path=copy.copy(current.path)
            index_to_app.path.append(copy.copy((index_to_app.x,index_to_app.y)))
            #index_to_app.path=copy.copy(ind.path)
            #index_to_app.path=list.append([str(ind.x),str(ind.y)])
            st.append(copy.copy(index_to_app))
    index_to_app.y=ind.y+1#right
    index_to_app.x=ind.x
    if index_to_app.y<maxc and not check_if_visited(index_to_app,vis):
        #print("pushing :x=",index_to_app.x," y=",index_to_app.y,"\n")
        if arr[index_to_app.x][index_to_app.y]!='1':
            index_to_app.cost=ind.cost+3
            #index_to_app.path.clear()
            index_to_app.path=copy.copy(current.path)
            index_to_app.path.append(copy.copy((index_to_app.x,index_to_app.y)))
            #index_to_app.path=copy.copy(ind.path)
            #index_to_app.path=list.append([str(ind.x),str(ind.y)])
            st.append(copy.copy(index_to_app))

def check_if_visited(ind=index(),visit=deque()):
    for i in range(len(visit)):
        check=visit[i]
        if ind.x==check.x and ind.y==check.y:
            return True
    return False

f=open('grid.txt','r')

sl=f.readline()
stl=f.readline()
gl=f.readline()
grid=f.read().replace(' ', '')

grid=grid.split('\n')
#print("grid is ",grid)
for i in range(len(grid)):
    grid[i]=grid[i].replace('\t',',')
#f.close()
size=index()
start=index()
goal=index()
#arr=list()
ind=0
for item in grid:
    grid[ind]=item.split(',')
    ind=ind+1

arr=np.array(grid)
print(arr)
size.x,size.y=sl.split(' ')
start.x,start.y=(stl.split(' '))
goal.x,goal.y=(gl.split(' '))
# rev_arr=arr[::-1]
# print(rev_arr)
#list.append()
size.x=int(size.x)
size.y=int(size.y)
start.x=int(start.x)
start.y=int(start.y)
goal.x=int(goal.x)
goal.y=int(goal.y)
print("goal is",goal.x,goal.y)
print("start is ", start.x,start.y)
start.x=13-start.x
goal.x=13-goal.x
stack=deque()
visited=deque()
current=copy.copy(start)
value=0
maxr=len(arr)
maxc=len(arr[0])
count=1
arr[goal.x][goal.y]='G'
current.path.append((start.x,start.y))
while not(current.x == goal.x and current.y == goal.y):
   # print("current index is :",current.x,current.y)
   #  arr[current.x][current.y]='#'

    visited.append(copy.copy(current))
    next_into_stack(maxr,maxc,arr,current,stack,visited)
    current=stack.popleft()
    count=count+1
    #if count>10000:
    #    break
    # print("poped :x=",current.x," y=",current.y,"\n")


for i in range(len(current.path)):
    x1=current.path[i][0]
    y1=current.path[i][1]
    arr[x1][y1]='#'
arr[goal.x][goal.y]='G'
arr[start.x][start.y]='S'
# list(set(current.path))

print(arr)

print("cost is :",current.cost)
# print("path is ",current.path)

print("time took:",time.time()-t)

