# SOC-EXCEL-CONVERT

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
|-e|--excel|Y|None|Specify the path to the excel file to be converted|
|-m|--mode|N|md|Specify the conversion format, optional parameters: md (markdown) and json. Do not pass the default to md. Currently only supports md;|
|-s|--sheets|N|''|Specify which sheet tables to output, default output all|
|-t|--target|N|./{fileName}/|Output target path. Do not pass the default current directory. If the directory does not exist, it will be created automatically.|



## Thank you

If you have any questions. 
please contact my email：tree@ejyi.com
