# This File Contains AI Code for solving Maze Problem
import copy


problem = [
    ["#", " ", " ", " ", " ", " ", "B"],
    ["#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "#", "#"],
    ["#", "#", " ", "#", " ", "#", "#"],
    ["#", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "#", " ", " ", "#", "#"],
    ["#", "#", " ", " ", "#", "#", "#"],
    ["#", " ", " ", " ", "#", "#", "#"],
    ["#", "#", " ", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", "#", "#"],
    ["#", " ", "#", " ", "#", "#", "#"],
    ["A", " ", " ", " ", " ", " ", " "]
]

# Actions
# 1. Up 
# 2. Down
# 3. Left
# 4. Right


notReachedGoalState = True
states = []
actions = []


# Individual Node
class Node:
    def __init__(self, state, parent, action, currentPosition):
        self.state = state
        self.parent = parent
        self.action = action
        self.currentPosition = currentPosition # list of row and column [row, column]


# Depth First Search
class StackFrontier:
    def __init__(self):
        self.frontier = []
        self.isVisitedState = []

    def addNode(self, node):
        self.frontier.append(node)
    
    def checkIfStateVisited(self, node):
        if(node in self.isVisitedState):
            return True
        return False
    
    def removeNode(self):
        node = self.frontier[-1]
        print(findGoalPositiom(problem) == node.currentPosition)
        if findGoalPositiom(problem) == node.currentPosition:
            global notReachedGoalState
            global states
            global actions
            print("Reached Goal State")
            notReachedGoalState = False
            while node:
                states.append(node.state)
                actions.append(node.action)
                node = node.parent
            states = states[: -1]
            actions = actions[: -1]
            states.reverse()
            actions.reverse()
            


        else:
            self.isVisitedState.append(node.state)
            if len(self.frontier) > 1:
                self.frontier = self.frontier[:-1]
            else:
                self.frontier = []
            self.expandNode(node)
    
    def expandNode(self, node):
        position = node.currentPosition
        if (position[0] >= 0 and not position[0] == len(problem) - 1) and (problem[position[0] + 1][position[1]] == " " or problem[position[0] + 1][position[1]] == "B"):
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0] + 1][position[1]] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "down", [position[0] + 1, position[1]]))
        if (position[0] <= len(problem) - 1 and not position[0] == 0) and (problem[position[0] - 1][position[1]] == " " or problem[position[0] - 1][position[1]] == "B"):
            # check for up
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0] - 1][position[1]] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "up", [position[0] - 1, position[1]]))
        if (position[1] >= 0 and not position[1] == len(problem[0]) - 1) and (problem[position[0]][position[1] + 1] == " " or problem[position[0]][position[1] + 1] == "B"):
            # check for right
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0]][position[1] + 1] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "right", [position[0], position[1] + 1]))
        if (position[1] <= len(problem[0]) - 1 and not position[1] == 0) and (problem[position[0]][position[1] - 1] == " " or problem[position[0]][position[1] - 1] == "B"):
            # check for left
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0]][position[1] - 1] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "left", [position[0], position[1] - 1]))
        

# Breadth First Search
class QueueFrontier:
    def __init__(self):
        self.frontier = []
        self.isVisitedState = []

    def addNode(self, node):
        self.frontier.append(node)
    
    def checkIfStateVisited(self, node):
        if(node in self.isVisitedState):
            return True
        return False
    
    def removeNode(self):
        node = self.frontier[0]
        print(findGoalPositiom(problem) == node.currentPosition)
        if findGoalPositiom(problem) == node.currentPosition:
            global notReachedGoalState
            global states
            global actions
            print("Reached Goal State")
            notReachedGoalState = False
            while node:
                states.append(node.state)
                actions.append(node.action)
                node = node.parent
            states = states[: -1]
            actions = actions[: -1]
            states.reverse()
            actions.reverse()
            


        else:
            self.isVisitedState.append(node.state)
            if len(self.frontier) > 1:
                self.frontier = self.frontier[1: ]
            else:
                self.frontier = []
            self.expandNode(node)
    
    def expandNode(self, node):
        position = node.currentPosition
        if (position[0] >= 0 and not position[0] == len(problem) - 1) and (problem[position[0] + 1][position[1]] == " " or problem[position[0] + 1][position[1]] == "B"):
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0] + 1][position[1]] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "down", [position[0] + 1, position[1]]))
        if (position[0] <= len(problem) - 1 and not position[0] == 0) and (problem[position[0] - 1][position[1]] == " " or problem[position[0] - 1][position[1]] == "B"):
            # check for up
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0] - 1][position[1]] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "up", [position[0] - 1, position[1]]))
        if (position[1] >= 0 and not position[1] == len(problem[0]) - 1) and (problem[position[0]][position[1] + 1] == " " or problem[position[0]][position[1] + 1] == "B"):
            # check for right
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0]][position[1] + 1] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "right", [position[0], position[1] + 1]))
        if (position[1] <= len(problem[0]) - 1 and not position[1] == 0) and (problem[position[0]][position[1] - 1] == " " or problem[position[0]][position[1] - 1] == "B"):
            # check for left
            smallProblem = copy.deepcopy(problem)
            smallProblem[position[0]][position[1] - 1] = '*'
            if(not self.checkIfStateVisited(smallProblem)):
                self.addNode(Node(smallProblem, node, "left", [position[0], position[1] - 1]))
        


# Hill Climbing



def findInitialCurrentPosition(problem):
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if problem[i][j] == 'A':
                return [i, j]
    return [len(problem) - 1, 0]


def findGoalPositiom(problem):
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if problem[i][j] == 'B':
                return [i, j]
    return [0, len(problem[0]) - 1]

myNode = Node(problem, None, None, findInitialCurrentPosition(problem))
myFrontier = QueueFrontier()
myFrontier.addNode(myNode)
while(notReachedGoalState):
    myFrontier.removeNode()


for i in actions:
    print(i)