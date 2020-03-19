def merge(ds, l, m, r):
    left = ds.elements[l:m]
    left.append(float('inf'))
    right = ds.elements[m:r]
    right.append(float('inf'))
    i = 0
    j = 0
    for k in range(l, r):
        if left[i] <= right[j]:
            ds.set_value(k, left[i])
            i += 1
        else:
            ds.set_value(k, right[j])
            j += 1


def merge_sort(ds, l, r):
    if r - l < 2:
        return
    middle = (l + r) // 2
    merge_sort(ds, l, middle)
    merge_sort(ds, middle, r)

    merge(ds, l, middle, r)


def launch_merge_sort(ds):
    merge_sort(ds, 0, len(ds))