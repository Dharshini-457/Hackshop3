import streamlit as st
import numpy as np
import cv2
from io import BytesIO
import time
st.set_page_config(page_title="Flag Pattern Blending", page_icon=":flag:", layout="wide")
st.title("Flag Pattern Blending Tool")
st.write("Upload a flag image and a pattern image to blend them together with natural folds. Are choose the pattern from below.")
from PIL import Image
# Upload inputs
flag_file = st.file_uploader("Upload the white flag image", type=["jpg", "jpeg", "png"])
pattern_file = st.file_uploader("Upload the pattern image", type=["jpg", "jpeg", "png"])
with st.spinner("Loading..."):
        time.sleep(5)
        st.success("Done!")
if flag_file and pattern_file:
    flag = np.array(Image.open(flag_file).convert("RGB"))[:, :, ::-1]  # Convert to BGR
    pattern = np.array(Image.open(pattern_file).convert("RGB"))[:, :, ::-1]

    flag_h, flag_w = flag.shape[:2]
    pat_h, pat_w = pattern.shape[:2]
    scale = min((flag_w * 0.9) / pat_w, (flag_h * 0.9) / pat_h)
    new_w, new_h = int(pat_w * scale), int(pat_h * scale)
    resized_pattern = cv2.resize(pattern, (new_w, new_h))

    canvas = np.zeros_like(flag)
    x, y = (flag_w - new_w) // 2, (flag_h - new_h) // 2
    canvas[y:y+new_h, x:x+new_w] = resized_pattern

    # --- Cloth mask from HSV + adaptive threshold ---
    hsv = cv2.cvtColor(flag, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, (0, 0, 180), (179, 60, 255))
    gray = cv2.cvtColor(flag, cv2.COLOR_BGR2GRAY)
    mask2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)
    mask = cv2.bitwise_and(mask1, mask2)

    # --- Clean mask ---
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    alpha = cv2.GaussianBlur(mask, (21, 21), 0).astype(np.float32) / 255.0
    alpha_3c = cv2.merge([alpha] * 3)

    # --- Simulate folds ---
    flag_gray_norm = gray.astype(np.float32) / 255.0
    pattern_float = canvas.astype(np.float32) / 255.0
    for c in range(3):
        pattern_float[:, :, c] *= flag_gray_norm
    pattern_float = np.clip(pattern_float * 1.2, 0, 1)

    # --- Final blend ---
    flag_float = flag.astype(np.float32) / 255.0
    blended = alpha_3c * pattern_float + (1 - alpha_3c) * flag_float
    final = (np.clip(blended, 0, 1) * 255).astype(np.uint8)

    # Display
    with st.spinner("Loading..."):
        time.sleep(5)
        st.success("Done!")
    st.subheader("Blended Output")
    st.image(final[:, :, ::-1], caption="🖼️ Blended Output", use_column_width=True)

    # Download
    result_pil = Image.fromarray(final[:, :, ::-1])
    buf = BytesIO()
    result_pil.save(buf, format="JPEG")
    st.download_button("📥 Download Output", buf.getvalue(), file_name="Output.jpg", mime="image/jpeg")

else:
    st.info("⬆️ Please upload both the flag and pattern images.")
# Sidebar for instructions and examples
st.sidebar.title("Flag Pattern Blending Tool")
st.sidebar.write("This tool allows you to blend a pattern onto a flag image with natural folds. Upload your images to get started.")
# Display instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Upload a white flag image.
2. Upload a pattern image.
3. The tool will blend the pattern onto the flag with natural folds.
4. Download the blended output image.
""")
# Display example images
with st.sidebar:
    st.header("Example Images")
    st.write("You can use the following example images:")
    st.image("C:\\Users\\dhars\\OneDrive\\Pictures\\flag.jpg", caption="Example Flag", use_column_width=True)
    st.image("C:\\Users\\dhars\\OneDrive\\Desktop\\Am_pattern.jpg", caption="Example Pattern", use_column_width=True)
    st.image("C:\\Users\\dhars\\OneDrive\\Pictures\\output_flag.jpg", caption="Example Output", use_column_width=True)
    st.write("You can also upload your own images.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
st.sidebar.write("This tool is built using Streamlit, OpenCV, and PIL. Special thanks to the open-source community for their contributions!")
# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ by [ Developer]")       
# Add a footer
st.sidebar.markdown("---")  
st.sidebar.write("© 2023 Flag Pattern Blending Tool")
# Add a link to the source code
st.sidebar.write("[View Source Code](https://github.com/yourusername/your-repo)")           
