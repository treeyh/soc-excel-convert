#-*- encoding: utf-8 -*-

import os
import sys

import argparse



from utils import excel_utils
from result_code import ResultCode







def print_msg(msg, result_code = None):
    print(msg)
    if None != result_code:
        sys.exit(result_code)


def read_args():
    ''' read command line args '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--excel", help="excel file path")
    parser.add_argument("-c", "--convert", help = "convert format.support:md (markdown); default md.", action="store_true", default = "md")
    parser.add_argument("-t", "--target", help="target file path. default ./{FileName}/ ", action="store_true", default = "")

    return parser.parse_args()





def run():
    args = read_args()

    if None == args.excel:
        print_msg('file path is none.', ResultCode.PARAMS_ERROR)

    if not os.path.isfile(args.excel):
        print_msg('file path is none.', ResultCode.EXCEL_FILE_NOT_EXIST)








if __name__ == '__main__':
    run()










