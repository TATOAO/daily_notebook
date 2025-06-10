# Document Layout Parser with LayoutParser

A comprehensive implementation of document layout analysis using the [LayoutParser](https://github.com/Layout-Parser/layout-parser) library. This implementation is based on the [Deep Layout Parsing example](https://layout-parser.readthedocs.io/en/latest/example/deep_layout_parsing/) from the official documentation.

## Features

- 🔍 **Layout Detection**: Detect different layout elements (Text, Title, List, Table, Figure)
- 📝 **Text Extraction**: Extract text from detected regions using OCR
- 🎯 **Smart Sorting**: Automatically sort text blocks in reading order (left-to-right, top-to-bottom)
- 🖼️ **Visualization**: Generate visual outputs showing detected layout elements
- 📊 **Multiple Formats**: Support for images and PDFs
- 🔧 **Configurable**: Adjustable confidence thresholds and OCR languages

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install System Dependencies

#### For OCR (Tesseract):

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

#### For PDF Processing:

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

**Windows:**
Download and install from: https://blog.alivate.com.au/poppler-windows/

### 3. Install PyTorch and Detectron2

The layout parser requires PyTorch and Detectron2. Installation varies by system:

**For CPU-only:**
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.10/index.html
```

**For GPU (CUDA 11.8):**
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu118/torch1.10/index.html
```

## Usage

### Command Line Usage

Process a single image:
```bash
python layout_parser_3.py your_document.jpg --output-dir ./output
```

With custom settings:
```bash
python layout_parser_3.py document.png \
    --output-dir ./results \
    --confidence 0.7 \
    --ocr-lang eng \
    --no-viz
```

### Python API Usage

#### Basic Usage

```python
from layout_parser_3 import DocumentLayoutParser

# Initialize parser
parser = DocumentLayoutParser(
    confidence_threshold=0.8,
    ocr_language='eng'
)

# Process document
results = parser.process_document(
    'document.jpg',
    output_dir='./output',
    save_visualizations=True
)

# Print results
parser.print_results(results)
```

#### Advanced Usage

```python
from layout_parser_3 import DocumentLayoutParser
import cv2

# Initialize with custom model and settings
parser = DocumentLayoutParser(
    model_config='lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
    confidence_threshold=0.7,
    ocr_language='chi_sim'  # Chinese simplified
)

# Load and process image manually
image = parser.load_image('document.jpg')
layout = parser.detect_layout(image)

# Filter and process text blocks
text_blocks = parser.filter_and_sort_text_blocks(layout, image)
text_blocks = parser.extract_text_from_blocks(text_blocks, image)

# Visualize results
visualization = parser.visualize_layout(image, layout)
```

#### Processing Multiple Files

```python
import os
from layout_parser_3 import DocumentLayoutParser

parser = DocumentLayoutParser()

# Process all images in a directory
image_dir = './documents'
output_dir = './results'

for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        
        try:
            results = parser.process_document(
                image_path,
                output_dir=output_dir
            )
            print(f"Processed {filename}: {len(results['extracted_texts'])} text blocks")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
```

## Configuration Options

### Model Configuration

The layout parser supports different pre-trained models:

```python
# PubLayNet models (academic papers)
model_config = 'lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config'
model_config = 'lp://PubLayNet/mask_rcnn_R_50_FPN_3x/config'

# TableBank models (table detection)
model_config = 'lp://TableBank/faster_rcnn_R_50_FPN_3x/config'

# Historical Japanese documents
model_config = 'lp://HJDataset/faster_rcnn_R_50_FPN_3x/config'
```

### OCR Languages

Supported OCR languages (requires corresponding Tesseract language packs):

```python
# English
ocr_language = 'eng'

# Chinese Simplified
ocr_language = 'chi_sim'

# Chinese Traditional
ocr_language = 'chi_tra'

# Japanese
ocr_language = 'jpn'

# Multiple languages
ocr_language = 'eng+chi_sim'
```

### Confidence Threshold

Adjust detection sensitivity:

```python
# More strict (fewer false positives)
confidence_threshold = 0.9

# More lenient (more detections)
confidence_threshold = 0.5

# Default
confidence_threshold = 0.8
```

## Output Files

The parser generates several output files:

1. **`{filename}_layout_results.json`**: Complete results in JSON format
2. **`{filename}_layout_detected.jpg`**: Visualization of all detected elements
3. **`{filename}_text_blocks.jpg`**: Visualization of text blocks only
4. **`{filename}_extracted_text.txt`**: Plain text output of extracted content

### JSON Output Format

```json
{
  "image_path": "document.jpg",
  "total_elements": 15,
  "text_blocks": 8,
  "layout_elements": [
    {
      "type": "Title",
      "coordinates": {"x1": 100, "y1": 50, "x2": 500, "y2": 80},
      "confidence": 0.95
    }
  ],
  "extracted_texts": [
    {
      "id": 0,
      "text": "Document Title",
      "coordinates": {"x1": 100, "y1": 50, "x2": 500, "y2": 80}
    }
  ]
}
```

## Examples

### Example 1: Research Paper Analysis

```python
from layout_parser_3 import DocumentLayoutParser

# Initialize for academic papers
parser = DocumentLayoutParser(
    model_config='lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
    confidence_threshold=0.8
)

# Process paper
results = parser.process_document('research_paper.pdf', './paper_analysis')

# Extract only text content (excluding figures and tables)
text_content = []
for text_block in results['extracted_texts']:
    text_content.append(text_block['text'])

full_text = '\n\n'.join(text_content)
print("Extracted paper content:", full_text)
```

### Example 2: Multi-language Document

```python
# For Chinese documents
parser = DocumentLayoutParser(
    confidence_threshold=0.7,
    ocr_language='chi_sim+eng'  # Chinese + English
)

results = parser.process_document('chinese_document.jpg')
```

### Example 3: Batch Processing

```python
import glob
from layout_parser_3 import DocumentLayoutParser

parser = DocumentLayoutParser()

# Process all PDFs in a directory
pdf_files = glob.glob('./documents/*.pdf')

for pdf_file in pdf_files:
    # Convert PDF to images first (implement pdf_to_images function)
    image_paths = convert_pdf_to_images(pdf_file)
    
    for i, image_path in enumerate(image_paths):
        output_dir = f'./results/{Path(pdf_file).stem}/page_{i+1}'
        results = parser.process_document(image_path, output_dir)
        print(f"Processed {pdf_file} page {i+1}")
```

## Troubleshooting

### Common Issues

1. **ImportError: No module named 'detectron2'**
   - Install Detectron2 following the official instructions
   - Make sure PyTorch is installed first

2. **TesseractNotFoundError**
   - Install Tesseract OCR system dependency
   - On Windows, add Tesseract to PATH

3. **CUDA out of memory**
   - Reduce image size before processing
   - Use CPU-only version of PyTorch

4. **Poor OCR results**
   - Check image quality and resolution
   - Adjust confidence threshold
   - Use appropriate OCR language

### Performance Tips

1. **Resize large images** before processing:
   ```python
   import cv2
   image = cv2.imread('large_image.jpg')
   image = cv2.resize(image, (1600, 1200))  # Resize to reasonable size
   ```

2. **Use GPU** for faster processing (if available)

3. **Batch process** multiple documents for efficiency

## References

- [LayoutParser GitHub Repository](https://github.com/Layout-Parser/layout-parser)
- [Deep Layout Parsing Example](https://layout-parser.readthedocs.io/en/latest/example/deep_layout_parsing/)
- [LayoutParser Documentation](https://layout-parser.readthedocs.io/)
- [Model Zoo](https://layout-parser.readthedocs.io/en/latest/notes/modelzoo.html)

## License

This implementation follows the Apache 2.0 license of the original LayoutParser library. 