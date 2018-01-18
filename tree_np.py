from matplotlib import pyplot as plt
import numpy as np
import yaml
from argparse import ArgumentParser

# Configuration file
config = yaml.load(open("config.yml"))


def add_cut_np(current_branch, branch_length, branch_angle, side="positive"):

        if side == "positive":
            new_angles = current_branch[:, 2]-branch_angle
            x_coordinate = current_branch[:, 0] + branch_length*np.sin(new_angles)
            y_coordinate = current_branch[:, 1] + branch_length*np.cos(new_angles)
            new_branch_combined = np.stack((x_coordinate, y_coordinate, new_angles), axis=-1)

        else:
            new_angles = current_branch[:, 2]+branch_angle
            x_coordinate = current_branch[:, 0] + branch_length*np.sin(new_angles)
            y_coordinate = current_branch[:, 1] + branch_length*np.cos(new_angles)
            new_branch_combined = np.stack((x_coordinate, y_coordinate, new_angles), axis=-1)

        return new_branch_combined


def create_tree_np(branch_length, branch_length_decay, tree_size, branch_angle,
                   to_plot='yes', to_save='yes', file_name='tree_np.png'):

    # Initialise the tree
    previous_level_np = np.array([[0, branch_length, 0]])

    if to_plot == 'yes':
        plt.plot([0, 0], [0, branch_length])

    for i in range(tree_size):

        branch_length *= branch_length_decay

        current_level_neg = add_cut_np(previous_level_np, branch_length, branch_angle, side="negative")
        current_level_pos = add_cut_np(previous_level_np, branch_length, branch_angle, side="positive")

        if to_plot == 'yes':

            for base, neg, pos in zip(previous_level_np, current_level_neg, current_level_pos):
                plt.plot([base[0], pos[0]], [base[1], pos[1]])
                plt.plot([base[0], neg[0]], [base[1], neg[1]])

        previous_level_np = np.vstack((current_level_neg, current_level_pos))

    if to_save == 'yes':
        plt.savefig(file_name)


if __name__ == "__main__":
    parser = ArgumentParser(description="Beautiful tree generator with NumPy.")
    parser.add_argument('--branch_length', '-l', type=float, required=False, default=1,
                        help="Branch length, default 1.")
    parser.add_argument('--branch_length_decay', '-d', type=float, required=False, default=0.5,
                        help="Branch length decay factor, default 0.5")
    parser.add_argument('--tree_size', '-s', type=int, required=False, default=5,
                        help="Number of levels on the tree, default 5.")
    parser.add_argument('--branch_angle', '-a', type=float, required=False, default=0.2,
                        help="Factor for tree branch separation, default 0.2.")
    parser.add_argument('--to_save', '-o', type=str, required=False, default="yes",
                        help="To save the output in file named tree_np.png.")
    arguments = parser.parse_args()

    create_tree_np(arguments.branch_length,
                   arguments.branch_length_decay,
                   arguments.tree_size,
                   arguments.branch_angle,
                   to_save=arguments.to_save)



