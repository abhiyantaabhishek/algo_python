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
def DAC_Binary_search(arr, i, j, x):
    # if i == j:
    #     if arr[i] == x:
    #         return i
    #     else:
    #         return -1
    if i > j:
        return -1
    else:
        # mid = (i + j) // 2
        mid = i + (j - i) // 2
        if x == arr[mid]:
            ret = mid
        elif x <= arr[mid]:
            ret = DAC_Binary_search(arr, i, mid - 1, x)
        else:
            ret = DAC_Binary_search(arr, mid + 1, j, x)
    return ret


if __name__ == "__main__":
    array = [3, 4, 5, 7, 9, 10, 30, 44, 55, 68, 79]
    ret = DAC_Binary_search(array, 0, len(array) - 1, 55)
    print("Search index = ", ret)
    vs.write_image(
        os.path.join(
            os.getcwd(), "algo_python", "DAC_Binary_search", "DAC_Binary_search.png"
        )
    )

