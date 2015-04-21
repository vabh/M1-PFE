import operator
import json
import pprint
import networkx as nx
import matplotlib.pyplot as plt

filename = 'tweet_ids_16clinton_hashtags.txt'
# filename = 'hashtest.txt'
reqday = 14

G = nx.Graph()

hashtag_list = {}
with open(filename, 'r') as f:
	for line in f:
		l = json.loads(line)
		
		hashtags = l['hashtags']
		node1 = hashtags[0]

		for h in hashtags:			

			if node1 in hashtag_list:
				
				if h not in hashtag_list[node1]:

					hashtag_list[node1].append(h)
					if h not in hashtag_list:
						hashtag_list[h] = []

					G.add_node(h)
					G.add_edge(h, node1)
			else:
				hashtag_list[node1] = []
				G.add_node(node1)
			

# print hashtag_list
pprint.pprint(hashtag_list)

# nx.draw(G)
# plt.show()