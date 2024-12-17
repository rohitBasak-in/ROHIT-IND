import cv2
import numpy as np

# Paths to the two images
image1_path = "me1.png"  # Replace with your first image
image2_path = "me2.png"  # Replace with your second image

# Load the images
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

if image1 is None or image2 is None:
    print("One or both images could not be loaded. Check the file paths.")
else:
    print("Original Shapes:")
    print(f"Image1 Shape: {image1.shape}")
    print(f"Image2 Shape: {image2.shape}")

    # Resize images to the same dimensions if they are different
    if image1.shape != image2.shape:
        print("Images have different sizes. Resizing image2...")
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
        print(f"Resized Image2 Shape: {image2.shape}")


    # Compare matrices
    total_pixels = image1.shape[0] * image1.shape[1]  # Total number of pixels
    matching_pixels = np.sum(image1 == image2) // image1.shape[2]  # Sum of all matching pixels across channels

    # Calculate similarity percentage
    similarity_percentage = (matching_pixels / total_pixels) * 100
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")

    # Debugging outputs
    print(f"Image1 Height: {image1.shape[0]}, Width: {image1.shape[1]}")
    print(f"Total Pixels: {total_pixels}")
    print(f"Matching Pixels: {matching_pixels}")

    # Check if images are at least 65% similar
    if similarity_percentage >= 65:
        print("The images are at least 65% similar.")
    else:
        print("The images are less than 65% similar.")
