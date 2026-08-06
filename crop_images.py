import os
from PIL import Image

# Path to the source screenshot
src_path = r"C:\Users\acer\.gemini\antigravity-ide\brain\4d97e4f2-e362-4ec3-bf23-2a0a0b2bb0ea\media__1786003770695.jpg"
output_dir = r"c:\Users\acer\OneDrive\Desktop\olivia_demo\assets\images"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

try:
    # Open the image
    img = Image.open(src_path)
    width, height = img.size
    print(f"Source image dimensions: {width}x{height}")

    # Instagram grid columns and rows from the screenshot
    cols = 6
    rows = 4

    # Calculate individual square size
    col_width = width / cols
    row_height = height / rows

    # Crop and save each square
    count = 1
    for r in range(rows):
        for c in range(cols):
            # Calculate coordinates
            left = c * col_width
            top = r * row_height
            right = (c + 1) * col_width
            bottom = (r + 1) * row_height

            # Crop the square
            cropped = img.crop((left, top, right, bottom))
            
            # Save the cropped image
            cropped_filename = f"insta_{count}.jpg"
            cropped_filepath = os.path.join(output_dir, cropped_filename)
            
            # Resize slightly to make it uniform and compressed for web (e.g., 500x500)
            cropped_resized = cropped.resize((500, 500), Image.Resampling.LANCZOS)
            cropped_resized.save(cropped_filepath, "JPEG", quality=85)
            
            print(f"Saved: {cropped_filepath}")
            count += 1
            
    print("\nSuccessfully cropped all 24 Instagram images!")

except Exception as e:
    print(f"Error processing image: {e}")
