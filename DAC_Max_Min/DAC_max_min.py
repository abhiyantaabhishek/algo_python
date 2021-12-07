import sys
import os

sys.path.append("D:\\abhi\\algo\\algo_python")
from visualiser import Visualiser as vs
import os


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def dac_max_min(arr, i, j):
    if i == j:
        max_ = min_ = i
    elif i == j - 1:
        if arr[i] > arr[j]:
            max_ = arr[i]
            min_ = arr[j]
        else:
            max_ = arr[j]
            min_ = arr[i]
    else:
        mid = (i + j) // 2
        max_1, min_1 = dac_max_min(arr, i, mid)
        max_2, min_2 = dac_max_min(arr, mid + 1, j)
        if max_1 > max_2:
            max_ = max_1
        else:
            max_ = max_2
        if min_1 < min_2:
            min_ = min_1
        else:
            min_ = min_2
    return max_, min_


def main():
    arr = [2, 5, 7, 9, 6, 3, 5, 7, 10]
    max_, min_ = dac_max_min(arr, 0, len(arr) - 1)
    print("Max and Min Values are :", max_, min_)
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "DAC_Max_Min", "dac_max_min.png")
    )
    # vs.make_animation(
    #     os.path.join(os.getcwd(), "algo_python", "DAC_Max_Min", "dac_max_min.gif"),
    #     delay=1,
    # )


if __name__ == "__main__":
    main()
