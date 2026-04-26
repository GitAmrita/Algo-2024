from typing import List
from collections import deque
def alienDictionary(words: List[str]) -> str: 
    prefix = set()
    def find_tuple(word1, word2):
        word = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(word):
            if word1[i] != word2[i]:
                return (word1[i], word2[i])
        if len(word1) > len(word2):
            return "invalid" # invalid abc ab
        else:
            return None # valid but no ordering ab abc
    
    def build_graph(prefix, unique_chars):
        graph = {c: [] for c in unique_chars}
        for node, edge in prefix:
            graph[node].append(edge)
        return graph

    def topological_sort(graph):
        result = ""
        indegree = deque()
        edge_dict = {} 
        for edges in graph.values():
            for edge in edges:
                if edge in edge_dict.keys():
                    edge_dict[edge] += 1
                else:
                    edge_dict[edge] = 1

        for node in graph.keys():
            if node not in edge_dict:
                indegree.append(node)
        while indegree:
            n = indegree.popleft()
            result += n
            edges = graph.get(n, [])
            for e in edges:
                edge_dict[e] -= 1
                if edge_dict[e] == 0:
                    indegree.append(e)
        return result
    for i in range(1, len(words)):
        word1 = words[i - 1]
        word2 = words[i]
        tuples = find_tuple(word1, word2)
        if tuples == "invalid":
            return ""
        if tuples:
            prefix.add(tuples)
    unique_chars = {c for word in words for c in word}
    graph = build_graph(prefix, unique_chars)
    topo_sorted = topological_sort(graph)
    if len(topo_sorted) == len(unique_chars):
        return topo_sorted
    else:
        return ''