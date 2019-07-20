# 云海Excel转换

将Excel内容转换成Markdown表格样式

[English](https://github.com/treeyh/soc-excel-convert/blob/master/README.md)

## 安装

```bash
pip install soc-excel-convert
```

## 使用

简单使用,命令如下:
```bash
soc-excel-convert -e ./test/excel/demo1.xlsx 
```
将在当前目录下创建文件名同名目录, 里面存放生成的markdown文件, 每个sheet一个文件, 以sheet名命名.

参数说明:

|短参数名|长参数名|是否必传|默认值|描述|
|:--|:--|:--:|:--:|:--|
|-e|--excel|Y|None|指定需要转换的excel文件路径|
|-m|--mode|N|md|指定转换格式, 可选参数: md(markdown)和json. 不传默认为md. 目前仅支持md;|
|-s|--sheets|N|''|指定输出哪些sheet表格, 不传输出所有;|
|-t|--target|N|./{fileName}/|输出目标路径. 不传默认当前目录. 如果目录不存在则会自动创建;|

