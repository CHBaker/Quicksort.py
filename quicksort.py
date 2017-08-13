"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# helper function moves starting index to compar with pivot to > value
def compare(pivotIndex, array, start):
        element = array[start]
        while array[pivotIndex] >= element:
            start += 1
            element = array[start]
            print "[][][] loop ---- index of new element count : ", start, "  value: ", array[start], " [][][]"

            # check if we have passed the pivot, to stop sorting
            if start == pivotIndex:
                    print "!!! sort ending... !!!"
                    return False
        return start

# helper function moves items within list for in-place sort        
def move(start, array, pivotIndex, end, compare):
        if not compare:
                # move element to last index
                print "* start value : ", array[start]
                array.insert(len(array[start:end]) + 1, array[start])
                # delete copy of first element
                array.pop(start)
                print "! first move : "
                print ""
                print array
                print ""
        else:
                # move element to last index
                print "* start value : ", array[compare]
                array.insert(len(array[start:end]) + 1, array[compare])
                # delete copy of first element
                array.pop(compare)
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
    sorting = True
    i = 1
    point = start
    print "* initial point: ", point
    pivot = array[(len(array[start: end]) - point)]
    print "* initial pivot: ", pivot
    pivotIndex = (len(array[start: end]) - point)
    print "* intial pivot index", pivotIndex
    
    while sorting:
        startval = array[start]
        print "[][][] start : ", startval, " }{ pivot : ", pivot, " [][][]"
        print "LOOP NUMBER", i
        
        if pivot < startval:
            pivotIndex = len(array[start: end]) - point
            array = move(start, array, pivotIndex, end, False)
            # update pivot location by changing point
            point += 1
            print "[][][] point : ", point, " [][][]"
            print "[][][] pivot index: ", pivotIndex, " [][][]"
            i += 1
            print "[][][] pivot: ", pivot, " [][][]"
            startval = array[start]
            
        elif pivot >= startval:
            print "[][][] elif move [][][]"
            pivotIndex = len(array[start: end]) - point
            print "[][][] --- arrays of elif ---- [][][]"
            comp = compare(pivotIndex, array, start)
            if comp:
                    array = move(start, array, pivotIndex, end, comp)
                    # update pivot location by changing point
                    point += 1
                    print "[][][] point : ", point, " [][][]"
                    startval = array[start]
        
                    i += 1
            elif not comp:
                    break
            
    print "[][][] completed list [][][]"
    return array
            
            
        
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, -1)
