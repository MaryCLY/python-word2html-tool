import docx
import argparse

parser = argparse.ArgumentParser(description="将docx文件转换成html结构")
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

document = docx.Document(args.input_file)
output_file = open(args.output_file, 'w', encoding='utf-8')
for p in document.paragraphs:
    p_text = ""
    for run in p.runs:
        run_text = run.text
        if run.bold:
            run_text = f"<strong>{run_text}</strong>"
        if run.italic:
            run_text = f"<em>{run_text}</em>"
        p_text += run_text
    output_file.write(f"<p>{p_text}</p>\n")
output_file.close()
print('转换完成')