import streamlit as st
import numpy as np
from utils import init
import matplotlib.pyplot as plt
import seaborn as sns

init()

st.title("Label Exploration")
st.markdown("This graph shows the co-occurrence relationship between different lung disease")

labels = st.session_state['labels']
label_matrix = st.session_state['label_matrix']
disease_counts = np.sum(label_matrix, axis=0)

# Create bar plot
fig = plt.figure(figsize=(10, 6))
plt.bar(labels, disease_counts)
plt.title('Count of Each Disease')
plt.xlabel('Disease')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

# corr_matrix = np.corrcoef(label_matrix.T)

# # Plot heatmap
# fig = plt.figure(figsize=(12, 10))
# sns.heatmap(corr_matrix, xticklabels=labels, yticklabels=labels, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation Between Diseases")

# st.pyplot(fig)

# Multi-select widget to choose labels
selected_labels = st.multiselect("Select Labels", labels, default=labels)

# Filter label matrix based on selected labels
selected_label_indices = [labels.index(label) for label in selected_labels]
selected_label_matrix = label_matrix[:, selected_label_indices]

# Compute correlation matrix for selected labels
corr_matrix = np.corrcoef(selected_label_matrix.T)

fig_heatmap = plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, xticklabels=selected_labels, yticklabels=selected_labels, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Selected Diseases")

st.pyplot(fig_heatmap)