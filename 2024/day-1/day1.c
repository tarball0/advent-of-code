#include <stdio.h>
#include <stdlib.h>

int comp(const void* a,const void* b) {
      return *(int*)a - *(int*)b;
}

int main(){
	FILE *file = fopen("input.txt", "r");
	char line[15];
	int n1, n2;
	int array1[1000], array2[1000];
	int counter = 0;
	int result = 0;
	int a, b;
	while (fscanf(file, "%d %d",&n1, &n2) == 2) {
		array1[counter] = n1;
		array2[counter] = n2;
		counter++;
	}
	qsort(array1, 1000, sizeof(int), comp);
	qsort(array2, 1000, sizeof(int), comp);

	for(int i = 0; i < 1000; i++) {
		a = array1[i];
		b = array2[i];
		if (a > b) {
			result += array1[i] - array2[i];
		} else {
			result += array2[i] - array1[i];
		}
	}
	printf("result 1: %d\n", result);
	result = 0;

	int checker;
	for(int i = 0; i < 1000; i++){
	 	checker = array1[i];
		counter = 0;
		for(int j = 0; j < 1000; j++){
			if (array2[j] == checker) {
				counter++;		
			}
		}
		result += array1[i]*counter;	
	}
	 		
	printf("result 2: %d\n", result);
	 		
	fclose(file);
	return 0;
}
