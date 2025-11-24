import numpy as np
import cv2
import os
from PIL import Image
import time


def generate_heatmap(image: Image.Image) -> Image.Image:
    img_array = np.array(image)
    if img_array.ndim == 3:
        gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        gray_img = img_array

    _, mask = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    heatmap = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
    masked_heatmap = cv2.bitwise_and(heatmap, heatmap, mask=mask)
    final_img = cv2.cvtColor(masked_heatmap, cv2.COLOR_BGR2RGB)
    return Image.fromarray(final_img)
def main() -> None:
    input_path = "sample.jpg"
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' not found! Add an image in this folder.")
        return

    print(f"[Server] Loading image ({input_path})...")
    try:
        image = Image.open(input_path)
    except Exception as err:
        print(f"Unable to open image: {err}")
        return

    width, height = image.size
    print(f"[Server] Resolution: {width}x{height} pixels")

    mid_height = height // 2
    top_box = (0, 0, width, mid_height)
    bottom_box = (0, mid_height, width, height)

    print("[Server] Decomposition into distributed tiles..")
    top_region = image.crop(top_box)
    bottom_region = image.crop(bottom_box)

    print("[Agent_1] calculating tissue density mapping (Region A)..")
    time.sleep(0.5)  #delay simulation
    heatmap_top = generate_heatmap(top_region)

    print("[Agent_2] calculating tissue density mapping (Region B)..")
    time.sleep(0.5)
    heatmap_bottom = generate_heatmap(bottom_region)

    print("[Server] aggregating analyzed regions...")
    final_heatmap = Image.new("RGB", (width, height))
    final_heatmap.paste(heatmap_top, top_box)
    final_heatmap.paste(heatmap_bottom, bottom_box)

    output_path = "heatmap_result.jpg"
    final_heatmap.save(output_path)
    print(f"[Server] Analysis complete. File saved to {output_path}")
    final_heatmap.show()

if __name__ == "__main__":
    main()
