import streamlit as st
import numpy as np
from utils import init
import random
from torchvision.transforms.functional import to_pil_image

init()

label_to_col_idx = {label: i for i, label in enumerate(st.session_state["labels"])}

st.title("Data Exploration")
st.markdown("See how these lungs look like")

idx = st.slider("Select Lung Image", min_value=0, max_value=len(st.session_state['train_dataset'])-1, value=80)

col1, col2= st.columns(2)
with col1:
    disease = st.selectbox("", ["Any Lung", "No Disease"] + st.session_state["labels"])
with col2:
    if st.button("Random", type="primary"):
        if disease == "Any Lung":
            idx = random.randint(0, len(st.session_state['train_dataset'])-1)
        elif disease == "No Disease":
            label_matrix = st.session_state["label_matrix"]
            indices = np.argwhere(np.sum(label_matrix, axis=1) == 0)
            idx = indices[random.randint(0, len(indices)), 0]
        else:
            label_matrix = st.session_state["label_matrix"]
            indices = np.argwhere(label_matrix[:, label_to_col_idx[disease]] == 1)
            idx = indices[random.randint(0, len(indices)), 0]

# Display lung image
img_tensor, label = st.session_state['train_dataset'][idx]
img = to_pil_image(img_tensor)
label_txt = ", ".join([st.session_state['labels'][i] for i, x in enumerate(label) if x == 1])
label_txt = "No Disease" if len(label_txt) == 0 else label_txt
st.image(img, caption=label_txt, use_column_width=True)
