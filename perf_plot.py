from matplotlib import pyplot as plt
import timeit
from argparse import ArgumentParser
from matplotlib.ticker import MaxNLocator


def time_the_tree(max_layers=5, number_of_runs=100, number_of_repeats=3,
                  to_plot='yes', to_save='no', file_name='perf_plot.png',
                  use_numpy='yes'):

    # Placeholders for time collection
    results = []

    for i in range(max_layers):

        if use_numpy == 'yes':
            function_call = ('create_tree_np(branch_length = 6, branch_length_decay = 0.8, tree_size = {layer},'
                             'branch_angle = 0.2, to_plot = "no", to_save="no")').format(layer=i)
            setup_call = 'from tree_np import create_tree_np'

        else:
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
        ax2.set_ylabel("Run-time (log-scale, base 2, seconds)", fontsize=8)
        ax1.set_ylabel("Run-time (seconds)", fontsize=8)
        ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

        if to_save == 'yes':
            plt.savefig(file_name)

    return results


if __name__ == "__main__":
    parser = ArgumentParser(description="Tree generator function performance analyser.")
    parser.add_argument('--max_layers', '-l', type=int, required=False, default=5,
                        help="Maximum number of layers to be created, default 5.")
    parser.add_argument('--number_of_runs', '-n', type=int, required=False, default=100,
                        help="Number of iterations per run, default 100.")
    parser.add_argument('--number_of_repeats', '-r', type=int, required=False, default=3,
                        help="Number of repeated experiments, default 3.")
    parser.add_argument('--to_save', '-s', type=str, required=False, default="yes",
                        help="To save the output in file named oerf_plot.png.")
    parser.add_argument('--use_numpy', '-u', type=str, required=False, default="no",
                        help="Toggle to use NumPy based arrays.")
    arguments = parser.parse_args()

    time_the_tree(max_layers=arguments.max_layers,
                  number_of_runs=arguments.number_of_runs,
                  number_of_repeats=arguments.number_of_repeats,
                  to_save=arguments.to_save,
                  use_numpy=arguments.use_numpy)

