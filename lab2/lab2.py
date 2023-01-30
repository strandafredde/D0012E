import sys

def ThreeSmallestInc(list):
    n = len(list)
    smallest = [list[0], list[1], list[2]]
    if n < 3:
        return ":/ "
    else:
        for i in range (0, n):
            if list[i] < smallest[0]:
                smallest[1] = smallest[0]
                smallest[0] =  list[i]
            elif list[i] < smallest[1]:
                 smallest[2] = smallest[1]
                 smallest[1] =  list[i]

            elif list[i] < smallest[2]:
                 smallest[2] =  list[i]

    return smallest

def algo1DAQ(list):
    if(len(list) == 1):
        return list
    elif len(list) == 2:
        if list[0]>list[1]:
            return [list[1],list[0]]
        return list
    elif len(list) == 3:
        #print(list, "a")
        if list[0] > list[1] or list[0] > list[2]:
            list = [list[1], list[0], list[2]]
           # print(list, "a")
        if list[1] > list[2]:
            list = [list[0], list[2], list[1]]
            #print(list, "a")
        if list[0] > list[1]:
            list = [list[1], list[0], list[2]]
            #print(list, "a")
        return list

    else:
        L = list[:len(list)//2]
        R = list[len(list)//2:]
        
        L_R = algo1DAQ(L) + algo1DAQ(R)
        #3,1,40,5,7,6
        while len(L_R) > 3:
            n=0
            for i in range(len(L_R)):
                if(L_R[i]>n):
                    n = L_R[i]
            L_R.remove(n)
        L_R = algo1DAQ(L_R)
        return L_R

 
def findMaxSubarray(list, low, high):
    if high == low:
        return (low, high, list[low])
    
    else:
        mid = (low + high) // 2


def max_subarray(list, left, right):
    if (left == right):
        return [list[left], list[left], list[left], list[left]]

    # Divide 
    # Get the left and right sums, divide
    middle = (left + right) // 2
    left_sums = max_subarray(list, left, middle)            # Get the left values [left left sum, left right sum, left max sum, left sum ]
    right_sums = max_subarray(list, middle + 1, right)      # Get the right values [right left sum, right right sum, right max sum, right sum]

    print("")

    # Conqure
    # Log the max sum on the left side
    if left_sums[0] > left_sums[3]+right_sums[0]:
        left_max = left_sums[0]                     # Case left left sum is better than merging entire left side with right left sum
        print("no merge left")
    else:
        left_max = left_sums[3]+right_sums[0]       # Case mergin entire left side with right left sum is best
        print("merge left")

    # Log the max sum om the right side
    if right_sums[1] > right_sums[3]+left_sums[1]:
        right_max = right_sums[1]                   # Case right right sum is better than crossing entire right side with left right max
        print("no merge right")
    else: 
        right_max = right_sums[3] + left_sums[1]    # Case merging entire right side with left right max is best
        print("merge right")
    # log the highest sum so far
    if left_sums[2] > right_sums[2]:
        max_temp = left_sums[2]                     # Case left sum was better than right sum
        print("left better than right")
    else:
        max_temp = right_sums[2]                    # Case right sum was better than left sum
        print("right better than left")
    if left_sums[1]+right_sums[0] > max_temp:
        max_sum = left_sums[1]+right_sums[0]        # Case crossing sum is better than both left and right
        print("cross sum best")
    else:
        max_sum = max_temp                          # Case left or right sum was best

    # keep track of the entire sum
    sum_total = left_sums[3] + right_sums[3]
    print("Left sums", left_sums)
    print("Left max", left_max)
    print("Right sums", right_sums)
    print("Right max", right_max)
    print("Total sum", sum_total)
    return [left_max, right_max, max_sum, sum_total]
#testing



test = [2, -4, 8, 12, -18, 24, -32, 48, 56, -64, 12]
#print(max(max_subarray(test,0, len(test)-1)))

#print(ThreeSmallestInc(test))
max_subarray(test,0, len(test)-1)
