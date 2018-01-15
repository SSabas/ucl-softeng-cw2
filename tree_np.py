from matplotlib import pyplot as plt
import numpy as np
import yaml

# Configuration file
config = yaml.load(open("config.yml"))


def add_cut_np(current_branch, branch_length, branch_angle, side="positive"):

        if side == "positive":
            new_angles = current_branch[:,2]-branch_angle
            first_column = current_branch[:,0] + branch_length*np.sin(new_angles)
            second_column = current_branch[:,1] + branch_length*np.cos(new_angles)
            new_branch_combined = np.stack((first_column, second_column, new_angles), axis=-1)

        else:
            new_angles = current_branch[:,2]+branch_angle
            first_column = current_branch[:,0] + branch_length*np.sin(new_angles)
            second_column = current_branch[:,1] + branch_length*np.cos(new_angles)
            new_branch_combined = np.stack((first_column, second_column, new_angles), axis=-1)

        return new_branch_combined


def create_tree_np(branch_length, branch_length_decay, tree_size, branch_angle,
                   to_plot='yes', save_plot='yes', file_name='tree_np.png'):

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

    if save_plot == 'yes':
        plt.savefig(file_name)


create_tree_np(config["branch_length"],
               config["branch_length_decay"],
               config["tree_size"],
               config["branch_angle"])


