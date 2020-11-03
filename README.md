# 云海Excel转换 SOC-EXCEL-CONVERT

Convert Excel to markdown, json ...

[中文](https://github.com/treeyh/soc-excel-convert/blob/master/docs/zh-CN/README.md)

## INSTALL

```bash
pip install soc-excel-convert
```

## USE

Simple to use, the command is as follows:
```bash
soc-excel-convert -e ./test/excel/demo1.xlsx 
```
The file name will be created in the current directory with the same name directory, which stores the generated markdown file, one file per sheet, named after the sheet name.

Parameter Description:

|Short parameter name|Long parameter name|Must|Default|Description|
|:--|:--|:--:|:--:|:--|
|-e|--excel|Y|None|Specify the path to the excel file to be converted.If it is empty, it will get excel data from the clipboard by default.|
|-m|--mode|N|md|Specify the conversion format, optional parameters: md (markdown) and json. Do not pass the default to md. Currently only supports md;|
|-s|--sheets|N|''|Specify which sheet tables to output, default output all|
|-t|--target|N|./{fileName}/|Output target path. Do not pass the default current directory. If the directory does not exist, it will be created automatically.|
|-c|--copy|N|''|Fill in "copy" to output the escaped markdown table content in the clipboard.Default not output. |


### View Results 
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

## Thank you

If you have any questions. 
please contact my email：tree@ejyi.com
