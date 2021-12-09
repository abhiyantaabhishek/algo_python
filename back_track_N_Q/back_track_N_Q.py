import os
import sys

sys.path.append("D:\\abhi\\algo\\algo_python")
from visualiser import Visualiser as vs

N = 4


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "gray",
    }
)
def back_track_N_Q(Q_position, x=0, level=0):
    if x == N:
        return True  # , Q_position
    ret = None
    # qp_ret = []
    for y in range(N):
        if is_safe(Q_position, x, y):
            Q_position[x][y] = 1
            ret = back_track_N_Q(Q_position, x + 1, level + 1)
        if ret == True:
            return True
        else:
            Q_position[x][y] = 0
    return ret  # , qp_ret


def is_safe(Q_position, x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    for i in range(N):
        if Q_position[i][y] == 1:
            return False
        if Q_position[x][i] == 1:
            return False
        for j in range(N):
            if Q_position[i][j] == 1:
                if abs(i - j) == abs(x - y):
                    return False
    return True


#%%

if __name__ == "__main__":
    Q_position = [[0 for i in range(N)] for i in range(N)]
    back_track_N_Q(Q_position)
    print(Q_position)
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "back_track_N_Q", "back_track_N_Q.png")
    )
    print("test")

