from pyecharts.charts import Bar

(Bar()
 .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
 .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
 .add_yaxis("商家B", [6, 23, 30, 15, 70, 80])
 .render()
 )

# bar.render_notebook()


# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [6, 23, 30, 15, 70, 80])
# bar.render()
