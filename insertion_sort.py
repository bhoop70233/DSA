def insertion_sort(A):
    #start from the secound element(index 1) to the last element
    for i in range(1,len(A)):
        key=A[i] #Current element to be inserted into the sorted subarray
        j=i-1 # start comparing with the previous element
       
        # shift elements of the sorted subarray A[0... i-1] that are greater than the key
        while j>=0 and A[j]>key:
            A[j+1]=A[j] # Move the element one position to the right
            j-=1 # Move to the next element on the left

        A[j+1]=key # Insert the key at the correct position

#Example usage
A=[12,11,13,5,6]
insertion_sort(A)
print("Sorted array;",A)
