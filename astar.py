from math import sqrt


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0


def print_board(b):
    for y in range(10):
        for x in range(10):
            print(b[y][x], end='')
        print()


def mark_the_path_on_board(b, steps):
    for step in steps:
        b[step[1]][step[0]] = 'X'


def get_shortest_path(b, start, finish):
    start_node = Node(None, start)
    finish_node = Node(None, finish)
    available_nodes = []
    used_nodes = []
    available_nodes.append(start_node)

    while available_nodes:
        current_node = available_nodes[0]
        for node in available_nodes:
            if node.f < current_node.f:
                current_node = node
        available_nodes.pop(available_nodes.index(current_node))
        used_nodes.append(current_node)

        if current_node.position == finish_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent

            return path[::-1]

        children = []

        for position in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_node.position[0] + position[0], current_node.position[1] + position[1])
            children.append(Node(current_node, new_position))

        for child in children:
            tmp_x = child.position[0]
            tmp_y = child.position[1]

            if tmp_x < 0 or tmp_x > len(b) - 1 or tmp_y < 0 or tmp_y > len(b) - 1:
                continue

            if b[tmp_y][tmp_x] != '.':
                continue

            flag_1 = False
            for node in available_nodes:
                if node.position == child.position:
                    flag_1 = True
                    break

            if flag_1 is True:
                continue

            flag_2 = False
            for node in used_nodes:
                if node.position == child.position:
                    flag_2 = True
                    break

            if flag_2 is True:
                continue

            child.g = current_node.g + 1
            child.h = sqrt((tmp_x - finish[0])**2 + (tmp_y - finish[1])**2)
            child.f = child.g + child.h

            available_nodes.append(child)		

def main():
    board = [['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
         ['.', '#', '.', '.', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '#', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '#', '.', '#', '#', '.', '.', '.', '.'],
         ['.', '.', '#', '.', '.', '.', '#', '.', '.', '.'],
         ['.', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
         ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']
         ]

    start = (0, 0)
    end = (9, 0)

    path = get_shortest_path(board, start, end)
    mark_the_path_on_board(board, path)
    print('Najkrotsza droga:', path)
    print_board(board)

if __name__ == '__main__':
    main()