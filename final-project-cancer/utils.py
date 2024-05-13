import torch
from models import VGG
import streamlit as st
from torch.utils.data import DataLoader
from medmnist import ChestMNIST
import torchvision
import numpy as np

labels = ["Infiltration", "Effusion", "Atelectasis", "Nodule", "Mass", "Consolidation", "Pneumothorax", "Pleural_Thickening", "Cardiomegaly", "Emphysema", "Edema", "Fibrosis", "Pneumonia", "Hernia"]


transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
])

@st.cache_data  # 👈 Add the caching decorator
def load_data(mode):
    df=None
    if mode=="train":
        df =ChestMNIST(split="train", download=True, size=64, transform=transform)
        return df
    else:
        df=ChestMNIST(split="test", download=True, size=64, transform=transform)
        return df
    
def init():
    if 'init' in st.session_state:
        return
    train_dataset = load_data('train')
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=False)
    st.session_state['train_dataset'] = train_dataset
    st.session_state['train_loader'] = train_loader
    st.session_state['labels'] = labels
    st.session_state['init'] = True
    label_matrix = np.vstack([label.cpu().numpy() for _, label in st.session_state['train_loader']])
    st.session_state['label_matrix'] = label_matrix