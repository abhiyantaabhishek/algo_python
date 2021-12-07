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
def dac_power(a, n):
    if n == 1:
        return a
    else:
        mid = n // 2
        b = dac_power(a, mid)
        if n % 2 == 0:
            return b * b
        else:
            return a * b * b


if __name__ == "__main__":
    p = dac_power(2, 6)
    print("2^6 = ", p)
    vs.write_image(
        os.path.join(os.getcwd(), "algo_python", "DAC_power", "DAC_power.png")
    )
    # vs.make_animation(
    #     os.path.join(os.getcwd(), "algo_python", "DAC_power", "DAC_power.gif"), delay=1,
    # )
