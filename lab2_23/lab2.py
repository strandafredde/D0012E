import sys


def ThreeSmallestInc(list):
    n = len(list)
    result = [sys.maxsize, sys.maxsize, sys.maxsize]
    if n < 3:
        return "inte nog stor lista :/ "
    else:
        for i in range (0, n):
            # if a number in the list is smallar than the smallest number in the resulting list,
            # move the numbers in the resutling array 1 step to the right and add the new smallest 
            # number in the first spot in the array, same goes for the elif statments but you
            # check second and thrid smallest in them but the process is the same.
            if list[i] < result[0]:
                result[2] = result[1]
                result[1] = result[0]
                result[0] = list[i]

            elif list[i] < result[1]:
                result[2] = result[1]
                result[1] = list[i] 

            elif list[i] < result[2]:
                result[2] = list[i]
        return result


def ThreeSmallestDAQ(list):
    #base cases
    result = []
    i = 0
    j = 0  
    if len(list) == 1:
        return list
    elif len(list) == 2:
        if list[0] > list[1]:
            list = [list[1], list[0]]
        return list
    elif len(list) == 3:
        if list[0] > list[1] or list[0] > list[2]:
            list = [list[1], list[0], list[2]]

        if list[1] > list[2]:
            list = [list[0], list[2], list[1]]

        if list[0] > list[1]:
            list = [list[1], list[0], list[2]]
        return list

    else:
        #divide list into two equal parts
        L = list[:len(list)//2]
        R = list[len(list)//2:]
        #print("left: ", L,"right: ", R)
        L_DAQ = ThreeSmallestDAQ(L)
        R_DAQ = ThreeSmallestDAQ(R)
        
                 
        while len(result) < 3 and (i < len(L_DAQ) or j < len(R_DAQ)):
            if i < len(L_DAQ) and (j == len(R_DAQ) or L_DAQ[i] < R_DAQ[j]):
                result.append(L_DAQ[i])
                i += 1
            else:
                result.append(R_DAQ[j])
                j += 1
        return result[:3]


def MaxSubArray(list, left, right):
    # Base case: when the range contains only one element
    if left == right:
        return [list[left], list[left], list[left], list[left]] 

    # Find the middle of the range
    middle = (left + right) // 2

    # Recursively compute the left and right subarray sums
    left_sums = MaxSubArray(list, left, middle)
    right_sums = MaxSubArray(list, middle + 1, right)

    # Merge and compare the results
    # Calculate the maximum sum on the left side
    left_max = max(left_sums[0], left_sums[3] + right_sums[0])

    # Calculate the maximum sum on the right side
    right_max = max(right_sums[1], right_sums[3] + left_sums[1])

    # Calculate the maximum sum so far
    max_temp = max(left_sums[2], right_sums[2])

    # Update the maximum sum if a cross-sum is greater
    max_sum = max(max_temp, left_sums[1] + right_sums[0])

    # Calculate the entire sum for the range
    sum_total = left_sums[3] + right_sums[3]

    return [left_max, right_max, max_sum, sum_total]


#-------------------------------------------------- Testing -----------------------------------------------------------------------------------------------
test_list1 = [2, 112, 1, 33 ,23 ,7, 41, 312]
test_list2 = [1,1,1,2]
test_list3 = [1, -3, -5, 2, -1, 3, -1]
print("")
print("INCREMENTAL| The three smallest numbers are:", ThreeSmallestInc(test_list1))

print("DIVIDE AND CONQUER| The three smallest numbers are:", ThreeSmallestDAQ(test_list1))

print("MAX SUB ARRAY| The maximum subarray is: ", max(MaxSubArray(test_list3, 0, len(test_list3) -1 )))