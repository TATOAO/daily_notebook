#!/usr/bin/env python3
"""
Basic LangChain DOCX Loader Example (Minimal Dependencies)

This example uses Docx2txtLoader which has minimal dependencies.
"""

from langchain_community.document_loaders import Docx2txtLoader


def load_docx_basic():
    """
    Simple example using Docx2txtLoader (fewer dependencies)
    """
    print("Loading DOCX file with Docx2txtLoader...")
    print("="*50)
    
    # Initialize the loader with your DOCX file
    loader = Docx2txtLoader("1-1 买卖合同（通用版）.docx")
    
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
        
        # Show some basic statistics
        word_count = len(doc.page_content.split())
        print(f"\nWord count: {word_count}")
        
        # Look for contract terms
        contract_terms = ["合同", "甲方", "乙方", "条款", "协议"]
        found_terms = [term for term in contract_terms if term in doc.page_content]
        if found_terms:
            print(f"Contract terms found: {', '.join(found_terms)}")


# python -m simple_docx_basic
if __name__ == "__main__":
    try:
        load_docx_basic()
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please install required packages:")
        print("pip install langchain-community docx2txt")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the DOCX file exists in the current directory.") 