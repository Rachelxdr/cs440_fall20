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
import math
import collections
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
            path.append(cur)
            path.reverse()
            return path
        neighbors = maze.getNeighbors(row, col)
        for n in neighbors:
            if n not in checked:
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
    heap = [(f[(stRow, stCol)], 0, (stRow, stCol))]
    print(heap)
    heapq.heapify(heap)
    
    while len(heap) > 0:
        (curF, curG, idx) =  heapq.heappop(heap)
        if idx in done:
            continue
        done.add(idx)
        if maze.isObjective(idx[0], idx[1]):
            path = []
            cur = idx
            while cur in prev:
                path.append(cur)
                cur = prev[cur]
            # print(path)
            path.append(cur)
            path.reverse()
            return path
                
        neighbors = maze.getNeighbors(idx[0], idx[1])
        for n in neighbors:
            hVal = getH(n)
            gVal = curG + 1
            g[n] = gVal
            h[n] = hVal
            fVal = hVal + gVal
            if n in f:
                if f[n] > fVal:
                    heap.remove((f[n], n))
                    heapq.heappush(heap, (fVal, gVal, n))
                    f[n] = fVal
                    prev[n] = idx


            else:
                heapq.heappush(heap, (fVal, gVal, n))
                f[n] = fVal
                prev[n] = (idx)
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

    def hFun(cur):
        idx = cur[0]
        remains = cur[1]
        

    
    # def mD(first, second):
    #     return abs(first[0] - second[0]) + abs(first[1] - second[1])
        
    # goals = maze.getObjectives()


    # def setUp(nodeList):
    #     aList = collections.defaultdict(list)
    #     for node in nodeList:
    #         for secNode in nodeList:
    #             if secNode != node:
    #                 aList[node].append((secNode))
    #     return aList

    # def prims(cur):
    #     print(cur)
    #     nodeList = []
    #     nodeList.append(cur[0])
    #     nodeList += cur[1]




    #     graph = setUp(nodeList)
    #     checked = set()
    #     checked.add(cur[0])
    #     ret = 0
    #     mst = []
    #     heapq.heapify(mst)
    #     heapq.heappush(mst, (0, cur[0]), cur[1])
    #     for node in nodeList:
    #         if node != cur[0]:
    #             heapq.heappush(math.inf, (0, node))
    #     while len(mst) > 0:
    #         (d, idx, remain) = heapq.heappop(mst)
    #         ret += d
    #         if 






        # d = dict()
        # d[cur[0]] = 0
        # checked = set()
        # for node in nodeList:
        #     if node != cur[0]:
        #         d[node] = math.inf
        # for i, node in enumerate(nodeList):
        #     for j, other in enumerate(nodeList):
        #         if i != j:
        #             graph[node] = (mD(node, other) , other)
        # mstHeap = []
        # heapq.heapify(mstHeap)
        # for key, val in d.items():
        #     heapq.heappush(mstHeap, (val, key))
        # ret = 0
        # while len(mstHeap) > 0:
        #     curG = heapq.heappop(mstHeap)
        #     if curG in checked:
        #         continue
        #     checked.add(curG[1])
        #     ret += d[curG[1]]
        #     if len(checked) == len(nodeList):
        #         return ret
        #     for n in nodeList:
        #         # print(curG[1], n)
        #         newD = mD(curG[1], n) + d[curG[1]]
        #         if newD < d[n]:
        #             d[curG[1]] = newD
        #             heapq.heappush(mstHeap,(newD, n))
        # return ret

    def hFunc(cur):
        curNode = cur[0]
        allGoals = cur[1]
        cl = allGoals[0]
        curMin = mD(curNode, allGoals[0])
        for g in allGoals:
            curD = mD(curNode, g)
            if curD < curMin:
                curMin = curD
                cl = g
        param2 = []
        for g in allGoals:
            if g != cl:
                param2.append(g)
        return curMin + prims((cl, param2))


    (stR, stC) = maze.getStart()
    g = dict()
    h = dict()
    f = dict()
    g[(stR, stC)] = 0
    h[(stR, stC)] = hFunc(((stR, stC), goals))
    print("start h:",h[(stR, stC)])
    f[(stR, stC)] = h[(stR, stC)] + g[(stR, stC)]
    prev = dict()
    heap = [(f[(stR, stC)], 0, (stR, stC), tuple(goals))]
    heapq.heapify(heap)
    checked = set()
    while len(heap) > 0:
        isGoal = 0
        (fVal, gVal, (r, c), remain) = heapq.heappop(heap)
        if ((r, c), remain) in checked:
            continue
        checked.add(((r, c), remain))
        oldRemain = remain
        curRemain = list(remain)
        if (r, c) in curRemain:
            # print("find")
            isGoal = 1
            curRemain.remove((r, c))
            remain = tuple(curRemain)
            if len(curRemain) == 0:
                # print("finish")
                # for key, val in prev.items():
                    # print("curr:", key)
                    # print("prev:", val)
                # print(prev)
                cur = ((r, c), oldRemain)
                path = []
                while cur in prev:
                    path.append(cur[0])
                    # print(cur, "   ", prev[cur])
                    cur = prev[cur]
                path.append(cur[0])
                path.reverse()
                return path
        # print("cur",((r, c), remain))
        # print("old",oldRemain)
        neighbors = maze.getNeighbors(r, c)
        for n in neighbors:
            # print(n)
            g[n] = gVal + 1
            h[n] = hFunc((n, remain))
            # print(h[n])
            newF = g[n] + h[n]
            # if n in f:
            #     if f[n] > newF:
            #         heapq.heappush(heap, (newF, g[n], n, remain))
            #         f[n] = newF
            #         prev[(n, remain)] = ((r, c), remain)

            # # if (n, remain) not in checked:
            # #     if isGoal:
            # #         print("old",oldRemain, "new", remain)
            # #         prev[(n, remain)] = ((r, c), oldRemain)
            # else:
                # print("push", n)
            # heapq.heappush(heap, (newF, g[n], n, remain))
            
            if (n, remain) not in checked:
                if isGoal:
                    prev[(n, remain)] = ((r, c), oldRemain)
                else:
                    prev[(n, remain)] = ((r, c), remain)
                
                heapq.heappush(heap, (newF, g[n], n, remain))
                f[n] = newF
            # heapq.heappush(heap, (f[n], n, remain))
    return []



            

    # TODO: Write your code 
  
