from math import sin, cos
from matplotlib import pyplot as plt
import yaml
from argparse import ArgumentParser


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


if __name__ == "__main__":
    parser = ArgumentParser(description="Beautiful tree generator.")
    parser.add_argument('--branch_length', '-l', type=float, required=False, default=1,
                        help="Branch length, default 1.")
    parser.add_argument('--branch_length_decay', '-d', type=float, required=False, default=0.5,
                        help="Branch length decay factor, default 0.5")
    parser.add_argument('--tree_size', '-s', type=int, required=False, default=5,
                        help="Number of levels on the tree, default 5.")
    parser.add_argument('--branch_angle', '-a', type=float, required=False, default=0.2,
                        help="Factor for tree branch separation, default 0.2.")
    parser.add_argument('--to_save', '-o', type=str, required=False, default="yes",
                        help="To save the output in file named tree.png.")
    arguments = parser.parse_args()

    create_tree(arguments.branch_length,
                arguments.branch_length_decay,
                arguments.tree_size,
                arguments.branch_angle,
                to_save=arguments.to_save)
