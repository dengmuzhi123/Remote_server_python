@[TOC](目录)
# 介绍
本项目是用python开发的telnet和ssh工具，可以实现自动化运维和远程连接服务器等功能。
# 编译
首先需要安装python3.12及以上版本。使用pip安装库

```shell
pip install paramiko
pip install PyQt6
pip install pyinstaller
```
在项目文件夹中打开终端，输入

```powershell
pyinstall -F main.py
```
即可在dist文件夹内发现编译好的exe文件。
或者在发行版直接下载二进制文件
