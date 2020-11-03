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
|-e|--excel|Y|None|指定需要转换的excel文件路径，如果不指定则从剪贴板中获取excel表格内容|
|-m|--mode|N|md|指定转换格式, 可选参数: md(markdown)和json. <br />不传默认为md. 目前仅支持md;|
|-s|--sheets|N|''|指定输出哪些sheet表格, 不传输出所有;|
|-t|--target|N|./{fileName}/|输出目标路径. 不传默认当前目录. <br />如果目录不存在则会自动创建;|
|-c|--copy|N|''|填入 "copy" 输出剪贴板中转义后的markdown表格内容.Default not output. |

### 查看结果
```bash
more demo1/test1.md 
```

```markdown
|短参数名|长参数名|是否必传|默认值|描述|
|:--|:--|:--:|:--:|:--|
|-e|--excel|Y||指定需要转换的excel文件路径|
|-m|--mode|N|md|指定转换格式,&nbsp;可选参数:&nbsp;md(markdown)和json.&nbsp;<br />不传默认为md.&nbsp;目前仅支持md;|
|-s|--sheets|N|''|指定输出哪些sheet表格,&nbsp;不传输出所有;|
|-t|--target|N|./{fileName}/|输出目标路径.&nbsp;不传默认当前目录.&nbsp;<br />如果目录不存在则会自动创建;|

```

## License

[Apache 2.0 License.](https://github.com/treeyh/soc-excel-convert/blob/master/LICENSE)

## 感谢使用

如有疑问可联系：tree@ejyi.com