"""

Name: Lotoya Willis
Date: 01/28/2024
Assignment: 3
Due Date: 01/28/2024
About this project: Finds a solution to the farmer-wolf-goat-cabbage riddle using breadth first search
Assumptions: N/A
All work below was performed by Lotoya Willis using the Missionaries and Cannibals example
video from Module 3 as reference

"""


class State:
    def __init__(self, farmerLeft, wolfLeft, goatLeft, cabbageLeft, boat, farmerRight, wolfRight, goatRight,
                 cabbageRight):
        self.farmerLeft = farmerLeft
        self.wolfLeft = wolfLeft
        self.goatLeft = goatLeft
        self.cabbageLeft = cabbageLeft
        self.boat = boat
        self.farmerRight = farmerRight
        self.wolfRight = wolfRight
        self.goatRight = goatRight
        self.cabbageRight = cabbageRight
        self.parent = None

    # ensures the farmer, the wolf, the goat, and the cabbage are all on the other side of the river
    def is_goal(self):
        if self.farmerLeft == 0 and self.wolfLeft == 0 and self.goatLeft == 0 and self.cabbageLeft == 0:
            return True
        else:
            return False

    # checks if a move is possible
    def is_valid(self):
        if self.wolfLeft > 0 and self.goatLeft > 0 and self.farmerLeft == 0 \
                or self.goatLeft > 0 and self.cabbageLeft > 0 and self.farmerLeft == 0 \
                or self.wolfRight > 0 and self.goatRight > 0 and self.farmerRight == 0 \
                or self.goatRight > 0 and self.cabbageRight > 0 and self.farmerRight == 0:
            return False
        else:
            return True

    # checks if a move is equal to another
    def __eq__(self, other):
        return (self.farmerLeft == other.farmerLeft and self.wolfLeft == other.wolfLeft
                and self.goatLeft == other.goatLeft and self.cabbageLeft == other.cabbageLeft
                and self.boat == other.boat and self.farmerRight == other.farmerRight
                and self.wolfRight == other.wolfRight and self.goatRight == other.goatRight
                and self.cabbageRight == other.cabbageRight)

    # creates a hash code using farmerLeft, wolfLeft, goatLeft, cabbageLeft, boat,
    # farmerRight, wolfRight, GoatRight, and cabbageRight
    def __hash__(self):
        return hash((self.farmerLeft, self.wolfLeft, self.goatLeft, self.cabbageLeft, self.boat, self.farmerRight,
                     self.wolfRight, self.goatRight, self.cabbageRight))


# finds the next possible moves
def successors(cur_state):
    children = []
    if cur_state.boat == 'left':
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft - 1,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight + 1)
        # The farmer and the cabbage cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft - 1, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight + 1,
                          cur_state.cabbageRight)
        # The farmer and the goat cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft - 1, cur_state.goatLeft, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight + 1, cur_state.goatRight,
                          cur_state.cabbageRight)
        # The farmer and the wolf cross left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft - 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft,
                          'right',
                          cur_state.farmerRight + 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight)
        # The farmer crosses left to right.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

    else:
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft + 1,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight - 1)
        # The farmer and the cabbage cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft + 1, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight - 1,
                          cur_state.cabbageRight)
        # The farmer and the goat cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft + 1, cur_state.goatLeft, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight - 1, cur_state.goatRight,
                          cur_state.cabbageRight)
        # The farmer and the wolf cross right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.farmerLeft + 1, cur_state.wolfLeft, cur_state.goatLeft, cur_state.cabbageLeft,
                          'left',
                          cur_state.farmerRight - 1, cur_state.wolfRight, cur_state.goatRight,
                          cur_state.cabbageRight)
        # The farmer crosses right to left.
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)

    return children


# breadth first search through the possible moves
def search():
    initial_state = State(1, 1, 1, 1, 'left', 0, 0, 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None


# displays solution
def print_solution(solution):
    path = [solution]
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(str(state.farmerLeft).center(12, ' ') + str(state.wolfLeft).center(11, ' ')
              + str(state.goatLeft).center(12, ' ') + str(state.cabbageLeft).center(15, ' ')
              + state.boat.center(7, ' ') + str(state.farmerRight).center(15, ' ')
              + str(state.wolfRight).center(13, ' ') + str(state.goatRight).center(13, ' ')
              + str(state.cabbageRight).center(15, ' '))


def main():
    solution = search()
    print("Farmer, Wolf, Goat, Cabbage Riddle solution:")
    print("Farmer Left | Wolf Left | Goat Left | Cabbage Left | Boat | Farmer Right | Wolf Right | Goat Right | "
          "Cabbage Right")
    print_solution(solution)


if __name__ == '__main__':
    main()
