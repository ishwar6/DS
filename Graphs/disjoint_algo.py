class UnionFind:

    """
        UnionFind Class to implement "QuickFind" Disjoint Set Data Structure of Graph.
        Note: N is the number of vertices in the graph.
        => When initializing a union-find constructor, we need to create an array of size N with the values
        equal to the corresponding array indices; this requires linear time.
        => Each call to find will require O(1) time since we are just accessing an element of the array at the given index.
        => Each call to union will require O(N) time because we need to traverse through the entire array
        and update the root vertices for all the vertices of the set that is going to be merged into another set.
        => The connected operation takes O(1) time since it involves the two find calls and the equality check operation.
    """

    def __init__(self, nodes) -> None:
        """
        To create a list of empty array [0,1,2,3] each representing root node of the graph. Initially they are not 
        connected to any other node, so each node is a root node of itself. 
        """
        self.root = [i for i in range(nodes)]

    def find_root(self, node):
        return self.root[node]

    def union(self, x, y) -> None:
        root_of_node_x = self.find_root(x)
        root_of_node_y = self.root[y]
        if(root_of_node_x != root_of_node_y):
            for i in range(len(self.root)):
                if(self.root[i] == root_of_node_y):
                    self.root[i] = root_of_node_x

    def is_connected(self, x, y) -> bool:
        return self.find_root(x) == self.find_root(y)

    def find_root_quick_union(self, node):
        while(node != self.root[node]):
            node = self.root[node]
        return node

    def quick_union(self, x, y) -> None:
        print("calling for", x, y)
        rootX = self.find_root_quick_union(x)
        rootY = self.find_root_quick_union(y)
        print("currently Parent root of {} and {} are".format(rootX, rootY))
        if(rootX != rootY):
            self.root[rootY] = rootX
        rootX = self.find_root_quick_union(x)
        rootY = self.find_root_quick_union(y)
        print("Finally Parent root of {} and {} are {} and {}".format(
            x, y, rootX, rootY))

    def quick_is_connected(self, x, y) -> bool:
        return self.find_root_quick_union(x) == self.find_root_quick_union(y)


def quick_union_test():
    graph_array = UnionFind(10)
    uf = graph_array

    # add elements
    uf.quick_union(1, 2)
    uf.quick_union(1, 9)
    uf.quick_union(2, 5)
    uf.quick_union(5, 6)
    uf.quick_union(5, 7)
    uf.quick_union(3, 8)
    uf.quick_union(8, 9)
    print(uf.quick_is_connected(1, 5))  # true
    print(uf.quick_is_connected(5, 7))  # true
    print(uf.quick_is_connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.quick_union(9, 4)
    print(uf.is_connected(4, 9))  # true
    print(uf.root)


def test():
    graph_array = UnionFind(10)
    uf = graph_array

    # add elements
    uf.union(1, 2)
    uf.union(1, 9)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(5, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.is_connected(1, 5))  # true
    print(uf.is_connected(5, 7))  # true
    print(uf.is_connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.is_connected(4, 9))  # true
    print(uf.root)


# quick_union_test()
# test()


# union by rank

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def test_rank():
    # Test Case
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
