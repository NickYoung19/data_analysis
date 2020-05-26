# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : matplot_pie_hj_spider.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-26 12:01:18
# Copyright (C) 2020 Nick Ltd. All rights reserved.
# -*- coding: utf-8 -*-
import requests
import matplotlib.pyplot as plt
from lxml import etree


class HuoJiangSpider(object):
    """
    长春理工大学历年获奖分析
    """
    def __init__(self):
        self.url = "https://www.cust.edu.cn/szdw/jxcg/index.htm"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def send_request(self):
        """
        请求数据
        :return: result对象
        """
        result = requests.get(self.url, headers=self.headers)

        return result

    def parse_data(self, result_str):
        """
        解析数据
        :param result_str:
        :return: province_num, nation_num, province_edu_num, nation_edu_num, time_names_dict
        """
        element_obj = etree.HTML(result_str)
        # 按级别分
        grade = element_obj.xpath('//table/tbody/tr/td[6]/div/text()')      # 提取所有级别
        province_num = len([i for i in grade if '省' in i])                 # 省级 数量
        nation_num = len([i for i in grade if '国' in i])                   # 国级 数量

        # 按颁发单位分
        award_units = element_obj.xpath('//table/tbody/tr/td[3]/div/text()')  # 提取所有颁发单位
        province_edu_num = len([i for i in award_units if '厅' in i])       # 颁发单位为省厅 数量
        nation_edu_num = len([i for i in award_units if '部' in i])         # 颁发单位为国部 数量

        # 按颁发时间分
        award_time = element_obj.xpath('//table/tbody/tr/td[4]/div/text()')
        temp_award_time = list(set(award_time))                             # 去重
        # temp_award_time: ['2001', '1989', '1997', '1993', '2009', '2007', '2006', '2008', '2004', '2005', '2010']
        time_names_dict = {'Year_' + i: 0 for i in temp_award_time}         # 定义颁发时间字典
        for i in time_names_dict:
            time_names_dict[i] = award_time.count(i[5:])                    # 将颁发时间对应的数量更新到颁发时间字典

        return province_num, nation_num, province_edu_num, nation_edu_num, time_names_dict

    def draw_pic(self, province_num, nation_num, province_edu_num, nation_edu_num, time_names_dict):
        """
        数据可视化
        :param province_num:
        :param nation_num:
        :param province_edu_num:
        :param nation_edu_num:
        :param time_names_dict:
        :return:
        """
        plt.figure(figsize=(18, 8), dpi=90)
        # 奖项颁发部门分布饼状图
        plt.subplot(1, 3, 1)
        plt.title('奖项颁发部门分布饼状图')
        labels = '省教育厅', '国家教育部'
        sizes = province_edu_num, nation_edu_num
        colors = 'lightgreen', 'lightskyblue'
        explode = 0, 0
        plt.pie(sizes, explode=explode, labels=labels,
                colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.legend(loc='upper center')

        # 奖项级别分布饼状图
        plt.subplot(1, 3, 2)
        plt.title('奖项级别分布饼状图')
        labels = '国家级', '省级'
        sizes = nation_num, province_num
        colors = 'pink', 'cyan'
        explode = 0, 0
        plt.pie(sizes, explode=explode, labels=labels,
                colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.legend(loc='upper center')

        # 奖项颁发时间分布饼状图
        plt.subplot(1, 3, 3)
        plt.title('奖项颁发时间分布饼状图')
        labels = [i for i in time_names_dict.keys()]
        sizes = [i for i in time_names_dict.values()]
        colors = '#f0f8ff', '#8dc63f', '#ffe4e1', '#faf0e6', '#e6e6fa', '#bc8f8f', '#fa8072'
        explode = [0 for i in time_names_dict.keys()]
        plt.pie(sizes, explode=explode, labels=labels,
                colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.legend(loc='upper center', ncol=3)

        plt.savefig("../static/images/matplot_pie_hj_spider.png", dpi=300)

        plt.show()

    def main(self):
        """
        调度方法
        :return:
        """
        # 发起请求
        result_str = self.send_request().content.decode()
        # 解析数据
        province_num, nation_num, province_edu_num, nation_edu_num, time_names_dict = self.parse_data(result_str)
        # 数据可视化
        self.draw_pic(province_num, nation_num, province_edu_num, nation_edu_num, time_names_dict)


if __name__ == '__main__':
    HuoJiangSpider().main()
