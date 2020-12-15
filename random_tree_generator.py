#https://www.geeksforgeeks.org/random-tree-generator-using-prufer-sequence-with-examples/

import numpy as np
#use np.random.choice to generate prufer

class randomtree():
    def __init__(self,n):
        self.edges=[]
        self.node=n
        self.prufer=[]

    #generate prufer seq: size n-2, value [1..n]
    def prufer_gen(self):
        self.prufer=np.random.choice(range(1,self.node+1),self.node-2,replace=True)
        print('prufer',self.prufer)


    def tree_gen(self):
        self.prufer_gen()

        nodes=list(range(1,self.node+1))
        #count for [0,..,n] in prufer seq, index 0 is not used
        count_node=[0]*(self.node+1)
        for i in self.prufer:
            count_node[i]+=1
        
        #for each one node1 in prufer, pick a node2 from [1..n] with property count[node2]==0.
        #dont pick nodes with count[node2]>0, such nodes in prufer will pick other nodes later, and cycle exists.
        #once node1 finishes pick： edges.append((node1,node2))
        ##its count-1: count_node[node1]-=1
        ##and the pick node cant be picked any more :count_node[node2]=-1
        ##node1 only pick one node: break
        for node1 in self.prufer:
            print ('count_node',count_node)
            for node2 in nodes:
                if count_node[node2]==0:
                    count_node[node2]=-1
                    self.edges.append((node1,node2))
                    print('node1,node2',node1,node2)
                    count_node[node1]-=1
                    break
        print ('count_node',count_node)

        #the last edge,property:
        #the remaining node with count[node]==0
        #only n-2 such nodes not picked
        #they are busy picking others in 1st step 
        first=0
        node1=0
        node2=0
        for node in nodes:
            if  count_node[node]==0:
                if first==0:
                    node1=node
                    first=1
                else:
                    node2=node
                    self.edges.append((node1,node2))
                    print('node1,node2',node1,node2)

tree=randomtree(5)
tree.tree_gen()
print(tree.prufer)
print(tree.edges)