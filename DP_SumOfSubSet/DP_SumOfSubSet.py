import os
import sys

sys.path.append("D:\\abhi\\algo\\algo_python")
from visualiser import Visualiser as vs

dynamic_map = {}


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def DP_SumOfSubSet(m, n, arr):  # m -> sum, n -> element no, arr-> weight
    if m == -1 or n == -1:
        return 0, []
    else:
        if arr[n] > m:
            if (m, n - 1) not in dynamic_map:
                dynamic_map[(m, n - 1)] = DP_SumOfSubSet(m, n - 1, arr)
            return dynamic_map[(m, n - 1)]  # do not take object
        else:
            if (m - arr[n], n - 1) not in dynamic_map:
                dynamic_map[(m - arr[n], n - 1)] = DP_SumOfSubSet(
                    m - arr[n], n - 1, arr
                )
            p1, sel1 = dynamic_map[(m - arr[n], n - 1)]  # take object
            p1 = p1 + arr[n]
            sel1 = sel1 + [n]

            if (m, n - 1) not in dynamic_map:
                dynamic_map[(m, n - 1)] = DP_SumOfSubSet(m, n - 1, arr)
            p2, sel2 = dynamic_map[(m, n - 1)]  # do not take object
            if p1 > p2:
                return p1, sel1
            else:
                return p2, sel2


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def NON_DP_SumOfSubSet(m, n, arr):  # m -> capacity, n -> object no, arr-> weight
    if m == -1 or n == -1:
        return 0, []
    else:
        if arr[n] > m:
            return NON_DP_SumOfSubSet(m, n - 1, arr)  # do not take object
        else:
            p1, sel1 = NON_DP_SumOfSubSet(m - arr[n], n - 1, arr)  # take object
            p1 = p1 + arr[n]
            sel1.append(n)
            p2, sel2 = NON_DP_SumOfSubSet(m, n - 1, arr)  # do not take object
            if p1 > p2:
                return p1, sel1
            else:
                return p2, sel2


if __name__ == "__main__":
    m = 300
    arr = [50, 90, 200, 45, 15, 100, 70]

    # m = 10
    # arr = [2, 1, 5, 4]

    print(DP_SumOfSubSet(m, len(arr) - 1, arr))
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "DP_SumOfSubSet", "DP_SumOfSubSet.png")
    )

    # print(NON_DP_SumOfSubSet(m, len(arr) - 1, arr))
    # vs.write_image(
    #     os.path.join(
    #         os.getcwd(), "algo_python", "DP_SumOfSubSet", "NON_DP_SumOfSubSet.png"
    #     )
    # )
