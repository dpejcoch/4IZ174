# Image Similarity Code - Usage Guide

## Files Included

1. **image_similarity.py** - Main script for creating embeddings and calculating similarity
2. **create_visualization.py** - Script for creating visual representations

## Requirements

```bash
pip install opencv-python numpy scikit-learn
```

or with break-system-packages flag:

```bash
pip install --break-system-packages opencv-python numpy scikit-learn
```

## Usage

### Basic Usage

```bash
python3 image_similarity.py
```

This will:
- Load the three images from specified paths
- Create 192-dimensional embeddings for each image
- Calculate cosine similarity between all pairs
- Display results in console
- Save results to `similarity_results.json`

### Creating Visualization

```bash
python3 create_visualization.py
```

This will:
- Load the similarity results
- Create a visual representation with images and heatmap
- Save to `similarity_visualization.png`

## How to Modify for Your Own Images

### In image_similarity.py

Find the section:
```python
# Image paths
image_paths = [
    '/mnt/user-data/uploads/ham_01.jpg',
    '/mnt/user-data/uploads/ham_04.jpg',
    '/mnt/user-data/uploads/ham_05.jpg'
]
```

Replace with your own image paths:
```python
image_paths = [
    '/path/to/your/image1.jpg',
    '/path/to/your/image2.jpg',
    '/path/to/your/image3.jpg'
]
```

### In create_visualization.py

Update the same section:
```python
image_paths = [
    '/path/to/your/image1.jpg',
    '/path/to/your/image2.jpg',
    '/path/to/your/image3.jpg'
]
```

## Understanding the Embeddings

The 192-dimensional embedding consists of:

1. **Color Features (96 dims)**: HSV color histograms
   - 32 bins for Hue (0-180°)
   - 32 bins for Saturation (0-255)
   - 32 bins for Value (0-255)

2. **Edge Features (32 dims)**: Canny edge detection histogram
   - Captures structural boundaries

3. **Texture Features (64 dims)**: Sobel gradient histograms
   - 32 bins for X-direction gradients
   - 32 bins for Y-direction gradients

## Key Functions

### extract_color_histogram(image, bins=32)
Extracts color features using HSV color space histograms.

### extract_edge_features(image)
Extracts edge patterns using Canny edge detection.

### extract_texture_features(image)
Extracts texture information using Sobel operators.

### create_image_embedding(image_path)
Main function that combines all features into a single embedding vector.

### calculate_similarity_matrix(embeddings)
Computes cosine similarity between all embedding pairs.

## Interpreting Results

**Cosine Similarity Scale:**
- 1.0 = Identical images
- 0.9-1.0 = Extremely similar (same subject/scene)
- 0.8-0.9 = Very similar (related content)
- 0.7-0.8 = Moderately similar
- < 0.7 = Less similar

## Example Output

```
SIMILARITY MATRIX
Cosine Similarity Scores (0 to 1, where 1 is identical):

                    Image 1     Image 2     Image 3
Image 1             1.0000      0.9016      0.9446
Image 2             0.9016      1.0000      0.8807
Image 3             0.9446      0.8807      1.0000

PAIRWISE SIMILARITIES
Image 1 vs Image 2: 0.9016 (90.16%)
Image 1 vs Image 3: 0.9446 (94.46%)
Image 2 vs Image 3: 0.8807 (88.07%)
```

## Advanced Customization

### Adjust Feature Weights

You can modify the number of histogram bins for different sensitivity:

```python
# More detailed color features (slower but more precise)
color_features = extract_color_histogram(image, bins=64)

# Fewer bins (faster but less precise)
color_features = extract_color_histogram(image, bins=16)
```

### Add More Features

You can extend the embedding by adding more feature extractors:

```python
def extract_custom_features(image):
    # Your custom feature extraction
    features = ...
    return features

# In create_image_embedding():
custom_features = extract_custom_features(image)
embedding = np.concatenate([color_features, edge_features, 
                           texture_features, custom_features])
```

## Limitations

1. **No Deep Learning**: Uses traditional CV features, not neural network embeddings
2. **Fixed Size**: All images resized to 512x512 for comparison
3. **Memory**: Loads all images in memory simultaneously
4. **Limited to Visual Similarity**: Doesn't understand semantic content

## Extending to More Images

To compare more than 3 images, simply add more paths to the `image_paths` list:

```python
image_paths = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
    'image5.jpg',
    # ... add as many as needed
]
```

The code will automatically handle N×N similarity matrix.

## Tips for Best Results

1. **Similar lighting conditions** in images give better comparisons
2. **Same aspect ratio** helps maintain feature consistency
3. **Higher resolution** source images provide better features
4. **Consistent camera settings** improve reliability

## Troubleshooting

**Error: "Could not read image"**
- Check file path is correct
- Ensure image format is supported (jpg, png, etc.)

**Low similarity for similar images**
- Images might have very different lighting
- Try adjusting histogram bin counts
- Consider preprocessing (normalization, etc.)

**Memory issues with many images**
- Process images in batches
- Reduce resize dimensions from 512x512

## License

Free to use and modify for any purpose.

---
Created: December 2025
