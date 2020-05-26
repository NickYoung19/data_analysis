# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : matplot_pie.py  v1.0
# @Desc        :《matplotlib 饼图绘图步骤》
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-26 11:49:34
# Copyright (C) 2020 Nick Ltd. All rights reserved.
import matplotlib.pyplot as plt

# 案例: 展现每部电影的排片的占比
# 创建一个figure >>> figsize:指定图的长宽, dpi:图像的清晰度, 返回fig对象
plt.figure(figsize=(12, 8), dpi=100)

# 准备每部电影的名字，电影的排片场次
movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']
place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]

# 通过pie绘制饼图
"""
plt.pie(x, labels=,autopct=,colors)
    x: 数量，自动算百分比
    labels: 每部分名称
    autopct: 占比显示指定%1.2f%%
    colors: 每部分颜色
"""
plt.pie(place_count, labels=movie_name, autopct='%1.2f%%', colors=['b','r','g','y','c','m','y','k','c','g','g'])

# 指定显示的pie是正圆
plt.axis('equal')
# 图例显示
plt.legend(loc='best')
# 标题显示
plt.title("每部电影排片占比示意图")

# 指定保存图片边缘空白距离，并将绘制的图片保存到images目录
# plt.subplots_adjust(top=0.93, bottom=0.08, right=0.97, left=0.05, hspace=0, wspace=0)
# plt.margins(0, 0)
plt.savefig("../static/images/matplot_pie.png", dpi=300)

plt.show()
