import operator
import json
import pprint
import networkx as nx
import matplotlib.pyplot as plt

filename = 'tweet_ids_16clinton_hashtags.txt'
# filename = 'hashtest.txt'

G = nx.Graph()

# add a measure of similarity
# classify distance from topic
# weight edges by sentiment

hashtag_list = {}
frequency_list = {}

with open(filename, 'r') as f:
    for line in f:
        l = json.loads(line)

        hashtags = l['hashtags']

        # print len(hashtags)

        for i in range(0, len(hashtags)):
            tagI = hashtags[i]
            # create node entry if node not in list
            if tagI not in hashtag_list:
                hashtag_list[tagI] = []
                G.add_node(tagI)
            # print tagI.encode('utf8')
            # frequency
            if tagI in frequency_list:
                frequency_list[tagI] = frequency_list[tagI] + 1
            else:
                frequency_list[tagI] = 1

            for j in range(i + 1, len(hashtags)):
                tagJ = hashtags[j]
                # add the edge, if not present
                # print tagJ.encode('utf8')
                if tagJ not in hashtag_list[tagI]:
                    hashtag_list[tagI].append(tagJ)
                    G.add_edge(tagI, tagJ)
                    # create node entry if node not in list
                    if tagJ not in hashtag_list:
                        hashtag_list[tagJ] = []
                        G.add_node(tagJ)

# PRINT ADJ LIST
# pprint.pprint(hashtag_list)
# with open('hashtags' , 'w') as f:
# 	for key in hashtag_list.keys():
# 		f.write(key.encode('utf8'))
# 		f.write('\n')
# nx.write_gexf(G, "test.gexf")


# DEGREE
# are nodes of degree 1 connected to HASHTAG?
# degree =  G.degree();
# sorted_list = sorted(degree.items(), key=operator.itemgetter(1), reverse=True)
# with open('../data/degree.txt', 'w') as f:
# 	for i in range(0, len(degree)):
# 		print sorted_list[i][0].encode('utf8'), ', ', sorted_list[i][1]
# 		f.write(sorted_list[i][0].encode('utf8') + ', ' + str(sorted_list[i][1]))
# 		f.write('\n')


print nx.diameter(G)  # diamter = 4

# FREQUENCY
# sorted_list = sorted(frequency_list.items(), key=operator.itemgetter(1), reverse=True)
# with open('../data/frequency.txt', 'w') as f:
# 	for i in range(0, len(sorted_list)):
# 		print sorted_list[i][0].encode('utf8'), ':', sorted_list[i][1]
# 		f.write(sorted_list[i][0].encode('utf8') + ', ' + str(sorted_list[i][1]))
# 		f.write('\n')


# nx.draw(G)
# plt.show()
