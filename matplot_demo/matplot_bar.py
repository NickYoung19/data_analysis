# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : matplot_bar.py  v1.0
# @Desc        :《matplotlib 柱状图绘图步骤》
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-11 14:10:10
# Copyright (C) 2020 Nick Ltd. All rights reserved.
import matplotlib.pyplot as plt

"完成简单的条形图展现不同的电影票房之间的对比"
# 创建一个figure
plt.figure(figsize=(20, 8), dpi=80)

# 准备电影的名字以及电影的票房数据
movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
y = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]
# 放进横坐标的数字列表
x = range(len(movie_name))

# 画出条形图
plt.bar(x, y, width=0.5, color=['b', 'r', 'lightgreen', 'y', 'c', 'm', 'y', 'k', 'c', 'lightpink', 'lightblue'])

# 修改刻度名称
plt.xticks(x, movie_name)
plt.title("猫眼电影票房对比图示", fontsize=24)

# 指定保存图片边缘空白距离，并将绘制的图片保存到images目录
plt.subplots_adjust(top=0.93, bottom=0.06, right=0.97, left=0.03, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig("../static/images/matplot_bar.png", dpi=300)

plt.show()

"三部电影的首日和首周票房对比"
# plt.figure(figsize=(20, 8), dpi=80)
#
# movie_name = ['雷神3：诸神黄昏','正义联盟','寻梦环游记']
#
# first_day = [10587.6,10062.5,1275.7]
# first_weekend=[36224.9,34479.6,11830]
#
# x = range(len(movie_name))
#
# # 画出柱状图
# plt.bar(x, first_day, width=0.2, label="首日票房")
# # 首周柱状图显示的位置在首日的位置右边
# plt.bar([i+0.2 for i in x], first_weekend, width=0.2, label="首周票房")
#
# # 显示X轴中文，固定在首日和首周的中间位置
# plt.xticks([i+0.1 for i in x], movie_name)
# plt.legend(loc='best')
#
# plt.show()
