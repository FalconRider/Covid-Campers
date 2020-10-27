
 Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



#  STORY NOTES:                                ***

#  PROCECT NAME:  CAMPERS


import datetime
import networkx as nx
import dwave_networkx as dnx

import matplotlib.pyplot as plt
from dwave.system.samplers import DWaveSampler

from dwave.system.composites import EmbeddingComposite


sampler = EmbeddingComposite(DWaveSampler())

#CONSTRAINTS

G = nx.Graph()

                                                    
G.add_edges_from [(1, 2 ),(2, 3 ),(3, 4 ),(4, 5 ),(5, 6 ),(6, 7 ),(7, 8 ),(8, 9 ),(9, 10 ),(10, 11 ),(11, 12 ),(12, 13 ),(13, 14 ),(14, 15 ),(15, 16 ),(16, 17 ),(17, 18 ),(18, 19 ),(19, 20 ),(20, 21 ),(21, 1 ), (10,10), (11,11)  ]

                
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)




                  

#   adjust your  printout requirments ---------------REPORT---------***
timestamp = datetime.datetime.now()
print(" ")
print("--------------------------------------------------------------")
print("Campers")
print("Run                             ",timestamp)
print("--------------------------------------------------------------")
print("Total original sites       21-2 = 19 "),
print("Maximum  set size     ", len (S))
print("Missed ", 19 -len(S))
print("Assignments in Nodes this run   ",S)
print("--------------------------------------------------------------")
print(" ")
k =G.subgraph(S)
notS =list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(k,pos=pos)
nx.draw(othersubgraph,pos=pos,node_color ='b')
plt.show()
