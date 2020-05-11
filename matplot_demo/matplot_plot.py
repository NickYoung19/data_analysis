# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : matplot_plot.py  v1.0
# @Desc        :《matplotlib 折线图绘图步骤》
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-04 13:13:20
# Copyright (C) 2020 Nick Ltd. All rights reserved.
import matplotlib.pyplot as plt
import random

"Demo1: 画出温度变化图"
# 创建一个figure >>> figsize:指定图的长宽, dpi:图像的清晰度, 返回fig对象
plt.figure(figsize=(16, 8), dpi=80)

# 准备x, y坐标的数据
x = range(60)
# 生成郑州的温度
y_zhengzhou = [random.uniform(15, 18) for i in x]
# 生成信阳的温度
y_xinyang = [random.uniform(10, 13) for j in x]

# 构造中文列表的字符串
x_ch = [u"11点{}分".format(i) for i in x]
y_ticks = range(40)

# 修改x, y坐标的刻度
plt.xticks(x[::5], x_ch[::5])
plt.yticks(y_ticks[::5])

# 增加标题、x轴y轴描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点0分到12点之间的温度变化图示", fontsize=24)

# 绘制折线图
plt.plot(x, y_zhengzhou, label="郑州")
# 使用plot可以多次画多个折线
plt.plot(x, y_xinyang, color='r', linestyle='--', label="信阳")

# 添加图例
plt.legend(loc="best")

# 指定保存图片边缘空白距离，并将绘制的图片保存到images目录
plt.subplots_adjust(top=0.93, bottom=0.06, right=0.97, left=0.03, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig("../static/images/matplot_plot.png", dpi=300)

plt.show()

"""
Demo2：画出温度变化图,展现在两个不同axes里面
"""
# # 创建一个figure
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)
#
# # 准备x, y坐标的数据
# x = range(60)
# # y的刻度范围
# y_ticks = range(40)
# y_zhengzhou = [random.uniform(15, 18) for i in x]
#
# # 生成北京的温度
# y_xinyang = [random.uniform(1, 3) for i in x]
#
# # 构造中文列表的字符串
# x_ch = ["11点{}分".format(i) for i in x]
#
# # 画折线图
# axes[0].plot(x, y_zhengzhou, label="郑州")
# # 使用plot可以多次画多个折线
# axes[1].plot(x, y_xinyang, color='r', linestyle='--', label="信阳")
#
# # 美化x,y的刻度值
# # 第一个参数必须是刻度数字类型，第二个是对应着第一个数字的中文描述
# axes[0].set_xticks(x[::5], x_ch[::5])
# axes[0].set_yticks(y_ticks[::5])
#
# axes[1].set_xticks(x[::5], x_ch[::5])
# axes[1].set_yticks(y_ticks[::5])
#
# # 增加x,y描述信息和标题信息
# axes[0].set_xlabel("时间")
# axes[0].set_ylabel("温度")
#
# axes[1].set_xlabel("时间")
# axes[1].set_ylabel("温度")
#
# axes[0].set_title("中午11点0分到12点之间的温度变化图示")
# axes[1].set_title("中午11点0分到12点之间的温度变化图示")
#
# axes[0].legend(loc="best")
# axes[1].legend(loc="best")
#
# plt.show()
