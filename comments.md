### Question 1
It can be easily seen from the plot produced by the perf_plot.py script (perf_plot.png)
that increasing the number of tree layers increases the run time exponentially, namely
the run time doubles with every subsequent layer. The behaviour is clearly shown on
the second subplot on plot perf_plot.png, which shows the log (base 2) of the run-time
versus the number of layers produced. The relationship is linear, confirming
the previous explanation. Such behaviour happens due appending new values to the array
with append() function, which is requires to create new lists every time the array is
full (it doubles in size).

### Question 2
When we use NumPy based array structure to create the trees, then the performance
changes considerably (see plot perf_plot_comparison.py, which is created with
run_comparison.py script). For small scale trees, standard library solution outperforms
the NumPy based solution by a small margin, but for large trees the opposite is true.
This phenomenon happens due to the fact that NumPy uses vectorised computation, meaning
it performs fast vectorised arithmetic operations on the whole array and hence is
magnitudes faster than base solution as it does not require continues new array
assignments.