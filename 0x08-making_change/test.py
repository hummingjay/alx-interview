
import sys
 
def findMinCountToReachSum(sum, components):
    # numWays[i] represent number of ways to build value i efficiently
    # using provided components.
    numWays=[0]*(sum+1);
     
    for i in range(1, sum+1):
        numWays[i] = sys.maxsize;  # First start with a invalid value.
        # Try to improve the value using given components.
        for j in range(0, len(components)): 
             
            # component c can only contribute in building number i, if it is
            # less than or equal to number i.
            if(i >= components[j]) :
                 
                # Check if component c can be utilized to build number i in 
                # a better way.
                numWays[i] = min(numWays[i], numWays[i-components[j]] + 1);
     
    return numWays[sum];
 
# driver code
sum = 111;
arr = [2,1,4,3,5,6];
print(findMinCountToReachSum(sum, arr));

