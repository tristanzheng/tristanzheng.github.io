import os
import sys
import subprocess
import PIL

def optimize_images(directory, max_width=1920, quality=80):
    from PIL import Image
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, file)
                try:
                    with Image.open(filepath) as img:
                        original_size = os.path.getsize(filepath)
                        
                        # Check if resize is needed
                        if img.width > max_width:
                            ratio = max_width / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                            print(f"Resizing {file}...")
                        
                        # Save with optimization
                        img.save(filepath, optimize=True, quality=quality)
                        
                        new_size = os.path.getsize(filepath)
                        saved = original_size - new_size
                        if saved > 0:
                            print(f"Optimized {file}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (Saved {saved/1024:.1f}KB)")
                        else:
                            print(f"Processed {file} (No size reduction)")
                            
                except Exception as e:
                    print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    optimize_images(os.path.join(root, 'assets/images'))