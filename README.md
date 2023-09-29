## Advanced Data Structures

<p align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/MrOlivo/data-structures-python?style=for-the-badge&labelColor=363a4f&color=b7bdf8">
  <img alt="GitHub Repo contributors" src="https://img.shields.io/github/contributors/MrOlivo/data-structures-python?style=for-the-badge&labelColor=363a4f&color=a6da95">
</p>

### Introduction

**Data Structures Package** for the *Advanced Data Structures* learning unit.

It contains python implementations of Advanced Data Structures, Search Algorithms, Binary Trees and Graphs.

### Data Structures

- [x] Graph
- [x] Binary Tree

### Trees and Graphs

- [x] Havel-Hakimi
- [x] Dijkstra
- [x] Floyd-Warshall
- [x] Prim
- [x] Kruskal
- [ ] Hopcroft-Tarjan

### Tree Traversals

- [x] Depth-first search
  - [x] Preorder
  - [x] Inorder
  - [x] Postorder
- [x] Breadth-first search

## Each Algorithm in Deep

### Havel-Hakimi

Havel-Hakimi algorithm is a way to determine if a given degree sequence can be represented by a simple graph. It works by removing the largest degree vertex and subtracting one from the next largest degree until either all degrees are 0 or an invalid sequence is found.

### Dijkstra
 
Dijkstra's algorithm is a shortest path algorithm that calculates the shortest path from a single source node to all other nodes in a weighted graph. It works by maintaining a priority queue of vertices and updating the minimum distance to each vertex based on the edges and weights in the graph.

### Floyd-Warshall

The Floyd-Warshall algorithm is a dynamic programming algorithm that calculates the shortest path between all pairs of vertices in a weighted graph. It works by storing the minimum distance between each pair of vertices and updating this distance based on intermediate vertices.

### Prim

Prim's algorithm is a greedy algorithm that finds the minimum spanning tree of a weighted undirected graph. It works by starting with a single vertex and iteratively adding the shortest edge that connects to a new vertex until all vertices are included in the tree.

### Kruskal

Kruskal's algorithm is a greedy algorithm that finds the minimum spanning tree of a weighted undirected graph. It works by sorting the edges by weight and iteratively adding the next shortest edge that does not create a cycle until all vertices are included in the tree.