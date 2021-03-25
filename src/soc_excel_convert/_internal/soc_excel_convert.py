#-*- encoding: utf-8 -*-

import os
import sys
import html

import argparse
import pyperclip


from soc_excel_convert._utils import excel_utils, file_utils, str_utils
from soc_excel_convert._internal.result_code import ResultCode




def print_msg(msg):
    print(str_utils.json_encode(msg))


def read_args():
    ''' read command line args '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--excel", help="Excel file path. If it is empty, it will get excel data from the clipboard by default.")
    parser.add_argument("-m", "--mode", help = "Convert format.support:md (markdown); default md.", action="store_true", default = "md")
    parser.add_argument("-t", "--target", help="Target file path. Default ./{FileName}/ ", action="store_true", default = "")
    parser.add_argument("-s", "--sheets", help="Convert excel sheet name. Default all sheets. Multiple comma separated.", action="store_true",
                        default="")
    parser.add_argument("-c", "--copy", help = "Output clipboard contents.Default not output.", action="store_true", default = "")

    return parser.parse_args()




'''
content内容结构：

{
    "sheetName": {
        "maxBeginIndex": 1,
        "maxEndIndex": 3,
        "title": {
            "beginIndex": 1,
            "endIndex": 3,
            "data": [
                {
                    "content": "name1",
                    "horizontal": "left",
                    "link": "http://xxx.xxx.xxx/"
                },
                {
                    "content": "name2",
                    "horizontal": "middle",
                    "link": "http://xxx.xxx.xxx/"
                },
                {
                    "content": "name3",
                    "horizontal": "right",
                    "link": "http://xxx.xxx.xxx/"
                }
            ]
        },
        "data": [
            {
                "beginIndex": 1,
                "endIndex": 3,
                "data": [
                    {
                        "content": "name1",
                        "link": "http://xxx.xxx.xxx/"
                    },
                    {
                        "content": "name2",
                        "link": "http://xxx.xxx.xxx/"
                    },
                    {
                        "content": "name3",
                        "link": "http://xxx.xxx.xxx/"
                    }
                ]
            },
            {
                "beginIndex": 1,
                "endIndex": 3,
                "data": [
                    {
                        "content": "name1",
                        "link": "http://xxx.xxx.xxx/"
                    },
                    {
                        "content": "name2",
                        "link": "http://xxx.xxx.xxx/"
                    },
                    {
                        "content": "name3",
                        "link": "http://xxx.xxx.xxx/"
                    }
                ]
            }
        ]
    }
}
'''


def read_excel(excelPath, sheets):
    ''' 读取excel内容 '''
    wb = excel_utils.open_excel(excelPath)

    sheetNames = excel_utils.get_sheet_names(wb)

    contents = {}

    for name in sheetNames:
        if len(sheets) > 0 and name not in sheets:
            continue
        contents[name] = read_excel_content(wb, name)
    return contents


def read_excel_content(wb, sheetName):
    ''' 读取excel具体内容 '''
    ws = excel_utils.get_sheet_by_name(wb, sheetName)

    rows = ws.values

    rowIndex = 0
    content = {
        "maxBeginIndex": 0,
        "maxEndIndex": 0,
        "title": None,
        "data": []
    }

    for rowInfo in rows:
        rowIndex += 1
        row = {
            "beginIndex": 0,
            "endIndex": 0,
            "data": []
        }
        colIndex = 0
        for value in rowInfo:
            colIndex += 1

            if row['beginIndex'] < 1 and (value is None or value == ""):
                continue

            row['beginIndex'] = colIndex if row['beginIndex'] < 1 else row['beginIndex']
            row['endIndex'] = colIndex if (value is not None and value != "") else row['endIndex']

            if value is None:
                value = ""

            columnName = excel_utils.get_column_code_by_index(colIndex)
            cell = ws[columnName + str(rowIndex)]


            link = None
            if None is not cell.hyperlink:
                link = cell.hyperlink.target if None is not cell.hyperlink.target and "" != cell.hyperlink.target else None

            if content['maxBeginIndex'] < 1:
                # 还没有标题，需要分析标题对齐位置

                info = {'content': value, 'horizontal': cell.alignment.horizontal, 'link': link}

                row["data"].append(info)
                pass
            else:
                # 已有标题
                row["data"].append({
                    'content': value,
                    'link': link
                })


        row['data'] = row['data'][:(row['endIndex'] - row['beginIndex'] + 1)]
        content['maxBeginIndex'] = row['beginIndex'] if (content['maxBeginIndex'] < 1 or row['beginIndex'] < content['maxBeginIndex']) else content['maxBeginIndex']
        content['maxEndIndex'] = row['endIndex'] if row['endIndex'] > content['maxEndIndex'] else content['maxEndIndex']


        if row['beginIndex'] < 1 and content['title'] is None:
            continue
        elif content['title'] is None:
            content['title'] = row
        else:
            content['data'].append(row)

    return content


def get_markdown_horizontal(horizontal):
    ''' 获得列对齐策略 '''
    if None == horizontal or "" == horizontal:
        return  ':--'
    elif horizontal == 'left':
        return ':--'
    elif horizontal == 'center':
        return ':--:'
    else:
        return '--:'

def format_markdown_content(content):
    ''' 格式化markdown表格内容 '''
    c = str(content.get('content', ''))
    link = content.get('link', None)
    c = format_markdown_by_content(c)

    if link is None or '' == link:
        return c
    else:
        return "[%s](%s)" % (c, link)


def format_markdown_by_content(content):
    ''' 格式化markdown表格内容 '''
    content = content.replace('&', '&amp;')
    content = content.replace('"', '&quot;')
    content = content.replace('|', '&vert;') # &brvbar;  &vert;
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')
    content = content.replace(' ', '&nbsp;')
    content = content.replace('\r\n', '<br />')
    content = content.replace('\n', '<br />')

    return content


def build_content(content, mode):
    ''' 构造保存文件内容 '''
    if mode == 'md':
        md = ''
        linesep = '\n'
        sep = '|'
        maxBeginIndex = content['maxBeginIndex']
        maxEndIndex = content['maxEndIndex']

        if content['maxBeginIndex'] < 1:
            return md

        title = sep
        horizontal = sep
        beginIndex = content['title']['beginIndex']

        for i in range(maxBeginIndex, maxEndIndex + 1):
            if i < beginIndex:
                title += sep
                horizontal += get_markdown_horizontal('') + sep
                continue
            idx = i - beginIndex
            if idx < len(content['title']['data']):
                title += format_markdown_content(content['title']['data'][idx])
                horizontal += get_markdown_horizontal(content['title']['data'][idx]['horizontal'])
            title += sep
            horizontal += sep

        md = title + linesep + horizontal + linesep

        for row in content['data']:
            beginIndex = row['beginIndex']
            c = sep
            for i in range(maxBeginIndex, maxEndIndex + 1):
                if i < beginIndex:
                    title += sep
                    continue
                idx = i - beginIndex
                if idx < len(row['data']):
                    c += format_markdown_content(row['data'][idx])
                c += sep
            md += c + linesep
        return md
    else:
        return ''



def save_excel_info(contents, path, mode):
    '''保存转换的excel信息'''

    # 创建文件夹
    file_utils.make_folders(path)

    # 保存文件
    for k, content in contents.items():
        c = build_content(content, mode)
        filePath = os.path.join(path, k+'.md')
        file_utils.write_file(filePath, c)


def format_clipboard_quotes(c):
    ''' 转义剪贴板中单元格内容，为了适配单元格内容中有换行符前后默认会加引号 '''
    if len(c) >= 6:
        if c[:3] == '"""' and c[-3:] == '"""':
            return c[3:-3]
    if len(c) >= 3:
        if c[:1] == '"' and c[-1:] == '"':
            return c[1:-1]
    return c


def format_clipboard_html_quotes(c):
    ''' 转义剪贴板中单元格内容, html转义后，为了适配单元格内容中有换行符前后默认会加引号 '''
    if len(c) >= 11:
        if c[:6] == '&quot;' and c[-6:] == '&quot;':
            return c[6:-6]
    return c

def clipboard_to_markdown(cb):
    ''' 将剪贴板中的excel表格内容转义成markdown内容 '''
    content = ''
    index = 0
    for line in cb.split('\r\n'):
        if line.strip() == '':
            continue

        ls = format_markdown_by_content(line).split('\t')
        for l in ls:
            content += '| ' + format_clipboard_html_quotes(l) +' '
        content += '|\n'

        if index == 0:
            # 补头
            for l in ls:
                content += '|:--'
            content += '|\n'
        index += 1
    pyperclip.copy(content)
    return 0


def run(args):

    cb = pyperclip.paste()
    if None == args.excel:
        if cb == None or cb == '':
            print_msg('file path or clipboard is none.')
            return ResultCode.PARAMS_ERROR
        else:
            result = clipboard_to_markdown(cb)
            if True == args.paste:
                pyperclip.paste()
            return result

    if not os.path.isfile(args.excel):
        print_msg('file path is none.')
        return ResultCode.EXCEL_FILE_NOT_EXIST

    sheets = []
    if args.sheets is not None and args.sheets != '':
        sheets = args.sheets.split(',')

    contents = read_excel(args.excel, sheets)

    target = args.target
    if None == args.target or "" == args.target:
        target = os.path.join('./', file_utils.get_file_name_no_suffix(args.excel))

    mode = args.mode
    if mode != "md":
        mode = "md"
    save_excel_info(contents, target, args.mode)

    return 0










