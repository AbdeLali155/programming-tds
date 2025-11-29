set terminal png size 1400,900 font 'Arial,12'
set output 'efficient_algorithms.png'
set title 'Efficient Algorithms O(n log n)' font 'Arial,16'
set xlabel 'Array Size (elements)' font 'Arial,14'
set ylabel 'Time (seconds)' font 'Arial,14'
set logscale x
set grid
set key left top
plot 'results.dat' using 1:5 with linespoints lw 2 title 'Quick Sort', \
     'results.dat' using 1:6 with linespoints lw 2 title 'Merge Sort', \
     'results.dat' using 1:7 with linespoints lw 2 title 'Shell Sort', \
     'results.dat' using 1:8 with linespoints lw 2 title 'TimSort'
