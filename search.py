# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node:
    def __init__(self, state, action, parent, cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost

def getSolution(node):
    path = []
    temp = node
    while (temp.parent != None):
        #print("advanced")
        path.append(temp.action)
        temp = temp.parent
    #print(path, "path")
    newPath = path[::-1]
   # print("\n",newPath,"actual path")
    return newPath

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    node = Node(state = problem.getStartState(), action = None, parent = None, cost = None) #https://stackoverflow.com/questions/12864004/tracing-and-returning-a-path-in-depth-first-search
    path = []
    if problem.isGoalState(node.state):
        return path
    frontier = util.Stack()
    frontier.push(node)
    explored = set([])
    #print("entering loop")
    while True:
        if frontier.isEmpty():
            #print("no path")
            return []
       
        node = frontier.pop()
        if problem.isGoalState(node.state):
                   # print("found")
                   path = getSolution(node)
                   return path
                   
        explored.add(node.state)
        i = 0
        t = problem.getSuccessors(node.state)
        print(t)
        for x in t:
           # print(x)
            succ = x[0]
            ac = x[1]
            i = i + 1
           # print(i)
            
        
           # print("h")
            child = Node(state = succ, action = ac, parent = node, cost = None)
            if child.state not in explored:
                
                
                frontier.push(child)
    

            
           

            
            
        
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    node = Node(state = problem.getStartState(), action = None, parent = None, cost = None) #https://stackoverflow.com/questions/12864004/tracing-and-returning-a-path-in-depth-first-search
    path = []
    if problem.isGoalState(node.state):
        return path
    frontier = util.Queue()
    frontier.push(node)
    explored = set([])
    explored.add(node.state)
    #print("entering loop")
    while True:
        if frontier.isEmpty():
            #print("no path")
            return []
       
        node = frontier.pop()
        if problem.isGoalState(node.state):
                   # print("found")
                   path = getSolution(node)
                   return path
                   
        
        i = 0
        t = problem.getSuccessors(node.state)
        #print(t)
        for x in t:
           # print(x)
            succ = x[0]
            ac = x[1]
            i = i + 1
           # print(i)
            
        
           # print("h")
            child = Node(state = succ, action = ac, parent = node, cost = None)
            if child.state not in explored:
                explored.add(child.state)
                
                frontier.push(child)
    
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    node= Node(state=problem.getStartState(), action = None, parent = None, cost = 0)
    frontier = util.PriorityQueue()
    path = []
    explored = set([])
    explored.add(node.state)
    if problem.isGoalState(node.state):
        return path
    frontier.push(node, 0)
    #print("entering loop")
    while True:
        if frontier.isEmpty():
            #print("no path")
            return []
        node = frontier.pop()
        if problem.isGoalState(node.state):
            path=getSolution(node)
            return path
        i = 0
        #explored.add(node.state)
        t = problem.getSuccessors(node.state)
        #explored.add(node.state)
        for x in t:
           # print(x)
            succ = x[0]
            ac = x[1]
            co = x[2]
            i = i + 1
           # print(i)

            
           # print("h")
            child = Node(state = succ, action = ac, parent = node, cost = co + node.cost)
            #print(child.cost)
            if child.state not in explored:   
                explored.add(child.state)             
                frontier.push(child, co)   


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
