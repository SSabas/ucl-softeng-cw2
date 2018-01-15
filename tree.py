from math import sin, cos
from matplotlib import pyplot as plt

# Constants
tree_size = 5
branch_angle = 0.2
branch_length_decay = 0.6
branch_length = 1


def add_cut(current_branch, branch_length, branch_angle, side="positive"):

    if side == "positive":
        new_branch = [current_branch[0]+branch_length*sin(current_branch[2]+branch_angle),
                      current_branch[1]+branch_length*cos(current_branch[2]+branch_angle),
                      current_branch[2]+branch_angle]

    else:
        new_branch = [current_branch[0]+branch_length*sin(current_branch[2]-branch_angle),
                      current_branch[1]+branch_length*cos(current_branch[2]-branch_angle),
                      current_branch[2]-branch_angle]

    return new_branch


def create_tree(branch_length, branch_length_decay, tree_size, branch_angle):

    d = [[0, branch_length, 0]]
    plt.plot([0, 0], [0, branch_length])

    for i in range(tree_size):
        n = []

        for j in range(len(d)):
            n.append(add_cut(d[j], branch_length, branch_angle, side="negative"))
            n.append(add_cut(d[j], branch_length, branch_angle, side="positive"))

            plt.plot([d[j][0], n[-2][0]], [d[j][1], n[-2][1]])
            plt.plot([d[j][0], n[-1][0]], [d[j][1], n[-1][1]])
        d = n
        branch_length *= branch_length_decay


create_tree(branch_length, branch_length_decay, tree_size, branch_angle)
plt.savefig('tree.png')