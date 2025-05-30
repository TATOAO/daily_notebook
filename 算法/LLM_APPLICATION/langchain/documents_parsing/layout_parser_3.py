#!/usr/bin/env python3
"""
Layout Parser Implementation for Document Analysis

This script demonstrates how to use the layoutparser library to:
1. Load Deep Learning Layout Detection models
2. Detect layout elements in document images
3. Extract text from detected regions using OCR
4. Process and organize the detected layout

Based on the Deep Layout Parsing example from:
https://layout-parser.readthedocs.io/en/latest/example/deep_layout_parsing/
"""

import layoutparser as lp
import cv2
import numpy as np
from pathlib import Path
import json
from typing import List, Dict, Any, Optional
import argparse


class DocumentLayoutParser:
    """A comprehensive document layout parser using layoutparser library."""
    
    def __init__(self, 
                 model_config: str = 'lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                 confidence_threshold: float = 0.8,
                 ocr_language: str = 'eng'):
        """
        Initialize the layout parser.
        
        Args:
            model_config: Layout detection model configuration
            confidence_threshold: Confidence threshold for detection
            ocr_language: Language for OCR (default: 'eng')
        """
        self.confidence_threshold = confidence_threshold
        self.ocr_language = ocr_language
        
        # Label mapping for different layout elements
        self.label_map = {
            0: "Text", 
            1: "Title", 
            2: "List", 
            3: "Table", 
            4: "Figure"
        }
        
        # Initialize the layout detection model
        self.model = lp.Detectron2LayoutModel(
            model_config,
            extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", confidence_threshold],
            label_map=self.label_map
        )
        
        # Initialize OCR agent
        self.ocr_agent = lp.TesseractAgent(languages=ocr_language)
        
    def load_image(self, image_path: str) -> np.ndarray:
        """
        Load and preprocess image for layout detection.
        
        Args:
            image_path: Path to the input image
            
        Returns:
            Preprocessed image array
        """
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image from {image_path}")
        
        # Convert from BGR (cv2 default) to RGB
        image = image[..., ::-1]
        return image
    
    def detect_layout(self, image: np.ndarray) -> lp.Layout:
        """
        Detect layout elements in the image.
        
        Args:
            image: Input image array
            
        Returns:
            Layout object containing detected elements
        """
        layout = self.model.detect(image)
        return layout
    
    def filter_and_sort_text_blocks(self, layout: lp.Layout, image: np.ndarray) -> lp.Layout:
        """
        Filter and sort text blocks for better readability order.
        
        Args:
            layout: Detected layout
            image: Original image
            
        Returns:
            Filtered and sorted text blocks
        """
        # Filter text blocks and figure blocks
        text_blocks = lp.Layout([b for b in layout if b.type == 'Text'])
        figure_blocks = lp.Layout([b for b in layout if b.type == 'Figure'])
        
        # Remove text blocks that are inside figure regions
        text_blocks = lp.Layout([
            b for b in text_blocks 
            if not any(b.is_in(b_fig) for b_fig in figure_blocks)
        ])
        
        # Sort text blocks by reading order (left column first, then right column)
        h, w = image.shape[:2]
        
        # Define left column interval
        left_interval = lp.Interval(0, w/2 * 1.05, axis='x').put_on_canvas(image)
        
        # Filter blocks by left and right columns
        left_blocks = text_blocks.filter_by(left_interval, center=True)
        left_blocks.sort(key=lambda b: b.coordinates[1], inplace=True)
        
        right_blocks = [b for b in text_blocks if b not in left_blocks]
        right_blocks.sort(key=lambda b: b.coordinates[1], inplace=True)
        
        # Combine and assign IDs
        text_blocks = lp.Layout([
            b.set(id=idx) for idx, b in enumerate(left_blocks + right_blocks)
        ])
        
        return text_blocks
    
    def extract_text_from_blocks(self, text_blocks: lp.Layout, image: np.ndarray) -> lp.Layout:
        """
        Extract text from detected text blocks using OCR.
        
        Args:
            text_blocks: Text blocks to process
            image: Original image
            
        Returns:
            Text blocks with extracted text
        """
        for block in text_blocks:
            # Crop the image segment with padding for better OCR
            segment_image = (block
                           .pad(left=5, right=5, top=5, bottom=5)
                           .crop_image(image))
            
            # Perform OCR
            text = self.ocr_agent.detect(segment_image)
            block.set(text=text, inplace=True)
        
        return text_blocks
    
    def visualize_layout(self, image: np.ndarray, layout: lp.Layout, 
                        show_ids: bool = True, box_width: int = 3) -> np.ndarray:
        """
        Visualize the detected layout with bounding boxes.
        
        Args:
            image: Original image
            layout: Detected layout
            show_ids: Whether to show element IDs
            box_width: Width of bounding boxes
            
        Returns:
            Image with layout visualization
        """
        return lp.draw_box(image, layout, 
                          box_width=box_width, 
                          show_element_id=show_ids)
    
    def process_document(self, image_path: str, 
                        output_dir: Optional[str] = None,
                        save_visualizations: bool = True) -> Dict[str, Any]:
        """
        Complete document processing pipeline.
        
        Args:
            image_path: Path to input image
            output_dir: Directory to save outputs
            save_visualizations: Whether to save visualization images
            
        Returns:
            Dictionary containing processing results
        """
        # Load image
        image = self.load_image(image_path)
        
        # Detect layout
        layout = self.detect_layout(image)
        
        # Filter and sort text blocks
        text_blocks = self.filter_and_sort_text_blocks(layout, image)
        
        # Extract text from blocks
        text_blocks = self.extract_text_from_blocks(text_blocks, image)
        
        # Prepare results
        results = {
            'image_path': image_path,
            'total_elements': len(layout),
            'text_blocks': len(text_blocks),
            'layout_elements': [],
            'extracted_texts': []
        }
        
        # Process all layout elements
        for element in layout:
            element_info = {
                'type': element.type,
                'coordinates': {
                    'x1': float(element.block.x_1),
                    'y1': float(element.block.y_1), 
                    'x2': float(element.block.x_2),
                    'y2': float(element.block.y_2)
                },
                'confidence': float(element.score) if hasattr(element, 'score') else None
            }
            results['layout_elements'].append(element_info)
        
        # Extract texts
        for text_block in text_blocks:
            if hasattr(text_block, 'text') and text_block.text:
                results['extracted_texts'].append({
                    'id': text_block.id,
                    'text': text_block.text.strip(),
                    'coordinates': {
                        'x1': float(text_block.block.x_1),
                        'y1': float(text_block.block.y_1),
                        'x2': float(text_block.block.x_2),
                        'y2': float(text_block.block.y_2)
                    }
                })
        
        # Save outputs if directory is specified
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(exist_ok=True)
            
            # Save JSON results
            json_path = output_path / f"{Path(image_path).stem}_layout_results.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            # Save visualizations
            if save_visualizations:
                # Save original layout visualization
                layout_vis = self.visualize_layout(image, layout)
                layout_vis_path = output_path / f"{Path(image_path).stem}_layout_detected.jpg"
                cv2.imwrite(str(layout_vis_path), layout_vis[..., ::-1])
                
                # Save text blocks visualization  
                text_vis = self.visualize_layout(image, text_blocks)
                text_vis_path = output_path / f"{Path(image_path).stem}_text_blocks.jpg"
                cv2.imwrite(str(text_vis_path), text_vis[..., ::-1])
            
            # Save extracted text to file
            text_path = output_path / f"{Path(image_path).stem}_extracted_text.txt"
            with open(text_path, 'w', encoding='utf-8') as f:
                for i, text_info in enumerate(results['extracted_texts']):
                    f.write(f"Text Block {text_info['id']}:\n")
                    f.write(f"{text_info['text']}\n")
                    f.write("---\n")
        
        return results
    
    def print_results(self, results: Dict[str, Any]):
        """Print processing results to console."""
        print(f"\n=== Layout Analysis Results ===")
        print(f"Image: {results['image_path']}")
        print(f"Total layout elements detected: {results['total_elements']}")
        print(f"Text blocks processed: {results['text_blocks']}")
        
        print(f"\n--- Layout Elements ---")
        for i, element in enumerate(results['layout_elements']):
            print(f"{i+1}. Type: {element['type']}, "
                  f"Confidence: {element['confidence']:.3f}")
        
        print(f"\n--- Extracted Texts ---")
        for text_info in results['extracted_texts']:
            print(f"Block {text_info['id']}: {text_info['text'][:100]}...")
            print("---")


def main():
    """Main function for command line usage."""
    parser = argparse.ArgumentParser(description="Document Layout Parser")
    parser.add_argument("image_path", help="Path to input image")
    parser.add_argument("--output-dir", "-o", default="./output", 
                       help="Output directory for results")
    parser.add_argument("--confidence", "-c", type=float, default=0.8,
                       help="Confidence threshold for detection")
    parser.add_argument("--ocr-lang", default="eng",
                       help="OCR language")
    parser.add_argument("--no-viz", action="store_true",
                       help="Skip saving visualizations")
    
    args = parser.parse_args()
    
    # Initialize parser
    doc_parser = DocumentLayoutParser(
        confidence_threshold=args.confidence,
        ocr_language=args.ocr_lang
    )
    
    # Process document
    try:
        results = doc_parser.process_document(
            args.image_path,
            output_dir=args.output_dir,
            save_visualizations=not args.no_viz
        )
        
        # Print results
        doc_parser.print_results(results)
        
        print(f"\nResults saved to: {args.output_dir}")
        
    except Exception as e:
        print(f"Error processing document: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    # exit(main())
    main()

