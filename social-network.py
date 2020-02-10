## Networking with Graphs in Python
import networkx as nx
import matplotlib

G_symmetric = nx.Graph()
G_symmetric.add_edge('Saul Wiggin', 'Brad Pitt')
G_symmetric.add_edge('Saul Wiggin','Aamir Khan')
G_symmetric.add_edge('Brad Pitt','Akshay Kumar')
G_symmetric.add_edge('Amitabh Bachchan','Dev Anand')
G_symmetric.add_edge('Abhishek Bachchan','Aamir Khan')
G_symmetric.add_edge('Abhishek Bachchan','Akshay Kumar')
G_symmetric.add_edge('Abhishek Bachchan','Dev Anand')
G_symmetric.add_edge('Dev Anand','Aamir Khan')

nx.degree(G_symmetric, 'Dev Anand`)
nx.average_clustering(G_symmetric)
nx.shortest_path(G_symmetric, 'Dev Anand', 'Akshay Kumar')

nx.draw_networkx(G_symmetric)

##an asymetric graph is a directional graphs

G_asymmetric = nx.DiGraph()
G_asymmetric.add_edge('A','B')
G_asymmetric.add_edge('A','D')
G_asymmetric.add_edge('C','A')
G_asymmetric.add_edge('D','E')

nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)

## a weighted network

G_weighted = nx.Graph()
G_weighted.add_edge('Amitabh Bachchan','Abhishek Bachchan', weight=25)
G_weighted.add_edge('Amitabh Bachchan','Aaamir Khan', weight=8)
G_weighted.add_edge('Amitabh Bachchan','Akshay Kumar', weight=11)
G_weighted.add_edge('Amitabh Bachchan','Dev Anand', weight=1)
G_weighted.add_edge('Abhishek Bachchan','Aaamir Khan', weight=4)
G_weighted.add_edge('Abhishek Bachchan','Akshay Kumar',weight=7)
G_weighted.add_edge('Abhishek Bachchan','Dev Anand', weight=1)
G_weighted.add_edge('Dev Anand','Aaamir Khan',weight=1)

# a relational multigraph
G = nx.MultiGraph()
G.add_edge('A','B',relation ='neighbor')
G.add_edge('A','B',relation='friend)
G.add_edge('B','C', relation='neighbor')
G.add_edge('D','C',relation='friend')
