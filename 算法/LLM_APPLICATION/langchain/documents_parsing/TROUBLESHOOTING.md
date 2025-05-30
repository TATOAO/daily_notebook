# Troubleshooting LangChain DOCX Loading

## Common Issues and Solutions

### 1. ModuleNotFoundError: No module named 'unstructured.__version__'

**Problem**: The `unstructured` package has installation issues or conflicts.

**Solutions**:

#### Option A: Use the minimal version
```bash
# Use the basic version with fewer dependencies
python simple_docx_basic.py

# Install minimal dependencies
pip install langchain-community docx2txt
```

#### Option B: Reinstall unstructured
```bash
# Uninstall and reinstall unstructured
pip uninstall unstructured
pip install "unstructured[docx]"
```

#### Option C: Install with conda (if using conda)
```bash
conda install -c conda-forge unstructured
```

### 2. ModuleNotFoundError: Module langchain_community.document_loaders not found

**Solution**:
```bash
pip install langchain-community
```

### 3. ImportError with python-docx

**Solution**:
```bash
pip install python-docx
```

### 4. Issues in Virtual Environment

If you're using a virtual environment and having issues:

```bash
# Activate your virtual environment first
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Then install packages
pip install -r requirements_minimal.txt
```

### 5. Alternative: Use python-docx directly

If LangChain loaders are problematic, here's a direct approach:

```python
from docx import Document

def load_docx_direct(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Usage
text = load_docx_direct("1-1 买卖合同（通用版）.docx")
print(text[:500])  # First 500 characters
```

### 6. Platform-specific Issues

#### macOS
```bash
# If you have permission issues
pip install --user langchain-community docx2txt
```

#### Linux
```bash
# Install system dependencies if needed
sudo apt-get install python3-dev
pip install langchain-community docx2txt
```

#### Windows
```bash
# Use pip with --upgrade flag
pip install --upgrade langchain-community docx2txt
```

## Recommended Installation Order

1. Start with minimal dependencies:
   ```bash
   pip install langchain-community docx2txt
   python simple_docx_basic.py
   ```

2. If that works, add more features:
   ```bash
   pip install "unstructured[docx]" python-docx
   python simple_docx_example.py
   ```

3. For full functionality:
   ```bash
   pip install -r requirements.txt
   python docx_loader_example.py
   ```

## Test Your Installation

Run this simple test:
```python
try:
    from langchain_community.document_loaders import Docx2txtLoader
    print("✓ langchain-community installed correctly")
    
    loader = Docx2txtLoader("1-1 买卖合同（通用版）.docx")
    docs = loader.load()
    print(f"✓ Successfully loaded {len(docs)} documents")
    
except Exception as e:
    print(f"✗ Error: {e}") 