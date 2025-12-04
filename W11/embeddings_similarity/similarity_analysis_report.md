# Image Similarity Analysis Report

## Overview
This report presents the results of a comprehensive image similarity analysis using computer vision techniques to create embeddings and calculate similarity between three images of what appears to be the same historic building (Ham House).

## Methodology

### Embedding Creation
Each image was processed to create a 192-dimensional embedding vector using multiple feature extraction techniques:

1. **Color Histogram Features (96 dimensions)**
   - Converted images to HSV color space
   - Extracted histograms for Hue, Saturation, and Value channels
   - Used 32 bins per channel for detailed color representation
   - Normalized to ensure scale invariance

2. **Edge Features (32 dimensions)**
   - Applied Canny edge detection
   - Created histogram of edge intensities
   - Captures structural information and boundaries

3. **Texture Features (64 dimensions)**
   - Applied Sobel operators for gradient detection
   - Extracted X and Y gradient histograms
   - Captures surface patterns and textures

### Similarity Calculation
- Used cosine similarity metric
- Measures angle between embedding vectors
- Range: 0 (completely different) to 1 (identical)

## Results

### Similarity Matrix
```
                    Image 1     Image 2     Image 3
Image 1 (ham_01.jpg)  1.0000      0.9016      0.9446
Image 2 (ham_04.jpg)  0.9016      1.0000      0.8807
Image 3 (ham_05.jpg)  0.9446      0.8807      1.0000
```

### Pairwise Comparisons

**Image 1 vs Image 2: 0.9016 (90.16%)**
- Very high similarity
- Both appear to be frontal views of the building
- Slight differences in image quality/compression

**Image 1 vs Image 3: 0.9446 (94.46%)** ⭐ HIGHEST
- Extremely high similarity
- Image 3 shows rear/side view but shares many features
- Color palette and architectural elements very consistent

**Image 2 vs Image 3: 0.8807 (88.07%)**
- High similarity
- Different angles of the same building
- Some perspective differences affecting the score

### Overall Analysis

**Average Similarity: 90.90%**

The analysis reveals that all three images are extremely similar, which aligns with visual inspection - they all depict the same historic brick building from different angles and with slight variations in:
- Camera angle and perspective
- Lighting conditions
- Image quality/compression
- Specific architectural features visible

## Technical Details

### Embedding Characteristics
- **Dimension**: 192 features per image
- **Feature Distribution**:
  - 50% color information (captures red brick, stone detailing)
  - 17% edge information (captures architectural lines and boundaries)
  - 33% texture information (captures brick patterns and surface details)

### Why These Images Score So High
1. **Consistent Color Palette**: All images show the same red brick building with similar stone/yellow architectural detailing
2. **Similar Architectural Features**: Windows, chimneys, and building structure are consistent
3. **Common Elements**: Lawn, pathways, and statue visible in similar positions
4. **Same Subject**: All three images are of the same building, just from different viewpoints

## Interpretation

The embeddings successfully capture the essential visual characteristics of the images, demonstrating that:
- The images are of the same building complex
- Despite different angles, the core visual features remain highly consistent
- The algorithm can reliably identify similar images even with perspective changes

## Files Generated
1. `similarity_results.json` - Raw numerical results
2. `similarity_visualization.png` - Visual representation of the analysis

---
*Analysis performed using OpenCV and scikit-learn*
*Date: December 4, 2025*
