#
# MAINTAINER        Nick.Y.Peng <PENGYANGALP@GMAIL.COM>
# DOCKER-VERSION    1.0
#
# Dockerizing Ubuntu16.04: Dockerfile for building Python3_dev images
#
# 构建Docker镜像必须要有一个基础镜像，即父镜像(可从官网pull也可自己制作)
FROM ubuntu:16.04
# 指定维护者信息
MAINTAINER Nick.Y.Peng <PENGYANGALP@GMAIL.COM>

# 安装常用工具和Python环境
RUN apt-get update && apt-get install -y iputils-ping wget net-tools vim python3.5 python3-pip
# 配置pip阿里镜像源
#RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
#RUN pip3 config set install.trusted-host mirrors.aliyun.com

# 更新pip至最新版本
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
# 安装我们开发使用Python包
RUN pip3 install requests lxml matplotlib==2.0.2 pandas==0.20.3 tables==3.4.2 jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 复制、解压、安装TA_Lib依赖库
ADD ta-lib-0.4.0-src.tar.gz /opt
RUN cd /opt/ta-lib/ && ./configure --prefix=/usr && make && make install
# 安装TA_Lib包，另numpy包会作为依赖自动安装
RUN pip3 install TA_Lib -i https://pypi.tuna.tsinghua.edu.cn/simple/

# ===== The below are some common usage. =====
## 设置时区环境变量（ENV环境变量在Dockerfile中可以写多个）
## 这些指定的环境变量，后续可以被RUN指令使用，容器运行起来之后，也可以在容器中获取这些环境变量
#ENV TZ "Asia/Shanghai"
#ENV TERM xterm
#
## ADD：添加/拷贝文件到container里面，还有一个拷贝命令是COPY
## 两者的区别如下：
## 前者比后者多两个功能；
##     1. 可直接将url对应的文件直接复制到container里面；
##     2. 如果复制的是tar压缩包文件，用ADD拷贝结束后会自动帮我们解压；
#ADD aliyun-mirror.repo /etc/yum.repos.d/CentOS-Base.repo
#ADD aliyun-epel.repo /etc/yum.repos.d/epel.repo
#
## RUN 后面是要执行的命令，每执行一条指令就是一层，所以Dockerfile采用的是分层的技术
## 安装进程管理工具
#RUN pip install supervisor
## 添加进程管理工具的主配置文件到指定目录下，一般是/etc目录
#ADD supervisord.conf /etc/supervisord.conf
## 1. 为进程管理工具新建一个目录，用来存放启动其他服务的配置文件
## 2. 新建进程管理日志目录
#RUN mkdir -p /etc/supervisor.conf.d && \
#    mkdir -p /var/log/supervisor
#
#EXPOSE 22   # Docker服务器开放的端口，供容器外部连接使用(在启动容器时做端口映射)
#
## 如果有多条ENTRYPOINT语句，那么只有最后一条生效
## ENTRYPOINT指的是container每次启动的时候需要执行的命令
#ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
