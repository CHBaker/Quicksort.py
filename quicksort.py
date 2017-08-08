"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# helper function moves starting index to compar with pivot to > value
def compare(newpivot, array):
        index = 0
        element = array[index]
        while newpivot >= element:
            index += 1
            element = array[index]
            print "loop ---- index of new element count : ", index
        return index

# helper function moves items within list for in-place sort        
def move(compare, array, pivotIndex):
        # move element to last index
        array.append(array[compare])
        # delete copy of first element
        array.pop(compare)
        print "first move : ", array
        
        # move item left of pivot to last element to the front of the list
        array.insert(0, array[pivotIndex - 2])
        # remove copy of said element
        array.pop(pivotIndex - 1)
        print "second move : ", array
        
        return array
        
def quicksort(array):
    i = 1
    point = 1
    pivot = array[(len(array) - point)]
    pivotIndex = (len(array) - point)
    
    while i <= ((len(array) / 2) - 1):
        start = array[0]
        print "start :", start, "pivot :", pivot
        
        if pivot < start:
            pivotIndex = len(array) - point
            array = move(0, array, pivotIndex)
            # update pivot location by changing point
            point += 1
            print "point : ", point
            print "index: ", pivotIndex
            i += 1
            print "pivot", pivot
            start = array[0]
            
        elif pivot >= start:
            print "elif move"
            pivotIndex = len(array) - point
            print "---arrays of elif----"
            array = move((compare(pivot, array)), array, pivotIndex)
            # update pivot location by changing point
            point += 1
            print "point : ", point
            start = array[0]
        
            i += 1
            
    print "completed list  ", array
            
            
        
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
