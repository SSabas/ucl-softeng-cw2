from matplotlib import pyplot as plt
import timeit
from matplotlib.ticker import MaxNLocator


def time_the_tree(max_layers=5, number_of_runs=10000, number_of_repeats=3,
                  to_plot='yes', to_save='no', file_name='perf_plot.png'):

    # Placeholders for time collection
    results = []

    for i in range(max_layers):

        function_call = ('create_tree(branch_length = 6, branch_length_decay = 0.8, tree_size = {layer},'
                         'branch_angle = 0.2, to_plot = "no", to_save="no")').format(layer=i)
        setup_call = 'from tree import create_tree'

        t = timeit.Timer(function_call, setup_call)
        layer_time = min(t.repeat(number=number_of_runs, repeat=number_of_repeats))
        results.append([layer_time])

    if to_plot == 'yes':

        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(range(1,max_layers+1), results)
        # ax1.set_title(label = "Normal text $\it{Italics}$")
        ax1.set_title("Run-time of tree building function with varying number of layers \n (based on the cumulative"
                      " time of {number} iterations and shown the minimum  of \n {repeats} "
                      "repeated experiments)".format(number=number_of_runs, repeats=number_of_repeats), fontsize=10)
        ax2.plot(range(1,max_layers+1), results)
        ax2.set_yscale('log', basey=2)
        ax2.set_xlabel("Number of layers", fontsize=8)
        ax2.set_ylabel("Run-time (log-scale, base 2)", fontsize=8)
        ax1.set_ylabel("Run-time", fontsize=8)
        ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

        if to_save == 'yes':
            plt.savefig(file_name)

    return results


# time_the_tree(max_layers=10,
#               number_of_runs=100,
#               number_of_repeats=10,
#               to_save='no',
#               to_plot='yes')

