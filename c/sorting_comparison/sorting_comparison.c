#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


void bubbleSort(int arr[], int n);
void insertionSort(int arr[], int n);
void selectionSort(int arr[], int n);
void quickSort(int arr[], int low, int high);
void mergeSort(int arr[], int left, int right);
void shellSort(int arr[], int n);
void timSort(int arr[], int n);
void generateRandomArray(int arr[], int n);
double measureTime(void (*sortFunc)(int[], int), int arr[], int n);
double measureTimeQuick(int arr[], int n);
double measureTimeMerge(int arr[], int n);  


void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int *L = (int*)malloc(n1 * sizeof(int));
    int *R = (int*)malloc(n2 * sizeof(int));
    
    if (L == NULL || R == NULL) {
        printf("Memory allocation failed in merge!\n");
        exit(1);
    }
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
    
    free(L);
    free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void shellSort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}

#define MIN_MERGE 32

void insertionSortRange(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void timSort(int arr[], int n) {
    for (int i = 0; i < n; i += MIN_MERGE) {
        int right = (i + MIN_MERGE - 1 < n - 1) ? (i + MIN_MERGE - 1) : (n - 1);
        insertionSortRange(arr, i, right);
    }
    
    for (int size = MIN_MERGE; size < n; size = 2 * size) {
        for (int left = 0; left < n; left += 2 * size) {
            int mid = left + size - 1;
            int right = (left + 2 * size - 1 < n - 1) ? (left + 2 * size - 1) : (n - 1);
            
            if (mid < right) {
                merge(arr, left, mid, right);
            }
        }
    }
}



void generateRandomArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000000;
    }
}

double measureTime(void (*sortFunc)(int[], int), int arr[], int n) {
    int *temp = (int*)malloc(n * sizeof(int));
    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return -1.0;
    }
    
    memcpy(temp, arr, n * sizeof(int));
    
    clock_t start = clock();
    sortFunc(temp, n);
    clock_t end = clock();
    
    free(temp);
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}

double measureTimeQuick(int arr[], int n) {
    int *temp = (int*)malloc(n * sizeof(int));
    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return -1.0;
    }
    
    memcpy(temp, arr, n * sizeof(int));
    
    clock_t start = clock();
    quickSort(temp, 0, n - 1);
    clock_t end = clock();
    
    free(temp);
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}

double measureTimeMerge(int arr[], int n) {
    int *temp = (int*)malloc(n * sizeof(int));
    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return -1.0;
    }
    
    memcpy(temp, arr, n * sizeof(int));
    
    clock_t start = clock();
    mergeSort(temp, 0, n - 1);
    clock_t end = clock();
    
    free(temp);
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}




