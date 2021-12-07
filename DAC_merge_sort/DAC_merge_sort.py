import os
import sys

sys.path.append("D:\\abhi\\algo\\algo_python")
from visualiser import Visualiser as vs


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def DAC_merge_sort(arr, i, j):
    if i == j:
        return arr[i : j + 1]
    else:
        mid = i + (j - i) // 2
        DAC_merge_sort(arr, i, mid)
        DAC_merge_sort(arr, mid + 1, j)
        merge(arr, i, mid, mid + 1, j)
    return arr[i : j + 1]


def merge(arr, i, j, k, l):
    arr1 = arr[i : j + 1]
    arr2 = arr[k : l + 1]
    merged_arr = []
    ind1 = ind2 = 0
    for _ in range(len(arr1) + len(arr2)):
        if ind1 < len(arr1) and ind2 < len(arr2):
            if arr1[ind1] < arr2[ind2]:
                merged_arr.append(arr1[ind1])
                ind1 += 1
            else:
                merged_arr.append(arr2[ind2])
                ind2 += 1
        elif ind1 < len(arr1):
            merged_arr.append(arr1[ind1])
            ind1 += 1
        elif ind2 < len(arr2):
            merged_arr.append(arr2[ind2])
            ind2 += 1
    arr[i : l + 1] = merged_arr
    print(merged_arr)


if __name__ == "__main__":
    arr = [4, 6, 3, 7, 4, 8]
    DAC_merge_sort(arr, 0, len(arr) - 1)
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "DAC_merge_sort", "DAC_merge_sort.png")
    )
    print(arr)
