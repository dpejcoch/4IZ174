import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import json

def extract_color_histogram(image, bins=32):
    """Extract color histogram features from image"""
    # Convert to HSV for better color representation
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Calculate histogram for each channel
    hist_h = cv2.calcHist([hsv], [0], None, [bins], [0, 180])
    hist_s = cv2.calcHist([hsv], [1], None, [bins], [0, 256])
    hist_v = cv2.calcHist([hsv], [2], None, [bins], [0, 256])
    
    # Normalize histograms
    hist_h = cv2.normalize(hist_h, hist_h).flatten()
    hist_s = cv2.normalize(hist_s, hist_s).flatten()
    hist_v = cv2.normalize(hist_v, hist_v).flatten()
    
    # Concatenate all histograms
    return np.concatenate([hist_h, hist_s, hist_v])

def extract_edge_features(image):
    """Extract edge features using Canny edge detector"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    # Create histogram of edges
    hist = cv2.calcHist([edges], [0], None, [32], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    
    return hist

def extract_texture_features(image):
    """Extract texture features using LBP-like approach"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate gradient features
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Create histograms
    hist_x = np.histogram(sobelx, bins=32, range=(-255, 255))[0]
    hist_y = np.histogram(sobely, bins=32, range=(-255, 255))[0]
    
    # Normalize
    hist_x = hist_x / (hist_x.sum() + 1e-7)
    hist_y = hist_y / (hist_y.sum() + 1e-7)
    
    return np.concatenate([hist_x, hist_y])

def create_image_embedding(image_path):
    """Create a comprehensive embedding for an image"""
    # Read image
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")
    
    # Resize to standard size for consistent comparison
    image = cv2.resize(image, (512, 512))
    
    # Extract different features
    color_features = extract_color_histogram(image)
    edge_features = extract_edge_features(image)
    texture_features = extract_texture_features(image)
    
    # Concatenate all features to create final embedding
    embedding = np.concatenate([color_features, edge_features, texture_features])
    
    return embedding

def calculate_similarity_matrix(embeddings):
    """Calculate cosine similarity between all embeddings"""
    return cosine_similarity(embeddings)

def main():
    # Image paths
    image_paths = [
        '/mnt/user-data/uploads/ham_01.jpg',
        '/mnt/user-data/uploads/ham_04.jpg',
        '/mnt/user-data/uploads/ham_05.jpg'
    ]
    
    print("Creating embeddings for images...\n")
    
    # Create embeddings
    embeddings = []
    for i, path in enumerate(image_paths, 1):
        print(f"Processing Image {i}: {Path(path).name}")
        embedding = create_image_embedding(path)
        embeddings.append(embedding)
        print(f"  Embedding shape: {embedding.shape}")
        print(f"  Embedding dimension: {len(embedding)}")
        print()
    
    # Convert to numpy array
    embeddings = np.array(embeddings)
    
    # Calculate similarity matrix
    print("Calculating similarity matrix...\n")
    similarity_matrix = calculate_similarity_matrix(embeddings)
    
    # Print results
    print("="*60)
    print("SIMILARITY MATRIX")
    print("="*60)
    print("\nCosine Similarity Scores (0 to 1, where 1 is identical):\n")
    
    image_names = ['Image 1 (ham_01.jpg)', 'Image 2 (ham_04.jpg)', 'Image 3 (ham_05.jpg)']
    
    # Print header
    print(f"{'':20}", end='')
    for name in image_names:
        print(f"{name:20}", end='')
    print()
    print("-"*80)
    
    # Print matrix
    for i, name in enumerate(image_names):
        print(f"{name:20}", end='')
        for j in range(len(image_names)):
            print(f"{similarity_matrix[i][j]:20.4f}", end='')
        print()
    
    print("\n" + "="*60)
    print("PAIRWISE SIMILARITIES")
    print("="*60 + "\n")
    
    # Print pairwise similarities
    pairs = [
        (0, 1, "Image 1 vs Image 2"),
        (0, 2, "Image 1 vs Image 3"),
        (1, 2, "Image 2 vs Image 3")
    ]
    
    for i, j, label in pairs:
        similarity = similarity_matrix[i][j]
        percentage = similarity * 100
        print(f"{label:25} Similarity: {similarity:.4f} ({percentage:.2f}%)")
    
    print("\n" + "="*60)
    print("INTERPRETATION")
    print("="*60 + "\n")
    
    avg_similarity = np.mean([similarity_matrix[i][j] for i, j, _ in pairs])
    print(f"Average similarity across all pairs: {avg_similarity:.4f} ({avg_similarity*100:.2f}%)\n")
    
    if avg_similarity > 0.9:
        print("The images are extremely similar (likely same scene/object)")
    elif avg_similarity > 0.8:
        print("The images are very similar (likely related content)")
    elif avg_similarity > 0.7:
        print("The images are moderately similar")
    else:
        print("The images have lower similarity")
    
    # Save results
    results = {
        'similarity_matrix': similarity_matrix.tolist(),
        'embeddings_shape': embeddings.shape,
        'pairwise_similarities': {
            'image_1_vs_2': float(similarity_matrix[0][1]),
            'image_1_vs_3': float(similarity_matrix[0][2]),
            'image_2_vs_3': float(similarity_matrix[1][2])
        }
    }
    
    with open('/home/claude/similarity_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: similarity_results.json")

if __name__ == "__main__":
    main()
