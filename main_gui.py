from email import message
import PySimpleGUI as sg
from word2html import word2html


input_path = sg.popup_get_file(message='输入原始文件路径', title='输入文件',
                               default_extension='.docx', file_types=(('word文档', '.docx'), ))
# output_path = sg.popup_get_text(
#     message='输入导出代码文件路径(txt)', title='导出文件', default_text=input_path.replace('.docx', 'txt'),)
if input_path is not None:
    output_path = input_path.replace('.docx', '.txt')
    res = word2html(input_path, output_path)
    sg.popup_ok(res)
