# libraries 导入模块
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import xlrd

inputFile = "C:\\Users\\64864\\Downloads\\修士卒論\\M2四月発表\\Flickr_correct\\2010-2018.xls"
data = pd.read_excel(inputFile, sheet_name="格网节点", encoding="utf-8")
data2 = xlrd.open_workbook(r'C:\\Users\\64864\\Downloads\\修士卒論\\M2四月発表\\Flickr_correct\\格网排序.xlsx')

# 获取第2个sheet页的起止点
sheet1 = data2.sheets()[1]
# 获取总行数
rows = sheet1.nrows
data3 = []
for i in range(1, rows):
    x = int(sheet1.cell_value(i, 0))
    y = int(sheet1.cell_value(i, 1))
    z = int(sheet1.cell_value(i, 2))
    data3.append((x, y, z))
print (data3)

network = nx.DiGraph()
network.add_nodes_from(data["pythonID"], weight=data["照片数量"])
network.add_weighted_edges_from(data3)

# 获取第3个sheet页的坐标
sheet3 = data2.sheets()[2]
# 获取总行数
rows = sheet3.nrows
pos = []
for i in range(1, rows):
    m = float(sheet3.cell_value(i, 6))
    n = float(sheet3.cell_value(i, 7))
    pos.append((m, n))
print (pos)

nodeSize = list(nx.get_node_attributes(network, 'weight').values())
fig, ax = plt.subplots()
nx.draw_networkx_nodes(network, pos, with_labels=False, node_size=nodeSize[1],
                       node_color=list(nx.get_node_attributes(network, 'weight')[1]), cmap=plt.cm.get_cmap('Wistia'),
                       alpha=1, ax=ax)
nx.draw_networkx_edges(network, pos, width=0.2, alpha=0.2, edge_color='k', arrows=False)
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()

# 次数中心性(Degree Centrality)
dc1 = nx.in_degree_centrality(network)
result1 = (max(dc1.values()) - min(dc1.values())) * 0.5 + min(dc1.values())


def filter_dc(data):
    print(data.items())
    return {k: v for k, v in data.items() if v > result1}


filter_dc(dc1)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(network, pos, with_labels=False, node_size=1, node_color='silver')
nx.draw_networkx_edges(network, pos, width=0.1, alpha=0.75, edge_color='k', arrows=False)
nx.draw_networkx_nodes(dict(filter_dc(dc1)), pos, with_labels=False, node_size=10, node_color='crimson')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
plt.hist(dc1.values(), bins=10)
plt.xlabel('in_Degree Centrality')
plt.ylabel('frequency')
plt.show()

dc2 = nx.out_degree_centrality(network)
result2 = (max(dc2.values()) - min(dc2.values())) * 0.5 + min(dc2.values())


def filter_dc(data):
    print(data.items())
    return {k: v for k, v in data.items() if v > result2}


filter_dc(dc2)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(network, pos, with_labels=False, node_size=1, node_color='silver')
nx.draw_networkx_edges(network, pos, width=0.1, alpha=0.75, edge_color='k', arrows=False)
nx.draw_networkx_nodes(dict(filter_dc(dc2)), pos, with_labels=False, node_size=10, node_color='crimson')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
plt.hist(dc2.values(), bins=10)
plt.xlabel('out_Degree Centrality')
plt.ylabel('frequency')
plt.show()

# 近接中心性(Closeness Centrality)
cc = nx.closeness_centrality(network)
result3 = (max(cc.values()) - min(cc.values())) * 0.8 + min(cc.values())


def filter_dc(data):
    print(data.items())
    return {k: v for k, v in data.items() if v > result3}


filter_dc(cc)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(network, pos, with_labels=False, node_size=1, node_color='silver')
nx.draw_networkx_edges(network, pos, width=0.1, alpha=0.75, edge_color='k', arrows=False)
nx.draw_networkx_nodes(dict(filter_dc(cc)), pos, with_labels=False, node_size=10, node_color='crimson')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
plt.hist(cc.values(), bins=10)
plt.xlabel('Closeness Centrality')
plt.ylabel('frequency')
plt.show()

# 媒介中心性(Betweenness Centrality)
bc = nx.betweenness_centrality(network)
result4 = (max(bc.values()) - min(bc.values())) * 0.5 + min(bc.values())


def filter_dc(data):
    print(data.items())
    return {k: v for k, v in data.items() if v > result4}


filter_dc(bc)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(network, pos, with_labels=False, node_size=1, node_color='silver')
nx.draw_networkx_edges(network, pos, width=0.1, alpha=0.75, edge_color='k', arrows=False)
nx.draw_networkx_nodes(dict(filter_dc(bc)), pos, with_labels=False, node_size=10, node_color='crimson')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
plt.hist(bc.values(), bins=10)
plt.xlabel('Betweenness Centrality')
plt.ylabel('frequency')
plt.show()

# クラスター係数(clustering coefficient)
ce = nx.clustering(network)
print(ce)
plt.hist(ce.values(), color="crimson", bins=10, histtype="barstacked", )
plt.xlabel('Clustering Coefficient')
plt.ylabel('frequency')
plt.show()
print("---------------------")

# ストラクチャーホール(structural holes)
sh = nx.algorithms.triads.triadic_census(network)
print(sh)
es = nx.algorithms.structuralholes.effective_size(network)
print(es)
value_es = list(es.values())
cons = nx.algorithms.structuralholes.constraint(network)
print(cons)
degree = list(zip(*(network.degree())))
degree2 = degree[1]
print(degree2)
efficiency = [a / b for a, b in zip(value_es, degree2)]
print(efficiency)
