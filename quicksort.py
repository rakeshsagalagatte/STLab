def partition(Array , low , high):
    pivot = Array[high]
    i = low - 1
    for j in range(low,high):
        if Array[j] < pivot:
            i+=1
            Array[i],Array[j] = Array[j],Array[i]
    Array[i+1],Array[high] = Array[high],Array[i+1]
    return i+1

def quick_sort(Array , low , high):
    if low < high:
        par = partition(Array , low , high)
        quick_sort(Array , low , par-1)
        quick_sort(Array , par+1 , high)
def main():
    try:
        Array = list(map(int , input('Enter the array elements : ').split()))
    except:
        print('Invalid inputs')
        exit(0)
    print('Array Before sort : {}'.format(Array))
    quick_sort(Array,0,len(Array)-1)
    print('Array After sort : {}'.format(Array))

if __name__=='__main__':
    main()
