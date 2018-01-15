from math import sin, cos
from matplotlib import pyplot as plt
import yaml

# Configuration file
config = yaml.load(open("config.yml"))  # Configuration file


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

        for j in d:
            n.append(add_cut(j, branch_length, branch_angle, side="negative"))
            n.append(add_cut(j, branch_length, branch_angle, side="positive"))

            plt.plot([j[0], n[-2][0]], [j[1], n[-2][1]])
            plt.plot([j[0], n[-1][0]], [j[1], n[-1][1]])
        d = n
        branch_length *= branch_length_decay


create_tree(config["branch_length"],
            config["branch_length_decay"],
            config["tree_size"],
            config["branch_angle"])

plt.savefig('tree.png')