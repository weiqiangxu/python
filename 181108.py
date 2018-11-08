from pyecharts import Bar
from pyecharts import Line

bar = Bar("我的第一个图表", "这里是副标题")
# 使用主题
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.render(r"bar.html")    # 生成本地 HTML 文件数据挖掘


# bar对象是最简单的柱状图 - 实际应用：微信书城关注人数、取关人数、渠道引流人数、

# 折线图

attr = ['1号','2号','3号','4号','5号','6号','7号','8号','9号','10号','11号','12号','13号','14号','15号','16号','17号','18号','19号','20号','21号','22号','23号','24号','25号','26号','27号','28号','29号','30号','31号']
v1 = [1, 2, 3, 4, 10, 100,5, 4, 3, 10, 10, 100,5, 20, 36, 10, 10, 100,5, 20, 36, 10, 10, 100,5, 20, 36, 10, 10, 100,0]
v2 = [55, 60, 16, 20, 15, 80,55, 60, 16, 20, 15, 80,55, 60, 16, 20, 15, 80,55, 60, 16, 20, 15, 80,55, 60, 16, 20, 15, 80,0]
line = Line("微信书城数据变动")
line.add("关注人数", attr, v1)
line.add("取关人数", attr, v2)
line.add("渠道用户", attr, v2)
line.render(r"line.html")