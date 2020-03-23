def launch_insertion_sort(ds):
    for i in range(1, len(ds)):
        j = i
        while j > 0 and ds[j - 1] >= ds[j]:
            ds.swap(j - 1, j)
            j -= 1