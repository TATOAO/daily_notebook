
from langchain_community.document_loaders import PyMuPDFLoader


def pymupdf_parser(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    data = loader.load()
    return data


# python pymupdf_parser.py
if __name__ == "__main__":
    data = pymupdf_parser("1-1 买卖合同（通用版）.pdf")
    import ipdb; ipdb.set_trace()