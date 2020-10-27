import networkx as nx
import numpy as np


G=nx.read_edgelist('facebook_combined.txt')  #here we edges because our downloaded data in edges
#G=nx.read_edgelist('edge1.txt')  #here we edges because our downloaded data in edges

N=list(G.nodes())
print(G)
spll=[]

for u in N:
    for v in N:
       if u!=v:
           l=nx.shortest_path_length(G,u,v)
           #print(u,'&',v,':',l)
           spll.append(l)
print(spll)           
min_spl=min(spll)
max_spl=max(spll)
avg_spl=np.average(spll)

print("Minimum shortest path",min_spl)
print("Maximum shortest path",max_spl) 
print("Average shortest path",avg_spl)  #its maximum value is 6  
# hence this is called six degree of separation    