def astar_multi(maze):
    """
    Runs A star for part 3 of the assignment in the case where there are
    multiple objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    # def mD(first, second):
    #     return abs(first[0] - second[0]) + abs(first[1] - second[1])
    # goals = maze.getObjectives()

    # def hFunc(cur):
    #     nodeList = []
    #     nodeList.append(cur[0])
    #     nodeList += cur[1]
    #     graph = dict()
    #     d = dict()
    #     d[cur[0]] = 0
    #     checked = set()
    #     for node in nodeList:
    #         if node != cur[0]:
    #             d[node] = math.inf
    #     for i, node in enumerate(nodeList):
    #         for j, other in enumerate(nodeList):
    #             if i != j:
    #                 graph[node] = (mD(node, other) , other)
    #     mstHeap = []
    #     heapq.heapify(mstHeap)
    #     for key, val in d.items():
    #         heapq.heappush(mstHeap, (val, key))
    #     ret = 0
    #     while len(mstHeap) > 0:
    #         curG = heapq.heappop(mstHeap)
    #         if curG in checked:
    #             continue
    #         checked.add(curG[1])
    #         ret += d[curG[1]]
    #         if len(checked) == len(nodeList):
    #             return ret
    #         for n in nodeList:
    #             # print(curG[1], n)
    #             newD = mD(curG[1], n) + d[curG[1]]
    #             if newD < d[n]:
    #                 d[curG[1]] = newD
    #                 heapq.heappush(mstHeap,(newD, n))
    #     return ret

    # (stR, stC) = maze.getStart()
    # g = dict()
    # h = dict()
    # f = dict()
    # g[(stR, stC)] = 0
    # h[(stR, stC)] = hFunc(((stR, stC), goals))
    # f[(stR, stC)] = h[(stR, stC)] + g[(stR, stC)]
    # prev = dict()
    # heap = [(f[(stR, stC)], 0, (stR, stC), tuple(goals))]
    # heapq.heapify(heap)
    # checked = set()
    # while len(heap) > 0:
    #     isGoal = 0
    #     (fVal, gVal, (r, c), remain) = heapq.heappop(heap)
    #     if ((r, c), remain) in checked:
    #         continue
    #     checked.add(((r, c), remain))
    #     oldRemain = remain
    #     curRemain = list(remain)
    #     if (r, c) in curRemain:
    #         # print("find")
    #         isGoal = 1
    #         curRemain.remove((r, c))
    #         remain = tuple(curRemain)
    #         if len(curRemain) == 0:
    #             # print("finish")
    #             # for key, val in prev.items():
    #                 # print("curr:", key)
    #                 # print("prev:", val)
    #             # print(prev)
    #             cur = ((r, c), oldRemain)
    #             path = []
    #             while cur in prev:
    #                 path.append(cur[0])
    #                 # print(cur, "   ", prev[cur])
    #                 cur = prev[cur]
    #             path.append(cur[0])
    #             path.reverse()
    #             return path
    #     # print("cur",((r, c), remain))
    #     # print("old",oldRemain)
    #     neighbors = maze.getNeighbors(r, c)
    #     for n in neighbors:
    #         # print(n)
    #         g[n] = gVal + 1
    #         h[n] = hFunc((n, remain))
    #         newF = g[n] + h[n]
    #         # if n in f:
    #         #     if f[n] > newF:
    #         #         heapq.heappush(heap, (newF, g[n], n, remain))
    #         #         f[n] = newF
    #         #         prev[(n, remain)] = ((r, c), remain)

    #         # # if (n, remain) not in checked:
    #         # #     if isGoal:
    #         # #         print("old",oldRemain, "new", remain)
    #         # #         prev[(n, remain)] = ((r, c), oldRemain)
    #         # else:
    #             # print("push", n)
    #         # heapq.heappush(heap, (newF, g[n], n, remain))
    #         if n in remain:


    #         if (n, remain) not in checked:
    #             if isGoal:
    #                 prev[(n, remain)] = ((r, c), oldRemain)
    #             else:
    #                 prev[(n, remain)] = ((r, c), remain)
                
    #             heapq.heappush(heap, (newF, g[n], n, remain))
    #             f[n] = newF
    #         # heapq.heappush(heap, (f[n], n, remain))
    # return []
    


def fast(maze):
    """
    Runs suboptimal search algorithm for part 4.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []
