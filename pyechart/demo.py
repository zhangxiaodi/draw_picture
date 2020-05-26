

'''
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Page,Bar
from pyecharts.charts import Scatter
from pyecharts.render import make_snapshot
import tushare as ts
bar = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-jupyter渲染图片"))
        .render("geo_base.html")
    )
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
scatter = Scatter("散点图", "一年的降水量与蒸发量")
# xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
scatter.add("降水量与蒸发量的散点分布", data1,data2,xaxis_name="降水量",yaxis_name="蒸发量",
            yaxis_name_gap=40)
scatter.render()
# bar.render_notebook()
'''

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot

from snapshot_selenium import snapshot

def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

make_snapshot(snapshot, bar_chart().render(), "bar0.png")





