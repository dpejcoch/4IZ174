import cv2
import numpy as np
import json
from pathlib import Path

def create_similarity_visualization():
    """Create a visual representation of the similarity analysis"""
    
    # Load results
    with open('/home/claude/similarity_results.json', 'r') as f:
        results = json.load(f)
    
    similarity_matrix = np.array(results['similarity_matrix'])
    
    # Create a larger canvas for the visualization
    canvas_height = 1200
    canvas_width = 1400
    canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255
    
    # Load and resize images
    image_paths = [
        '/mnt/user-data/uploads/ham_01.jpg',
        '/mnt/user-data/uploads/ham_04.jpg',
        '/mnt/user-data/uploads/ham_05.jpg'
    ]
    
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        img = cv2.resize(img, (350, 250))
        images.append(img)
    
    # Place images on canvas
    y_offset = 50
    x_positions = [50, 400, 750]
    
    # Add title
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, 'IMAGE SIMILARITY ANALYSIS', (350, 30), 
                font, 1.2, (0, 0, 0), 2)
    
    # Place images with labels
    for i, (img, x_pos) in enumerate(zip(images, x_positions)):
        canvas[y_offset:y_offset+250, x_pos:x_pos+350] = img
        label = f'Image {i+1}'
        cv2.putText(canvas, label, (x_pos+120, y_offset+270), 
                    font, 0.7, (0, 0, 0), 2)
    
    # Draw similarity heatmap
    heatmap_y = 400
    heatmap_x = 100
    cell_size = 150
    
    cv2.putText(canvas, 'SIMILARITY MATRIX', (heatmap_x+100, heatmap_y-20), 
                font, 1.0, (0, 0, 0), 2)
    
    # Create color-coded similarity matrix
    for i in range(3):
        for j in range(3):
            similarity = similarity_matrix[i][j]
            
            # Calculate color (green for high similarity, yellow for medium)
            color_intensity = int(similarity * 255)
            if similarity > 0.95:
                color = (0, 255, 0)  # Green
            elif similarity > 0.85:
                color = (0, 255, 255)  # Yellow
            else:
                color = (0, 165, 255)  # Orange
            
            # Draw cell
            x1 = heatmap_x + j * cell_size
            y1 = heatmap_y + i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            cv2.rectangle(canvas, (x1, y1), (x2, y2), color, -1)
            cv2.rectangle(canvas, (x1, y1), (x2, y2), (0, 0, 0), 2)
            
            # Add text
            text = f'{similarity:.3f}'
            text_size = cv2.getTextSize(text, font, 0.8, 2)[0]
            text_x = x1 + (cell_size - text_size[0]) // 2
            text_y = y1 + (cell_size + text_size[1]) // 2
            cv2.putText(canvas, text, (text_x, text_y), 
                        font, 0.8, (0, 0, 0), 2)
    
    # Add labels for matrix rows and columns
    for i in range(3):
        label = f'Img {i+1}'
        cv2.putText(canvas, label, (heatmap_x - 70, heatmap_y + i * cell_size + 80), 
                    font, 0.6, (0, 0, 0), 2)
        cv2.putText(canvas, label, (heatmap_x + i * cell_size + 50, heatmap_y - 30), 
                    font, 0.6, (0, 0, 0), 2)
    
    # Add pairwise comparison details
    details_y = 850
    cv2.putText(canvas, 'PAIRWISE COMPARISONS:', (50, details_y), 
                font, 0.9, (0, 0, 0), 2)
    
    comparisons = [
        (f'Image 1 vs Image 2: {similarity_matrix[0][1]:.4f} ({similarity_matrix[0][1]*100:.2f}%)', details_y + 40),
        (f'Image 1 vs Image 3: {similarity_matrix[0][2]:.4f} ({similarity_matrix[0][2]*100:.2f}%)', details_y + 80),
        (f'Image 2 vs Image 3: {similarity_matrix[1][2]:.4f} ({similarity_matrix[1][2]*100:.2f}%)', details_y + 120)
    ]
    
    for text, y_pos in comparisons:
        cv2.putText(canvas, text, (80, y_pos), font, 0.7, (0, 0, 0), 2)
    
    # Add interpretation
    avg_similarity = np.mean([similarity_matrix[0][1], similarity_matrix[0][2], similarity_matrix[1][2]])
    cv2.putText(canvas, f'Average Similarity: {avg_similarity:.4f} ({avg_similarity*100:.2f}%)', 
                (50, details_y + 180), font, 0.8, (0, 100, 0), 2)
    
    # Add legend
    legend_y = 1050
    cv2.putText(canvas, 'Legend:', (50, legend_y), font, 0.7, (0, 0, 0), 2)
    cv2.rectangle(canvas, (150, legend_y-20), (200, legend_y), (0, 255, 0), -1)
    cv2.putText(canvas, '> 0.95 (Excellent)', (220, legend_y-5), font, 0.6, (0, 0, 0), 1)
    
    cv2.rectangle(canvas, (450, legend_y-20), (500, legend_y), (0, 255, 255), -1)
    cv2.putText(canvas, '0.85 - 0.95 (Very Good)', (520, legend_y-5), font, 0.6, (0, 0, 0), 1)
    
    # Save visualization
    output_path = '/mnt/user-data/outputs/similarity_visualization.png'
    cv2.imwrite(output_path, canvas)
    print(f"Visualization saved to: {output_path}")
    
    return output_path

if __name__ == "__main__":
    create_similarity_visualization()
