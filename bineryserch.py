

a=[1,23,4,7,67,5,6,86]
key = int(input("enter key [1,23,4,7,67,5,6,86] : "))

def binary_s(a,key):
    beg= 0
    end= len(a)-1
    while beg <= end:
        mid = int((beg+end)/2)
        if key==a[mid]:
            return mid
        elif key<a[mid]:
            end = mid-1
        else:
            beg = mid+1
        print(key,"could not found")
        return -1
print(binary_s(a, key))
