set terminal png size 1400,900 font 'Arial,12'
set output 'complexity_comparison.png'
set title 'O(n²) vs O(n log n) Complexity' font 'Arial,16'
set xlabel 'Array Size (elements)' font 'Arial,14'
set ylabel 'Time (seconds)' font 'Arial,14'
set grid
set key left top
plot 'results.dat' using 1:($2>0?$2:1/0) with linespoints lw 2 title 'Bubble O(n²)', \
     'results.dat' using 1:5 with linespoints lw 2 title 'Quick O(n log n)', \
     'results.dat' using 1:6 with linespoints lw 2 title 'Merge O(n log n)'
