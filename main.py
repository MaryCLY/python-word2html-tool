import argparse
from word2html import word2html


parser = argparse.ArgumentParser(description="将docx文件转换成html结构")
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

print(word2html(args.input_file, args.output_file))
