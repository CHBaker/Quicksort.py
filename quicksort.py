"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# helper function moves starting index to compar with pivot to > value
def compare(pivot, array, start):
        element = array[start]
        while pivot >= element:
            start += 1
            element = array[start]
            print "[][][] loop ---- index of new element count : ", start, " [][][]"
        return start

# helper function moves items within list for in-place sort        
def move(start, array, pivotIndex, end):
        # move element to last index
        array.insert(end, array[start])
        # delete copy of first element
        array.pop(start)
        print "! first move : "
        print ""
        print array
        print ""
        
        # move item left of pivot to last element to the front of the list
        array.insert(start, array[pivotIndex - 2])
        # remove copy of said element
        array.pop(pivotIndex - 1)
        print "! second move : "
        print ""
        print array
        print ""
        
        return array
        
def quicksort(array, start, end):
    i = 1
    point = start
    print "* initial point: ", point
    pivot = array[(len(array[start: end]) - point)]
    print "* initial pivot: ", pivot
    pivotIndex = (len(array[start: end]) - point)
    print "* intial pivot index", pivotIndex
    
    while i <= ((len(array[start: end]) - 1)):
        startval = array[start]
        print "[][][] start : ", start, " }{ pivot : ", pivot, " [][][]"
        
        if pivot < start:
            pivotIndex = len(array[start: end]) - point
            array = move(start, array, pivotIndex, end)
            # update pivot location by changing point
            point += 1
            print "[][][] point : ", point, " [][][]"
            print "[][][] index: ", pivotIndex, " [][][]"
            i += 1
            print "[][][] pivot: ", pivot, " [][][]"
            startval = array[start]
            
        elif pivot >= start:
            print "[][][] elif move [][][]"
            pivotIndex = len(array[start: end]) - point
            print "[][][] --- arrays of elif ---- [][][]"
            array = move((compare(pivot, array, start)), array, pivotIndex, end)
            # update pivot location by changing point
            point += 1
            print "[][][] point : ", point, " [][][]"
            startval = array[start]
        
            i += 1
            
    print "[][][] completed list [][][]"
    print array
            
            
        
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, -1)