int main() {
    srand(time(NULL)); 
    
    FILE *fp = fopen("results.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // En-tête du fichier
    fprintf(fp, "# Size Bubble Insertion Selection Quick Merge Shell TimSort\n");
    
    // Tailles à tester
    int sizes[] = {1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1000000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);
    
    printf("=== COMPARATIVE STUDY OF SORTING ALGORITHMS ===\n");
    printf("This may take several minutes...\n\n");
    printf("%-10s %-12s %-12s %-12s %-12s %-12s %-12s %-12s\n",
           "Size", "Bubble(s)", "Insertion(s)", "Selection(s)", 
           "Quick(s)", "Merge(s)", "Shell(s)", "TimSort(s)");
    printf("--------------------------------------------------------------------------------------------\n");
    
    for (int i = 0; i < numSizes; i++) {
        int n = sizes[i];
        
        int *arr = (int*)malloc(n * sizeof(int));
        if (arr == NULL) {
            printf("Memory allocation failed for size %d!\n", n);
            continue;
        }
        
        generateRandomArray(arr, n);
        
        double timeBubble = -1, timeInsertion = -1, timeSelection = -1;
        double timeQuick = 0, timeMerge = 0, timeShell = 0, timeTimSort = 0;
        
        if (n <= 16000) {
            timeBubble = measureTime(bubbleSort, arr, n);
            timeInsertion = measureTime(insertionSort, arr, n);
            timeSelection = measureTime(selectionSort, arr, n);
        }
        
        timeQuick = measureTimeQuick(arr, n);
        timeMerge = measureTimeMerge(arr, n);
        timeShell = measureTime(shellSort, arr, n);
        timeTimSort = measureTime(timSort, arr, n);
      
        printf("%-10d ", n);
        printf("%-12.6f %-12.6f %-12.6f ", 
               (timeBubble >= 0) ? timeBubble : 0.0,
               (timeInsertion >= 0) ? timeInsertion : 0.0,
               (timeSelection >= 0) ? timeSelection : 0.0);
        printf("%-12.6f %-12.6f %-12.6f %-12.6f\n",
               timeQuick, timeMerge, timeShell, timeTimSort);
       
        fprintf(fp, "%d %.6f %.6f %.6f %.6f %.6f %.6f %.6f\n",
                n, 
                (timeBubble >= 0) ? timeBubble : -1.0,
                (timeInsertion >= 0) ? timeInsertion : -1.0,
                (timeSelection >= 0) ? timeSelection : -1.0,
                timeQuick, timeMerge, timeShell, timeTimSort);
        
        free(arr);
    }
    
    fclose(fp);
    

    
    FILE *gnuplot = fopen("plot.gnu", "w");
    fprintf(gnuplot, "set terminal png size 1400,900 font 'Arial,12'\n");
    fprintf(gnuplot, "set output 'sorting_comparison.png'\n");
    fprintf(gnuplot, "set title 'Comparative Study of Sorting Algorithms' font 'Arial,16'\n");
    fprintf(gnuplot, "set xlabel 'Array Size (elements)' font 'Arial,14'\n");
    fprintf(gnuplot, "set ylabel 'Time (seconds)' font 'Arial,14'\n");
    fprintf(gnuplot, "set logscale xy\n");
    fprintf(gnuplot, "set grid\n");
    fprintf(gnuplot, "set key left top\n");
    fprintf(gnuplot, "plot 'results.dat' using 1:($2>0?$2:1/0) with linespoints lw 2 title 'Bubble Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:($3>0?$3:1/0) with linespoints lw 2 title 'Insertion Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:($4>0?$4:1/0) with linespoints lw 2 title 'Selection Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:5 with linespoints lw 2 title 'Quick Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:6 with linespoints lw 2 title 'Merge Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:7 with linespoints lw 2 title 'Shell Sort', \\\n");
    fprintf(gnuplot, "     'results.dat' using 1:8 with linespoints lw 2 title 'TimSort'\n");
    fclose(gnuplot);
    
    FILE *gnuplot2 = fopen("plot_efficient.gnu", "w");
    fprintf(gnuplot2, "set terminal png size 1400,900 font 'Arial,12'\n");
    fprintf(gnuplot2, "set output 'efficient_algorithms.png'\n");
    fprintf(gnuplot2, "set title 'Efficient Algorithms O(n log n)' font 'Arial,16'\n");
    fprintf(gnuplot2, "set xlabel 'Array Size (elements)' font 'Arial,14'\n");
    fprintf(gnuplot2, "set ylabel 'Time (seconds)' font 'Arial,14'\n");
    fprintf(gnuplot2, "set logscale x\n");
    fprintf(gnuplot2, "set grid\n");
    fprintf(gnuplot2, "set key left top\n");
    fprintf(gnuplot2, "plot 'results.dat' using 1:5 with linespoints lw 2 title 'Quick Sort', \\\n");
    fprintf(gnuplot2, "     'results.dat' using 1:6 with linespoints lw 2 title 'Merge Sort', \\\n");
    fprintf(gnuplot2, "     'results.dat' using 1:7 with linespoints lw 2 title 'Shell Sort', \\\n");
    fprintf(gnuplot2, "     'results.dat' using 1:8 with linespoints lw 2 title 'TimSort'\n");
    fclose(gnuplot2);
    
    FILE *gnuplot3 = fopen("plot_complexity.gnu", "w");
    fprintf(gnuplot3, "set terminal png size 1400,900 font 'Arial,12'\n");
    fprintf(gnuplot3, "set output 'complexity_comparison.png'\n");
    fprintf(gnuplot3, "set title 'O(n²) vs O(n log n) Complexity' font 'Arial,16'\n");
    fprintf(gnuplot3, "set xlabel 'Array Size (elements)' font 'Arial,14'\n");
    fprintf(gnuplot3, "set ylabel 'Time (seconds)' font 'Arial,14'\n");
    fprintf(gnuplot3, "set grid\n");
    fprintf(gnuplot3, "set key left top\n");
    fprintf(gnuplot3, "plot 'results.dat' using 1:($2>0?$2:1/0) with linespoints lw 2 title 'Bubble O(n²)', \\\n");
    fprintf(gnuplot3, "     'results.dat' using 1:5 with linespoints lw 2 title 'Quick O(n log n)', \\\n");
    fprintf(gnuplot3, "     'results.dat' using 1:6 with linespoints lw 2 title 'Merge O(n log n)'\n");
    fclose(gnuplot3);
    
    printf("\n=== ANALYSIS COMPLETE ===\n");
    printf("Results saved to 'results.dat'\n");
    printf("GNUPlot scripts generated:\n");
    printf("  1. plot.gnu              -> sorting_comparison.png\n");
    printf("  2. plot_efficient.gnu    -> efficient_algorithms.png\n");
    printf("  3. plot_complexity.gnu   -> complexity_comparison.png\n\n");
    printf("To generate graphs, run:\n");
    printf("  gnuplot plot.gnu\n");
    printf("  gnuplot plot_efficient.gnu\n");
    printf("  gnuplot plot_complexity.gnu\n");
    
    return 0;
}