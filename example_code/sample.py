#Format a to a decimal with 6 digits
"%.6f"%4
#Round works, but not to add zero padding
round(4, 6)
#Zero pad the front with something like this:
"%06.2f"%3.3
#Division by integers gets rounded to integer, so to preserve decimal values, divide by floats.


####
def miniMaxSum(arr):
    lenMin = len([x for x in arr if x == min(arr)])
    lenMax = len([x for x in arr if x == max(arr)])
    maximumNumber = 0
    minimumNumber = 0
    # Handle cases where there are duplicate min/max inputs.
    if lenMin == 1:
        maximumNumber = sum([x for x in arr if x > min(arr)])
    else:
        maximumNumber = sum([x for x in arr if x > min(arr)]) + ((lenMin-1)*min(arr))
        
    if lenMax == 1: 
        minimumNumber = sum([x for x in arr if x < max(arr)]) 
    else:
        minimumNumber = sum([x for x in arr if x < max(arr)]) + ((lenMax-1)*max(arr))
        
    print(f"{minimumNumber} {maximumNumber}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
