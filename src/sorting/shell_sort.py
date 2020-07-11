def launch_shell_sort(ds):
    gap = len(ds) // 2
    while gap > 0:
        for i in range(gap, len(ds)):
            temp = ds[i]
            j = i
            for j in range(i, gap - 1, -gap):
                if ds[j - gap] < temp:
                    break
                ds.swap(j, j - gap)
            # ds.set_value(j, temp)
        gap //= 2