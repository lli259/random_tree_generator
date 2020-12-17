#input:edge(1,2).edge(2,3)

#import commands #test case 2: commmands in python2 

class tree_feature():

    def __init__(self):
        self.adj_dict={}

    def parse_nodes(self,string_input):
        #edge(1,2). to 1,2
        layer1=string_input.split('(')[1].split(')')[0]
        a,b=layer1.replace(" ", "").split(',')
        return a,b

    def adj_gen(self,lines):
        #from [edge(1,2).edge(1,3)] to adj_list
        for l in lines:
            a,b=self.parse_nodes(l)
            if a not in self.adj_dict:
                self.adj_dict[a]=[b]
            else:
                self.adj_dict[a].append(b)
            if b not in self.adj_dict:
                self.adj_dict[b]=[a]
            else:
                self.adj_dict[b].append(a)        

    
    def max_degree(self):
        #get max degree
        max_deg=0
        for k in self.adj_dict:
            if len(self.adj_dict[k]) > max_deg:
                max_deg=len(self.adj_dict[k])
        print('max degree',max_deg)
        return max_deg

    def remove_leaf_node_once(self):
        #remove_leaf_node_once
        edgenode=[]
        for k in self.adj_dict:
            if len(self.adj_dict[k]) == 1:
                edgenode.append(k)
        for k in edgenode:
            del self.adj_dict[k]
            for k2 in self.adj_dict:
                if k in self.adj_dict[k2]:
                    self.adj_dict[k2].remove(k)

    def remove_leaf_node_all(self):
        #remove_leaf_node_all
        allstep=0
        needremove=True
        while(needremove):         
            needremove=False
            for node in self.adj_dict:
                if len(self.adj_dict[node]) >2 :
                    needremove=True
                    break
            
            if needremove:
                allstep+=1
                print('before',self.adj_dict)
                self.remove_leaf_node_once()
                print('after',self.adj_dict)
        remain_nodes=[]
        for node in self.adj_dict:
            if len(self.adj_dict[node]) >0 :
                remain_nodes.append(node)
        
        print('all removing step',allstep)
        print('remain_nodes',len(remain_nodes),remain_nodes)

        return allstep,len(remain_nodes)

def test1():
    strings='edge(9, 2).edge(15, 3).edge(25, 4).edge(6, 5).edge(9, 7).edge(25, 8).edge(10, 9).edge(22, 10).edge(18, 14).edge(13, 17).edge(11, 20).edge(13, 21).edge(18, 13).edge(11, 18).edge(6, 11).edge(16, 22).edge(12, 16).edge(19, 12).edge(23, 19).edge(6, 23).edge(15, 24).edge(1, 15).edge(6, 1).edge(6, 25)'
    lines=strings.split('.')
    print(strings)
    t=tree_feature()
    t.adj_gen(lines)
    print(t.adj_dict)
    f_values=[]
    max_deg=t.max_degree()
    f_values.append(str(max_deg))
    allstep,remain_nodes=t.remove_leaf_node_all()
    f_values.append(str(allstep))
    f_values.append(str(remain_nodes))

def test2():
    '''
    lines=[]
    lines.append('edge(1,2).')
    lines.append('edge(1,3).')
    lines.append('edge(1,4).')
    lines.append('edge(2,5).')
    lines.append('edge(3,8).')
    lines.append('edge(4,9).')
    lines.append('edge(5,6).')
    lines.append('edge(5,7).')
    '''
    savefile='domainfeature.csv'
    feature_names='max_deg,remove_steps,remain_nodes'
    #python2
    instances=commands.getoutput ("ls instances/*").split("\n")

    with open(savefile,'w') as f:
        f.write("ins,"+feature_names+"\n")

    for ins in instances:
        def get_file(file_name):
            with open(file_name,'r') as f:
                lines=f.readlines()
                return lines
        lines=get_file(ins)

        t=tree_feature()
        t.adj_gen(lines)
        print(t.adj_dict)
        f_values=[]
        max_deg=t.max_degree()
        f_values.append(str(max_deg))
        allstep,remain_nodes=t.remove_leaf_node_all()
        f_values.append(str(allstep))
        f_values.append(str(remain_nodes))
        with open(savefile,'a') as f:
            f.write(ins.split("/")[1]+","+",".join(f_values)+"\n")

test1()

