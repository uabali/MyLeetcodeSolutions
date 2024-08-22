/* 
1512. Number of Good Pairs
*/

int numIdenticalPairs(int* nums, int numsSize) {

    int i,j;
    int count=0;

    for(i=0; i<numsSize; i++){

        for(j= i + 1; j<numsSize; j++){

            if( nums[i] == nums[j]){

                count++;
            }

    }

    }
    return count;
}