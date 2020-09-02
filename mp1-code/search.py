# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi,fast)
import heapq
def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "astar": astar,
        "astar_corner": astar_corner,
        "astar_multi": astar_multi,
        "fast": fast,
    }.get(searchMethod)(maze)

def bfs(maze):
    """
    Runs BFS for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    (stRow, stCol) = maze.getStart()
    # print(maze.getObjectives())
    checked = set()
    # checked.add((stRow, stCol))
    queue = []
    queue.append((stRow, stCol))
    prev = dict()
    while len(queue) > 0:
        
        (row, col) = queue.pop(0)
        if (row, col) in checked:
            continue
        checked.add((row, col))
        # print(path)
        if maze.isObjective(row, col):
            path = []
            cur = (row, col)
            while cur in prev:
                path.append(cur)
                cur = prev[cur]
            # print(path)
            path.reverse()
            return path
        neighbors = maze.getNeighbors(row, col)
        for n in neighbors:
            if n not in checked:
                # checked.add(n)
                prev[n] = (row,col)
                # newPath = list(path)
#                 newPath.append(n)
                queue.append(n)
            #else:                
                # neighbors.remove(n)
                
    
    
    return []


def astar(maze):
    def getH (cur):
        row = cur[0]
        col = cur[1]
        return abs(row - gRow) + abs(col - gCol)
        
        
    print(maze.getObjectives())
    (stRow, stCol) = maze.getStart()
    (gRow, gCol) = maze.getObjectives()[0]
    g = dict()
    h = dict()
    f = dict()
    done = set()
    g[(stRow, stCol)] = 0
    h[(stRow, stCol)] = getH((stRow, stCol))
    f[(stRow, stCol)] = h[(stRow, stCol)] + g[(stRow, stCol)]
    prev = dict()
    heap = [(f[(stRow, stCol)], (stRow, stCol))]
    print(heap)
    heapq.heapify(heap)
    
    while len(heap) > 0:
        
        (row, col) = heapq.heappop(heap)[1]
        if (row, col) in done:
            continue
        done.add((row,col))
        # print((row, col))
        # print(heap)
        if maze.isObjective(row, col):
            path = []
            cur = (row, col)
            while cur in prev:
                path.append(cur)
                cur = prev[cur]
            # print(path)
            path.reverse()
            return path
                
        neighbors = maze.getNeighbors(row, col)
        for n in neighbors:
            hVal = getH(n)
            gVal = g[(row, col)] + 1
            g[n] = gVal
            h[n] = hVal
            fVal = hVal + gVal
            # heapq.heappush(heap,  (hVal, n))
#             prev[n] = (row, col)
            if n in f:
                if f[n] > fVal:
                    heap.remove((f[n], n))
                    heapq.heappush(heap, (fVal, n))
                    f[n] = fVal
                    prev[n] = (row, col)
            else:
                heapq.heappush(heap, (fVal, n))
                f[n] = fVal
                prev[n] = (row, col)
#
    
    """
    Runs A star for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []

def astar_corner(maze):
    """
    Runs A star for part 2 of the assignment in the case where there are four corner objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
        """
    # TODO: Write your code 
    goals = maze.getObjectives()
    def getH (cur):
        row = cur[0]
        col = cur[1]
        dist = dict()
        closest = goals[0]
        for (gRow, gCol) in goals:
            dist[(gRow, gCol)] = (abs(row - gRow) + abs(col - gCol))
            if dist[(gRow, gCol)] < dist[closest]:
                closest = (gRow, gCol)
        ret = dist[closest]
        cRow = closest[0]
        cCol = closest[1]
        for (gRow, gCol) in goals:
            if (gRow, gCol) != closest:
                ret += (abs(cRow - gRow) + abs(cCol - gCol))
        return ret
    reachedGoals = set()
    (stRow, stCol) = maze.getStart()
    checked = set()
    g = dict()
    h = dict()
    f = dict()
    g[(stRow, stCol)] = 0
    h[(stRow, stCol)] = getH((stRow, stCol))
    f[(stRow, stCol)] = g[(stRow, stCol)] + h[(stRow, stCol)] 
    heap = [(f[(stRow, stCol)], (stRow, stCol))]
    heapq.heapify(heap)
    path = []
    prev = dict()
    while len(heap) > 0:
        print(goals)
        (row, col) = heapq.heappop(heap)[1]
        if (row, col) in checked:
            continue
        checked.add((row, col))
        if (row, col) in goals:
            print(row, col)
            curPath = []
            goals.remove((row, col))
            cur = (row, col)
            while cur in prev:
                curPath.append(cur)
                cur = prev[cur]
            curPath.reverse()
            path += curPath
            if len(goals) == 0:
                print(path)
                return path
            prev.clear()
            checked.clear()
            checked.add((row, col))
            # heap.clear()
        neighbors = maze.getNeighbors(row, col)
        for n in neighbors:
            if n not in checked:
                prev[n] = (row, col)
            g[n] = g[(row, col)] + 1
            h[n] = getH(n)
            f[n] = g[n] + h[n]
            heapq.heappush(heap,(f[n], n))
    return []

def astar_multi(maze):
    """
    Runs A star for part 3 of the assignment in the case where there are
    multiple objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []


def fast(maze):
    """
    Runs suboptimal search algorithm for part 4.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []
