def partition(ds, low, hig):
    middle = ds.elements[(low + hig) // 2]
    i = low
    j = hig - 1
    while True:
        while ds.elements[i] < middle:
            i += 1
        while ds.elements[j] > middle:
            j -= 1
        if i >= j:
            return j
        if ds.elements[i] == ds.elements[j]:
            i += 1
        ds.swap(i, j)
            

def quick_sort(ds, low, hig):
    if low < hig:
        middle = partition(ds, low, hig)
        quick_sort(ds, low, middle)
        quick_sort(ds, middle + 1, hig)


def launch_quick_sort(ds):
    quick_sort(ds, 0, len(ds))