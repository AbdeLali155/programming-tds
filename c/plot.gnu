set terminal png size 1400,900 font 'Arial,12'
set output 'sorting_comparison.png'
set title 'Comparative Study of Sorting Algorithms' font 'Arial,16'
set xlabel 'Array Size (elements)' font 'Arial,14'
set ylabel 'Time (seconds)' font 'Arial,14'
set logscale xy
set grid
set key left top
plot 'results.dat' using 1:($2>0?$2:1/0) with linespoints lw 2 title 'Bubble Sort', \
     'results.dat' using 1:($3>0?$3:1/0) with linespoints lw 2 title 'Insertion Sort', \
     'results.dat' using 1:($4>0?$4:1/0) with linespoints lw 2 title 'Selection Sort', \
     'results.dat' using 1:5 with linespoints lw 2 title 'Quick Sort', \
     'results.dat' using 1:6 with linespoints lw 2 title 'Merge Sort', \
     'results.dat' using 1:7 with linespoints lw 2 title 'Shell Sort', \
     'results.dat' using 1:8 with linespoints lw 2 title 'TimSort'
