#!/usr/bin/env python3
"""
Simple LangChain DOCX Loader Example

Basic example of loading a DOCX file using LangChain's document loaders.
"""

from langchain_community.document_loaders import UnstructuredWordDocumentLoader


def load_docx_simple():
    """
    Simple example of loading a DOCX file
    """
    # Initialize the loader with your DOCX file
    loader = UnstructuredWordDocumentLoader("1-1 买卖合同（通用版）.docx")
    
    # Load the document
    documents = loader.load()
    
    # Print basic information
    print(f"Loaded {len(documents)} document(s)")
    
    # Display the content
    for i, doc in enumerate(documents):
        print(f"\n--- Document {i+1} ---")
        print(f"Content length: {len(doc.page_content)} characters")
        print(f"Metadata: {doc.metadata}")
        print(f"\nFirst 300 characters:")
        print(doc.page_content[:300])
        print("...")


if __name__ == "__main__":
    load_docx_simple() 