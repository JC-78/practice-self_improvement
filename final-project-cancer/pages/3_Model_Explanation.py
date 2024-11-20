import streamlit as st
import os
from time import sleep

# label_to_col_idx = {label: i for i, label in enumerate(st.session_state["labels"])}

st.title("Model Explanation")
st.markdown("See how these lungs look like")

selected_model = st.radio("model", ["ResNet-18", "ResNet-50"])
if selected_model == "ResNet-18":
    model = "resnet18"
elif selected_model == "ResNet-50":
    model = "resnet50" # TODO: add vgg-19 gradcam

gradcam_dir = f"./images/{model}"
image_file_names = os.listdir(gradcam_dir)
epochs = sorted([int(file.replace("output_image", "").replace(".png", "")) for file in image_file_names])

autoplay = st.toggle('Auto Play')
epoch = st.select_slider("epoch", epochs, disabled=autoplay)

if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
if autoplay:
    while True:
        img_to_show = os.path.join(gradcam_dir, f"output_image{epochs[st.session_state['counter']]}.png")
        st.image(img_to_show, caption=f"Gradcam of {model} with {epoch} epoch", use_column_width=True)
        st.session_state['counter'] += 1
        st.session_state['counter'] %= len(epochs)
        sleep(1)
        st.rerun()
else:
    img_to_show = os.path.join(gradcam_dir, f"output_image{epoch}.png")
    st.image(img_to_show, caption=f"Gradcam of {model} with {epoch} epoch", use_column_width=True)