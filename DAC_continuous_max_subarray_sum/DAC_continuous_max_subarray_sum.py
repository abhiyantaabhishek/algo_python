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
def DAC_continuous_max_subarray_sum(arr, i, j):
    if i == j:
        return arr[i], (i, j)
    else:
        mid = i + (j - i) // 2
        ls, (ls_lbsi, ls_rbsi) = DAC_continuous_max_subarray_sum(arr, i, mid)
        rs, (rs_lbsi, rs_rbsi) = DAC_continuous_max_subarray_sum(arr, mid + 1, j)
        continuous_sum, lbsi, rbsi = cross_sum(arr, i, mid, j)
        if ls > rs and ls > continuous_sum:
            ret = ls, (ls_lbsi, ls_rbsi)
        elif rs > continuous_sum and rs > ls:
            ret = rs, (rs_lbsi, rs_rbsi)
        else:
            ret = continuous_sum, (lbsi, rbsi)

    return ret


def cross_sum(arr, i, mid, j):
    lts = 0  # left total sum
    lbs = 0  # left best sum
    lbsi = -1  # left best sum index
    for k in range(mid, i - 1, -1):
        lts = lts + arr[k]
        if lts > lbs:
            lbs = lts
            lbsi = k
    rts = 0  # reft total sum
    rbs = 0  # reft best sum
    rbsi = -1  # reft best sum index
    for k in range(mid + 1, j + 1):
        rts = rts + arr[k]
        if rts > rbs:
            rbs = rts
            rbsi = k
    if lbsi == -1 and rbsi != -1:
        lbsi = rbsi
    elif rbsi == -1 and lbsi != -1:
        rbsi = lbsi
    elif lbsi == -1 and rbsi == -1:
        lbsi = rbsi = mid

    return lbs + rbs, lbsi, rbsi


if __name__ == "__main__":
    arr = [20, -25, 130, -80, 10, 90, -43, 12, -40]
    print(DAC_continuous_max_subarray_sum(arr, 0, len(arr) - 1))
    vs.write_image(
        os.path.join(
            os.getcwd(),
            "algo_python",
            "DAC_continuous_max_subarray_sum",
            "DAC_continuous_max_subarray_sum.png",
        )
    )
