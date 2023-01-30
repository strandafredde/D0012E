import random
import time



def insertionSortV1(list):

    #Goes through the list from 1 to the end
    #Starts at 1 because moved elements are always sorted because we haven't checked more
    for i in range(1, len(list)):
        j = i
        key = list[i]

        #compares the key with the previous element  until an element that is smaller is found
        while j -1 >= 0 and key < list[j -1] :
                list[j] = list[j-1 ]
                j -= 1

        #places the key after the element that was smaller than it 
        list[j] = key
    return list
def binarySearch(list, num, low, high):
    
    


        #Checks so the lowest value is not larger than the largest value
        if low > high:  
            return low

        #Creates a center point which is used to check if the number
        #that you are searching for are on the left or right side
        mid = ((high + low)//2)

        #Checks if the number you are looking for is in the middle of the list, if it is return mid. if not
        #Checks if the number you are looking for is greater or less than the middle value, then based on that
        #Changes minimum/minimum value changes to the middle value +- 1
        if list[mid] == num:
            return mid
        elif list[mid] < num: 
            return binarySearch(list, num , mid + 1, high)
        else:
            return binarySearch(list, num , low, mid - 1)



def bSort(list):
    #goes through the list from 1 to the end since we assume the first index is sorted
    for i in range(1, len(list)):
        key = list[i]
        pos = binarySearch(list, key, 0, i)
        #changes the list so that the elments from start until the position for the sorted number, places that number, adds the rest of the list
        list = list[:pos] + [key] + list[pos:i] + list[i+1:]

    return list


def mergeSortBSort(arr, k):
    #print(k, "k")
    #print(len(arr), "arr")
    if len(arr) <= k:
        #Replace with bSort/InsertionSort
        arr = bSort(arr) 
        return arr

    else:
        #Middle of list quantized to a multiple of 4
        middle = int(max(1, ((len(arr)/k)//2))*k) 

        L = arr[:middle]
        R = arr[middle:]
 
        L = mergeSortBSort(L, k)
        
        R = mergeSortBSort(R, k)
        #print(L, "l")
        #print(R, "r")
        

        i = 0
        j = 0
        k = 0

        #Merge sublist L and R
        li = []
        while len(L)>0 or len(R)>0:
            if(len(L)>0 and len(R)>0):
                if L[0]<R[0]:
                    li.append(L.pop(0))
                else:
                    li.append(R.pop(0))
            elif len(R) > 0:
                li.append(R.pop(0))
            elif len(L) > 0:
                li.append(L.pop(0))
        return li
    
def mergeSortInsertionSort(arr, k):
    #print(k, "k")
    #print(len(arr), "arr")
    if len(arr) <= k:
        #Replace with bSort/InsertionSort
        arr = insertionSortV1(arr) 
        return arr

    else:
        #Middle of list quantized to a multiple of 4
        middle = int(max(1, ((len(arr)/k)//2))*k) 

        L = arr[:middle]
        R = arr[middle:]
 
        L = mergeSortInsertionSort(L, k)
        
        R = mergeSortInsertionSort(R, k)
        #print(L, "l")
        #print(R, "r")
        

        i = 0
        j = 0
        k = 0

        #Merge sublist L and R
        li = []
        while len(L)>0 or len(R)>0:
            if(len(L)>0 and len(R)>0):
                if L[0]<R[0]:
                    li.append(L.pop(0))
                else:
                    li.append(R.pop(0))
            elif len(R) > 0:
                li.append(R.pop(0))
            elif len(L) > 0:
                li.append(L.pop(0))
    
        return li

#List creation.
def randomList(length):#completely random placements
    l = [] 
    li = [] 
    for i in range(0,length):
        l.append(i) 
    #end
    for i in range(0,length):
        rand = random.randint(0, len(l)-1) 
        li.append(l.pop(rand)) 
    
    return li 
    #end
#end

def sortedList(length):#Fully sorted
    l=[] 
    for i in range(0,length):
        l.append(i) 
    #end
    return l 
#end
#length: size
#offSorted: switches made
def unsortedList(length, offSorted):#switches random indexes in a sorted list
    l=[] 
    for i in range(0,length):
        l.append(i) 
    #end
    for i in range(0, offSorted):
        j = random.randint(0, len(l)-1) 
        k = random.randint(0, len(l)-1) 
        l[k], l[j] = l[j], l[k] 
    #end
    return l 
#end


#testing 


#MergeSort



def bSortTest(dataset, k):
    start_time = time.time()
    mergeSortBSort(dataset, k)
    print(k,"-rand b --- %s seconds ---" % (time.time() - start_time))

def LinearSortTest(dataset, k):
    start_time = time.time()
    mergeSortInsertionSort(dataset, k)
    print(k,"-rand ins --- %s seconds ---" % (time.time() - start_time))


rand = randomList(10000)
sort = sortedList(10000)
mult = 10
#for i in range(1,201):
    #LinearSortTest(randomList(10000), 4*i)
    #print(rand[1])
    #bSortTest(sort, mult*i)
    #LinearSortTest(sort, mult*i)

#list1 = randomList(200)
#list2 = randomList(100000)

print("Random", randomList(10))
print("Unsorted", unsortedList(10,5))
print("Sorted", sortedList(10))