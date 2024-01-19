#Sum at odd position is equal or not by removing an element


def remove_element_to_balance(arr):
    total_sum = sum(arr)
    even_sum=list()
    odd_sum=list()
    even_sum=[arr[1]]
    odd_sum= [arr[0]]
    e,o=1,1
    for i in (range(len(arr)-2)):
        if (i+2) % 2 == 0:
            odd_sum.append(odd_sum[o-1]+arr[i+2])
            o=o+1
        else:
            even_sum.append(even_sum[e-1]+ arr[i+2])
            e=e+1
    print(even_sum,odd_sum)
    e,o=1,1
    for i in range(len(arr)):
        if i==0:
            ce=odd_sum[len(odd_sum)-1]-arr[i]
            co=even_sum[len(even_sum)-1]
        elif i==1:
            ce=odd_sum[len(odd_sum)-1]-odd_sum[0]
            co=odd_sum[0]+even_sum[len(even_sum)-1]-arr[i]
        elif i%2==0:
            ce = even_sum[e-1] + odd_sum[len(odd_sum)-1] - odd_sum[o]
            co = even_sum[len(even_sum)-1] - even_sum[e] + odd_sum[o-1]
            o=o+1
        else:
            ce = even_sum[e-1] + odd_sum[len(odd_sum)-1] - odd_sum[o-1]
            co = even_sum[len(even_sum)-1] - even_sum[e] + odd_sum[o-1]
            e=e+1
            

        if ce == co:
            return arr[i]

    return -1  # If no element can be removed to balance even and odd positions

# Example usage:
array = [2,3,4,1,5,6,7]
result = remove_element_to_balance(array)
if result != -1:
    array.remove(result)
    print(f"Removed element {result} to balance the sums. Updated array: {array}")
else:
    print("No element can be removed to balance the sums.")
