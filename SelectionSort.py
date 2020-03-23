def launch_selection_sort(ds):
    for i in range(0, len(ds)):
        for j in range(i + 1, len(ds)):
            if ds.elements[j] < ds.elements[i]:
                ds.swap(j, i)
        