def launch_bubble_sort(ds):
    for i in range(len(ds) - 1, 0, -1):
        for j in range(i):
            if ds[j + 1] < ds[j]:
                ds.swap(j + 1, j)