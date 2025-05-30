# convert the document to markdown
import pymupdf4llm


def pdf_to_markdown(pdf_path):
    md_text = pymupdf4llm.to_markdown(pdf_path)
    return md_text


# python -m pdf_to_markdown
if __name__ == "__main__":
    md_text = pdf_to_markdown("1-1 买卖合同（通用版）.pdf")
    open("output.md", "w").write(md_text)