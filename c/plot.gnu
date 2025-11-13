set terminal png size 1200,800
set output 'sorting_comparison.png'
set title 'Comparative Study of Sorting Algorithms'
set xlabel 'Array Size (elements)'
set ylabel 'Time (seconds)'
set logscale xy
set grid
set key left top
plot 'results.dat' using 1:2 with linespoints title 'Bubble Sort', \
     'results.dat' using 1:3 with linespoints title 'Insertion Sort', \
     'results.dat' using 1:4 with linespoints title 'Selection Sort', \
     'results.dat' using 1:5 with linespoints title 'Quick Sort', \
     'results.dat' using 1:6 with linespoints title 'Merge Sort', \
     'results.dat' using 1:7 with linespoints title 'Shell Sort', \
     'results.dat' using 1:8 with linespoints title 'TimSort'
