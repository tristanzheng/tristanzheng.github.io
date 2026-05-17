import os
import sys
import shutil

def optimize_images(src_dir, dst_dir, max_width=1920, quality=80):
    from PIL import Image
    
    if not os.path.exists(src_dir):
        print(f"Source directory not found: {src_dir}")
        return

    os.makedirs(dst_dir, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        relative_root = os.path.relpath(root, src_dir)
        output_root = dst_dir if relative_root == "." else os.path.join(dst_dir, relative_root)
        os.makedirs(output_root, exist_ok=True)

        for file in files:
            src_filepath = os.path.join(root, file)
            dst_filepath = os.path.join(output_root, file)

            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    with Image.open(src_filepath) as img:
                        original_size = os.path.getsize(src_filepath)
                        
                        # Check if resize is needed
                        if img.width > max_width:
                            ratio = max_width / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                            print(f"Resizing {file}...")
                        
                        # Save with optimization
                        img.save(dst_filepath, optimize=True, quality=quality)
                        
                        new_size = os.path.getsize(dst_filepath)
                        saved = original_size - new_size
                        if saved > 0:
                            print(f"Optimized {file}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (Saved {saved/1024:.1f}KB)")
                        else:
                            print(f"Processed {file} (No size reduction)")
                            
                except Exception as e:
                    print(f"Error processing {file}: {e}")
            else:
                shutil.copy2(src_filepath, dst_filepath)

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if len(sys.argv) == 3:
        optimize_images(sys.argv[1], sys.argv[2])
    else:
        images_dir = os.path.join(root, 'assets/images')
        optimize_images(images_dir, images_dir)
