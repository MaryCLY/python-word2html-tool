import docx


def word2html(input_path, output_path):
    try:
        document = docx.Document(input_path)
        output_file = open(output_path, 'w', encoding='utf-8')
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
        return f"转换完成，文件为{output_path}"
    except:
        return "出错！"
