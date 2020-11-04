#-*- encoding: utf-8 -*-

#!/usr/bin/env python


import argparse

import soc_excel_convert._internal.soc_excel_convert as sec



def read_args():
    ''' read command line args '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--excel", help="Excel file path.If it is empty, it will get excel data from the clipboard by default.")
    parser.add_argument("-m", "--mode", help = "Convert format.support:md (markdown); default md.", action="store_true", default = "md")
    parser.add_argument("-t", "--target", help="Target file path. Default ./{FileName}/ ", action="store_true", default = "")
    parser.add_argument("-s", "--sheets", help="Convert excel sheet name. Default all sheets. Multiple comma separated.", action="store_true",
                        default="")
    parser.add_argument("-p", "--paste", help = "Output clipboard contents.Default not output.",  action="store_true", default = False)

    return parser.parse_args()




def main(args=None):

    args = read_args()

    sec.run(args)

