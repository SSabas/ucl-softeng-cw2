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


def create_tree(branch_length, branch_length_decay, tree_size, branch_angle,
                to_plot='yes', to_save='yes', file_name='tree.png'):

    previous_level = [[0, branch_length, 0]]

    if to_plot == 'yes':
        plt.plot([0, 0], [0, branch_length])

    for i in range(tree_size):
        current_level = []
        branch_length *= branch_length_decay

        for branch in previous_level:
            current_level.append(add_cut(branch, branch_length, branch_angle, side="negative"))
            current_level.append(add_cut(branch, branch_length, branch_angle, side="positive"))

            if to_plot == 'yes':
                plt.plot([branch[0], current_level[-2][0]], [branch[1], current_level[-2][1]])
                plt.plot([branch[0], current_level[-1][0]], [branch[1], current_level[-1][1]])

        previous_level = current_level

    if to_save == 'yes':
        plt.savefig(file_name)


create_tree(config["branch_length"],
            config["branch_length_decay"],
            config["tree_size"],
            config["branch_angle"])

plt.savefig('tree.png')