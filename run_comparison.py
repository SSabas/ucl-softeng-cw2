from matplotlib import pyplot as plt
from perf_plot import time_the_tree
from matplotlib.ticker import MaxNLocator


def compare_runs(max_layers=7, number_of_runs=100, number_of_repeats=3,
                 to_plot='yes', to_save='no', file_name='perf_plot_comparison.png'):

    results_standard = time_the_tree(max_layers=max_layers, number_of_runs=number_of_runs,
                                     number_of_repeats=number_of_repeats, use_numpy='no',
                                     to_plot='no')
    results_np = time_the_tree(max_layers=max_layers, number_of_runs=number_of_runs,
                               number_of_repeats=number_of_repeats, use_numpy='yes',
                               to_plot='no')

    if to_plot == 'yes':

        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(range(1,max_layers+1), results_standard, label='Standard array structure')
        ax1.plot(range(1,max_layers+1), results_np, label='NumPy array structure')
        ax1.legend(shadow=True, fancybox=True)
        ax1.set_title("Tree-building run-time comparison \n (run-time is aggregated over {number} iterations"
                      " and shown the min of {repeats} experiments)".format(length=max_layers,
                                                                            number=number_of_runs,
                                                                            repeats=number_of_repeats),
                      fontsize=10)
        ax2.plot(range(1, max_layers+1), results_standard)
        ax2.plot(range(1, max_layers+1), results_np)
        ax2.set_yscale('log', basey=2)
        ax2.set_xlabel("Number of layers", fontsize=8)
        ax2.set_ylabel("Run-time (log-scale, base 2, seconds)", fontsize=8)
        ax1.set_ylabel("Run-time (seconds)", fontsize=8)
        ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

        if to_save == 'yes':
            plt.savefig(file_name)


compare_runs(max_layers=15, number_of_runs=100, number_of_repeats=1,
             to_plot='yes', to_save='no', file_name='perf_plot_comparison.png')

