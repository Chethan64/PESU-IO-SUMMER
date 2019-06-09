li = list(map(int, input("Enter space separated values: ").rstrip().split()))
l = len(li)
li.sort()
ele = int(input("Enter the search element: "))

beg = 0
end = l - 1
pos = -1

while(beg <= end and pos == -1):
    mid = int((beg + end) / 2)
    if(li[mid] == ele):
        pos = mid
    elif(li[mid] > ele):
        end = mid - 1
    else:
        beg = mid + 1

if(pos == -1):
    print("Element not found")
else:
    print("Element found")
