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
def DP_0_1_KnapSack(
    m, n, w, p
):  # m -> capacity, n -> object no, w-> weight , p-> profit
    if m == -1 or n == -1:
        return 0, []
    else:
        if w[n] > m:
            if (m, n - 1) not in dynamic_map:
                dynamic_map[(m, n - 1)] = DP_0_1_KnapSack(m, n - 1, w, p)
            return dynamic_map[(m, n - 1)]  # do not take object
        else:
            if (m - w[n], n - 1) not in dynamic_map:
                dynamic_map[(m - w[n], n - 1)] = DP_0_1_KnapSack(m - w[n], n - 1, w, p)
            p1, sel1 = dynamic_map[(m - w[n], n - 1)]  # take object
            p1 = p1 + p[n]
            sel1 += [n]
            if (m, n - 1) not in dynamic_map:
                dynamic_map[(m, n - 1)] = DP_0_1_KnapSack(m, n - 1, w, p)
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
def NON_DP_0_1_KnapSack(
    m, n, w, p
):  # m -> capacity, n -> object no, w-> weight , p-> profit
    if m == -1 or n == -1:
        return 0, []
    else:
        if w[n] > m:
            return NON_DP_0_1_KnapSack(m, n - 1, w, p)  # do not take object
        else:
            p1, sel1 = NON_DP_0_1_KnapSack(m - w[n], n - 1, w, p)  # take object
            p1 = p1 + p[n]
            sel1 += [n]
            p2, sel2 = NON_DP_0_1_KnapSack(m, n - 1, w, p)  # do not take object
            if p1 > p2:
                return p1, sel1
            else:
                return p2, sel2


if __name__ == "__main__":
    m = 16
    w = [5, 3, 2, 4, 5]
    p = [25, 70, 50, 10, 60]

    print(DP_0_1_KnapSack(m, len(w) - 1, w, p))
    vs.write_image(
        os.path.join(
            os.getcwd(), "algo_python", "DP_0_1_KnapSack", "DP_0_1_KnapSack.png"
        )
    )

    # print(NON_DP_0_1_KnapSack(m, len(w) - 1, w, p))
    # vs.write_image(
    #     os.path.join(
    #         os.getcwd(), "algo_python", "DP_0_1_KnapSack", "NON_DP_0_1_KnapSack.png"
    #     )
    # )

