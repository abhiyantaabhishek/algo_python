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
def DP_LCS(m, n, X, Y):  # call NON_DP_LCS for non_dp
    if m == -1 or n == -1:
        return 0, ""
    else:
        if X[m] == Y[n]:
            if (m - 1, n - 1) not in dynamic_map:
                dynamic_map[(m - 1, n - 1)] = DP_LCS(m - 1, n - 1, X, Y)
            len, seq = dynamic_map[(m - 1, n - 1)]
            return 1 + len, seq + X[m]
        else:
            if (m - 1, n) not in dynamic_map:
                dynamic_map[(m - 1, n)] = DP_LCS(m - 1, n, X, Y)
            len_a, seq_a = dynamic_map[(m - 1, n)]
            if (m, n - 1) not in dynamic_map:
                dynamic_map[(m, n - 1)] = DP_LCS(m, n - 1, X, Y)
            len_b, seq_b = dynamic_map[(m, n - 1)]
            if len_a > len_b:
                return len_a, seq_a
            else:
                return len_b, seq_b


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def NON_DP_LCS(m, n, X, Y):
    if m == -1 or n == -1:
        return 0, ""
    else:
        if X[m] == Y[n]:
            len, seq = NON_DP_LCS(m - 1, n - 1, X, Y)
            return 1 + len, seq + X[m]
        else:
            len_a, seq_a = NON_DP_LCS(m - 1, n, X, Y)
            len_b, seq_b = NON_DP_LCS(m, n - 1, X, Y)
            if len_a > len_b:
                return len_a, seq_a
            else:
                return len_b, seq_b


if __name__ == "__main__":
    X = ["A", "B", "A", "A"]
    Y = ["A", "B", "B", "B"]
    # X = ["A", "A", "A"]
    # Y = ["B", "B", "B"]
    print(DP_LCS(len(X) - 1, len(Y) - 1, X, Y))
    vs.write_image(os.path.join(os.getcwd(), "algo_python", "DP_LCS", "DP_LCS.png"))
    # print(NON_DP_LCS(len(X) - 1, len(Y) - 1, X, Y))
    # vs.write_image(os.path.join(os.getcwd(), "algo_python", "DP_LCS", "NON_DP_LCS.png"))
