"""
 * @file   : BarChart.py
 * @time   : 14:40
 * @date   : 2023/6/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pandas as pd
from matplotlib import pyplot as plt

import pynimate as nim

df = pd.DataFrame(
    {
        "time": ["1960-01-01", "1961-01-01", "1962-01-01"],
        "Afghanistan": [1, 2, 3],
        "Angola": [2, 3, 4],
        "Albania": [1, 2, 5],
        "USA": [5, 3, 4],
        "Argentina": [1, 4, 5],
    }
).set_index("time")

cnv = nim.Canvas()
bar = nim.Barhplot.from_df(df, "%Y-%m-%d", "2d")
bar.set_time(callback=lambda i, datafier: datafier.data.index[i].year)
cnv.add_plot(bar)
cnv.animate()
plt.show()
