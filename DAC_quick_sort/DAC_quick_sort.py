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
def DAC_quick_sort(arr, p, q):
    if p == q:
        return
    else:
        mid = partition(arr, p, q)
        DAC_quick_sort(arr, p, mid)
        DAC_quick_sort(arr, mid + 1, q)
    return


def partition(arr, p, q):
    i = p
    pivot = arr[p]
    for j in range(p + 1, q + 1):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i


if __name__ == "__main__":
    arr = [50, 80, 90, 10, 8, 29, 89, 54, 16]
    ret = DAC_quick_sort(arr, 0, len(arr) - 1)
    print(arr, ret)
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "DAC_quick_sort", "DAC_quick_sort.png")
    )

