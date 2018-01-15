from math import sin, cos
from matplotlib import pyplot as plt

# Constants
tree_size = 5
branch_angle = 0.2
branch_length_decay = 0.6
branch_length = 1


def create_tree(branch_length, branch_length_decay, tree_size, branch_angle):

    d = [[0, branch_length, 0]]
    plt.plot([0, 0], [0, branch_length])

    for i in range(tree_size):
        n = []

        for j in range(len(d)):
            n.append([d[j][0]+branch_length*sin(d[j][2]-branch_angle),
                      d[j][1]+branch_length*cos(d[j][2]-branch_angle),
                      d[j][2]-branch_angle])
            n.append([d[j][0]+branch_length*sin(d[j][2]+branch_angle),
                      d[j][1]+branch_length*cos(d[j][2]+branch_angle),
                      d[j][2]+branch_angle])

            plt.plot([d[j][0], n[-2][0]], [d[j][1], n[-2][1]])
            plt.plot([d[j][0], n[-1][0]], [d[j][1], n[-1][1]])
        d = n
        branch_length *= branch_length_decay
        

create_tree(branch_length, branch_length_decay, tree_size, branch_angle)
plt.savefig('tree.png')