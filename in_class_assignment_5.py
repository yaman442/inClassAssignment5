#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''



import re
import statistics
def quicksort(numbers_in_a_list):

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION
    GreaterThanPivot = []
    LowerThanPivot = []


    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
    else:
        PivotItem = numbers_in_a_list.pop()
  
    for i in numbers_in_a_list:
        if i > PivotItem:
            GreaterThanPivot.append(i)
        else:
            LowerThanPivot.append(i)
    return quicksort(LowerThanPivot) + [PivotItem] + quicksort(GreaterThanPivot)
    


def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE
    

    with open('numbers.txt') as file_object:
        orderingList = file_object.readlines()
        #return print(quicksort(brekingList))
        #^keeps returning as a string ? (eveything in the text document is stored as a string in the first index of a list)

       
       
       
        with open('sorted.txt','w') as sortedList:
           for items in quicksort([449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 640, 448, 522, 820, 964, 688, 840, 113, 325, 950, 754, 999, 723, 909, 956, 255, 972, 111, 543, 282, 443, 362, 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 882, 834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 277, 29, 476, 126, 382, 101, 27, 135, 944, 307, 220, 51, 153, 536, 711, 901, 507, 139, 94, 155, 214, 724, 315, 33, 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 729, 484, 505, 508, 875, 709, 589, 425, 454, 702]):
               sortedList.write(str(items) + ',')
            

        return print(quicksort([449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 640, 448, 522, 820, 964, 688, 840, 113, 325, 950, 754, 999, 723, 909, 956, 255, 972, 111, 543, 282, 443, 362, 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 882, 834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 277, 29, 476, 126, 382, 101, 27, 135, 944, 307, 220, 51, 153, 536, 711, 901, 507, 139, 94, 155, 214, 724, 315, 33, 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 729, 484, 505, 508, 875, 709, 589, 425, 454, 702]))


if __name__ == "__main__":
    main()


#Thanks to Derrick Sherrill on Youtube for some help on the recursion algorithm