import math


class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        self.nodes = []
        for i in range(0, n):  # n by n, list of vertices, then tuples of path/weight, last item is arcs leaving vertices
            self.nodes.append([])
            for x in range(0, n):
                if x == i:
                    self.nodes[i].append(0)
                else:
                    self.nodes[i].append(float("inf"))
            self.nodes[i].append(0)




    def insert_arc(self, s, d, w):
        if s >= self.order or d >= self.order: #if out of range throw error
            raise IndexError("Out of range")
        if self.nodes[s][d] == float("inf"): #if no path create one, adjust size
            self.nodes[s][self.order] += 1
            self.size += 1
        self.nodes[s][d] = w  #if path exists, update the weight

    def out_degree(self, v):
        if v >= self.order: #if out of range throw error
            raise IndexError("Out of range")
        return self.nodes[v][self.order] #if not return degrees

    def are_connected(self, s, d):
        if s >= self.order or d >= self.order: #if out of range throw error
            raise IndexError("Out of range")
        return self.nodes[s][d] != float("inf") #if path isnt weight infinity, they connected, if it is not connected

    def is_path_valid(self, path):
        for i in range(0, len(path)):
            if path[i] >= self.order: #if out of range throw error
                raise IndexError("Out of range")
        if len(path) <= 1: #if path goes to itself
            return True
        d = path[0]
        for i in range(1, len(path)): #go thru and see if possible 
            s = d
            d = path[i]
            if self.nodes[s][d] == float("inf"): #if we find inf not possible
                return False
        return True #If not return true

    def arc_weight(self, s, d):
        if s >= self.order or d >= self.order: #if out of range throw error
            raise IndexError("Out of range")
        return self.nodes[s][d] #if not return the weight

    def path_weight(self, path):
        for i in range(0, len(path)):
            if path[i] >= self.order: #if out of range throw error
                raise IndexError("Out of range")
        if len(path) <= 1: #if path goes to itself
            return 0
        weight = 0
        d = path[0]
        for i in range(1, len(path)):
            s = d
            d = path[i]
            if self.nodes[s][d] == float("inf"): #if infinity return
                return float("inf")
            weight += self.nodes[s][d] #if not keep adding weights
        return weight

    def does_path_exist(self, s, d):
        if s >= self.order or d >= self.order: #if out of range throw error
            raise IndexError("Out of range")
        return self.find_min_weight_path(s,d) != [] #if not, if the mst function can find a path, return it


    def __queue_not_empty__(self, queue): #helper function, keep going until queue isn't empty
        for i in queue:
            if i[2] == True:
                return True
        return False

    def __get_queue_min__(self, queue): #helper function, this keeps track of the best path,
        min_index = 0
        min_dist = float("inf")
        for i in range(0,len(queue)):
            if queue[i][2] and queue[i][0] <= min_dist:
                min_index = i
                min_dist = queue[i][0]
        return min_index


    def find_min_weight_path(self, s, d):
        queue = []
        for i in range(0, self.order):
            #Distance, previous vertice, in queue
            queue.append([float("inf"), float("inf"), True])
        queue[s] = [0,s,True]
        while self.__queue_not_empty__(queue):
            min_index = self.__get_queue_min__(queue)
            if queue[min_index][0] == float("inf"): #if path doesn't exist return empty
                return []

            for i in range(0, self.order):
                if self.nodes[min_index][i] != float("inf"): #as long as not infinity, find shortest path

                    possible_dist_to_i = queue[min_index][0] + self.nodes[min_index][i]

                    if i == d: #If we find the best path, return it
                        #Shortest path found
                        path = [i]
                        prev = min_index
                        while prev != s and prev != float("inf"):
                            path.append(prev)
                            prev = queue[int(prev)][1]
                        path.append(s)
                        path.reverse()
                        return path
                    elif possible_dist_to_i < queue[i][0]: #if we found a better path, update it
                        queue[i][0] = possible_dist_to_i
                        queue[i][1] = min_index

            queue[min_index][2]  = False
        return []

