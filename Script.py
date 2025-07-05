import cv2
import numpy as np

# ----- 1. Load images -----
flag_path = "C:\\Users\\dhars\\Downloads\\flag2.jpg"
pattern_path = "C:\\Users\\dhars\\Downloads\\pattern1.jpg"

flag = cv2.imread(flag_path)
pattern = cv2.imread(pattern_path)

if flag is None or pattern is None:
    raise FileNotFoundError("❌ Flag.jpg or Pattern.jpg not found!")

# Resize pattern to match flag dimensions
pattern_resized = cv2.resize(pattern, (flag.shape[1], flag.shape[0]))

# ----- 2. Convert images to float for blending -----
flag_float = flag.astype(np.float32) / 255.0
pattern_float = pattern_resized.astype(np.float32) / 255.0

# ----- 3. Convert flag to grayscale to extract folds -----
flag_gray = cv2.cvtColor(flag_float, cv2.COLOR_BGR2GRAY)

# ----- 4. Enhance folds: normalize and use as alpha mask -----
alpha_mask = cv2.GaussianBlur(flag_gray, (21, 21), 0)
alpha_mask = cv2.normalize(alpha_mask, None, 0.4, 1.0, cv2.NORM_MINMAX)

# ----- 5. Multiply pattern by shading (simulating folds) -----
shaded_pattern = pattern_float * alpha_mask[:, :, np.newaxis]

# ----- 6. Blend pattern with original flag background -----
output_float = shaded_pattern * 0.9 + flag_float * alpha_mask[:, :, np.newaxis] * 0.1
output_img = (output_float * 255).astype(np.uint8)

# ----- 7. Save final output -----
cv2.imwrite("Output.jpg", output_img)
print("✅ Saved Output.jpg")
