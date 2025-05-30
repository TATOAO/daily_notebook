#!/usr/bin/env python3
"""
Simple example of using the Document Layout Parser.

This script demonstrates basic usage of the DocumentLayoutParser class
to analyze document layout and extract text from images.
"""

from layout_parser_3 import DocumentLayoutParser
import os


def convert_pdf_to_image(pdf_path: str, output_dir: str = "./temp_images"):
    """Convert PDF to images for layout analysis."""
    try:
        from pdf2image import convert_from_path
        import os
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Convert PDF to images
        images = convert_from_path(pdf_path)
        image_paths = []
        
        for i, image in enumerate(images):
            image_path = os.path.join(output_dir, f"page_{i+1}.jpg")
            image.save(image_path, 'JPEG')
            image_paths.append(image_path)
            
        return image_paths
        
    except ImportError:
        print("pdf2image not installed. Install with: pip install pdf2image")
        return []


def main():
    """Main example function."""
    
    # Initialize the layout parser
    print("Initializing Document Layout Parser...")
    parser = DocumentLayoutParser(
        confidence_threshold=0.8,
        ocr_language='eng'  # You can change this to 'chi_sim' for Chinese, etc.
    )
    
    # Example 1: Process a direct image file
    print("\n=== Example 1: Processing Image File ===")
    
    # Look for sample images in the current directory
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    sample_images = []
    
    for file in os.listdir('.'):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            sample_images.append(file)
    
    if sample_images:
        sample_image = sample_images[0]
        print(f"Processing image: {sample_image}")
        
        try:
            results = parser.process_document(
                sample_image,
                output_dir="./layout_output",
                save_visualizations=True
            )
            parser.print_results(results)
            
        except Exception as e:
            print(f"Error processing {sample_image}: {e}")
    else:
        print("No image files found in current directory")
    
    # Example 2: Process PDF file (convert to images first)
    print("\n=== Example 2: Processing PDF File ===")
    
    # Look for PDF files
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if pdf_files:
        pdf_file = pdf_files[0]
        print(f"Converting PDF to images: {pdf_file}")
        
        # Convert PDF to images
        image_paths = convert_pdf_to_image(pdf_file)
        
        if image_paths:
            # Process the first page as an example
            first_page = image_paths[0]
            print(f"Processing first page: {first_page}")
            
            try:
                results = parser.process_document(
                    first_page,
                    output_dir="./pdf_layout_output",
                    save_visualizations=True
                )
                parser.print_results(results)
                
                # Clean up temporary images
                for img_path in image_paths:
                    os.remove(img_path)
                os.rmdir("./temp_images")
                
            except Exception as e:
                print(f"Error processing PDF page: {e}")
        else:
            print("Could not convert PDF to images")
    else:
        print("No PDF files found in current directory")
    
    # Example 3: Programmatic usage
    print("\n=== Example 3: Programmatic Usage ===")
    
    # You can also use the parser programmatically
    sample_files = [f for f in os.listdir('.') 
                   if any(f.lower().endswith(ext) for ext in image_extensions + ['.pdf'])]
    
    if sample_files:
        print("Available files for processing:")
        for i, file in enumerate(sample_files):
            print(f"{i+1}. {file}")
        
        print("\nTo process a specific file, you can use:")
        print("from layout_parser_3 import DocumentLayoutParser")
        print("parser = DocumentLayoutParser()")
        print("results = parser.process_document('your_file.jpg', output_dir='./output')")
    
    print("\n=== Usage Instructions ===")
    print("1. Command line usage:")
    print("   python layout_parser_3.py your_image.jpg --output-dir ./output")
    print()
    print("2. Python usage:")
    print("   from layout_parser_3 import DocumentLayoutParser")
    print("   parser = DocumentLayoutParser()")
    print("   results = parser.process_document('your_image.jpg')")
    print()
    print("3. Advanced options:")
    print("   - Adjust confidence threshold: DocumentLayoutParser(confidence_threshold=0.7)")
    print("   - Change OCR language: DocumentLayoutParser(ocr_language='chi_sim')")
    print("   - Use different model: DocumentLayoutParser(model_config='lp://...')")


if __name__ == "__main__":
    main() 