# LangChain DOCX Document Loader Examples

This repository demonstrates how to use LangChain's document loaders to load and process DOCX files.

## Files Overview

- `simple_docx_example.py` - Basic example showing how to load a DOCX file
- `docx_loader_example.py` - Comprehensive example with multiple loaders and text processing
- `unstructured.py` - Original file with loader imports
- `requirements.txt` - Required Python packages
- `1-1 买卖合同（通用版）.docx` - Sample DOCX file (Chinese contract document)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install langchain langchain-community unstructured[docx] docx2txt python-docx
```

## Usage Examples

### Basic Usage

```python
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# Initialize the loader
loader = UnstructuredWordDocumentLoader("1-1 买卖合同（通用版）.docx")

# Load the document
documents = loader.load()

# Access the content
for doc in documents:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
```

### Run the Simple Example

```bash
python simple_docx_example.py
```

### Run the Comprehensive Example

```bash
python docx_loader_example.py
```

## Document Loaders Comparison

### 1. UnstructuredWordDocumentLoader
- **Pros**: Preserves formatting and structure information
- **Cons**: Requires additional dependencies
- **Use case**: When you need to maintain document structure

### 2. Docx2txtLoader
- **Pros**: Simple, fast, lightweight
- **Cons**: Loses formatting information
- **Use case**: When you only need plain text content

## Key Features Demonstrated

1. **Loading DOCX files** - Using different LangChain loaders
2. **Text splitting** - Breaking documents into smaller chunks
3. **Metadata extraction** - Accessing document properties
4. **Content analysis** - Basic text statistics and term detection
5. **Error handling** - Proper exception management

## Next Steps

After loading your DOCX documents, you can:

1. **Store in vector databases** for semantic search (Chroma, Pinecone, etc.)
2. **Use with LLMs** for question answering
3. **Extract specific information** using prompts
4. **Summarize content** using language models
5. **Translate** to other languages

## Example Applications

- Contract analysis and extraction
- Document summarization
- Information retrieval systems
- Content management systems
- Legal document processing

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
2. **File not found**: Ensure the DOCX file is in the correct path
3. **Encoding issues**: LangChain handles most encoding automatically

### Additional Dependencies

If you encounter issues, you might need:
```bash
# For better document parsing
pip install python-magic-bin  # Windows only
pip install libmagic          # Linux/Mac

# For improved text extraction
pip install pytesseract       # OCR capabilities
```

## Contributing

Feel free to extend these examples with:
- Additional document loaders
- More text processing techniques
- Integration with vector databases
- LLM-based analysis examples 