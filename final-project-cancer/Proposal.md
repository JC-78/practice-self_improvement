# Project Proposal

## Team members+Problem motivation

J-how, Parth, Joong Ho (Joshua) and Varun are all first-year MCDS students who are interested
in using data science for improving the interpretability of AI in the medical field.

## Dataset

We will be exploring ChestMNIST under MedMNIST. ChestMNISTcontains 112,120 frontal-view
X-Ray images of 30,805 unique patients with the text-mined 14 disease labels, which could be
formalized as a multi-label binary-class classification task. The dataset consists of 78,468
training points, 11,219 validation points and 22,433 test points).

We are able to access the dataset by

```
pip install medmnist
import medmnist
from medmnist import ChestMNIST
train_dataset = ChestMNIST(split="train", download=True, size=224)
val_dataset = ChestMNIST(split="val", download=True, size=224)
test_dataset = ChestMNIST(split="test", download=True, size=224)
```

![Screenshot 2024-04-04 at 17.20.43](https://hackmd.io/_uploads/rk6ntq2k0.png)

The distribution of the dataset is shown below:

![Screenshot 2024-04-04 at 17.21.10](https://hackmd.io/_uploads/r1RRY5h1R.png)

To augment our data, we are considering other potential data sources that could augment our main data. They are:

* MedMNIST (ChestX-ray 14): https://nihcc.app.box.com/v/ChestXray-NIHCC (huggingface)
* CheXpert: https://stanfordmlgroup.github.io/competitions/chexpert/
* MIMIC-CXR: https://physionet.org/content/mimic-cxr/2.0.0/
* Vindr-CXR: https://github.com/vinbigdata-medical/vindr-cxr
* PadCHEST: https://github.com/auriml/Rx-thorax-automatic-captioning


These five potential supplementary datasets cover different imaging modalities. Thus, integrating data from these sources could potentially enhance the diversity and generalization capabilities of our model and our findings later on.

## Research Question

We have a two major data science pursuits in this project :
* First, we try to find the correlation between different types of lung diseases present in the dataset. We do this by exploratory data analysis on the image classes and different clustering algorithms applied on the images.
* Secondly, we will try to show if there are any specific image patterns that can be used to detect the disease the person has been facing.

Here are some steps we plan to perform:

* Data Exploration: To uncover correlation patterns in the dataset we will do exploratory data analysis. We will use the multilabel classes as features and try to find which sort of diseases occur together and try to generate visualizations to view the patterns.
* Clustering: To find similarities between images of different diseases, we will try to use different clustering techniques to help identify the cluster center for different disease groups and compare how similar they are to figure out if there are any similar features that lead to different diseases.
* Model Creation: To try to classify the different types of disease images we will create a model involving CNNs which will output the probabilities of each disease for every image provided.
* Interpretability Visualizations: In this section we will try to show the interpretability of the CNN model that we create by trying to visualize what sort of features different filters are focussing on.


## Sketches and Data Analysis

### Data processing

Our team does not have to do any data cleanup, since our dataset purely consists of chest cancer images. Through neural networks, we plan on extracting hierarchical features from the data. Afterward, we will do any data processing in python. This will consist of 

Normalization: Ensure that the extracted features are on a similar scale to prevent certain features from dominating the analysis.

Dimensionality Reduction: If the extracted features result in a high-dimensional dataset, dimensionality reduction techniques such as Principal Component Analysis (PCA) or t-Distributed Stochastic Neighbor Embedding (t-SNE) can be used to reduce the number of features while preserving important information.

Feature Selection: Not all extracted features may be relevant for our analysis. Feature selection methods such as recursive feature elimination or feature importance ranking can help identify the most informative features.

### Exploratory Data Analysis

We have visualized the counts of various diseases present in our dataset. The plot is shown below : 

![Screenshot 2024-04-04 at 16.30.33](https://hackmd.io/_uploads/rycxAKny0.png)

The correlation between the occurence of various diseases can be viewed through a heatmap shown below : 

![Screenshot 2024-04-04 at 16.27.26](https://hackmd.io/_uploads/HyazD52k0.png)


Some screenshots of our data to demonstrate we have explored it
Feature extraction using clip-vit-base-patch32
Single row
![Screenshot 2024-04-04 at 2.15.08 PM](https://hackmd.io/_uploads/B1FSAPh1R.png)

Spreadsheet of multiple rows that keep track of index and 512 feature values
![Screenshot 2024-04-04 at 2.15.42 PM](https://hackmd.io/_uploads/SJlDRP2JR.png)

We also tried feature extraction using a CNN model (VGG in our case). The model first extracts features and the uses these fetures to train an MLP which outputs the image classes.
The model : 
![Screenshot 2024-04-04 at 15.57.37](https://hackmd.io/_uploads/SJiyPK2kC.png)

The features, there are 2048 features as the last layer of VGG outputs an image of size 512 * 2 * 2 : 
![Screenshot 2024-04-04 at 15.58.07](https://hackmd.io/_uploads/SyzzPKhkR.png)


### System Design

> How will you display your data? What types of interactions will you support? Provide some sketches that you have for the system design.

We will display our data using streamlit and altair. Our dashboard will provide user interaction through provision of filterable click-downs of different chest type diseases.. For example, our user can filter a few of chest diseases he/she is interested in out of 14 diseases, and our app will show the correlation plots between the diseases.  

For disease correlations : 
For pairs of diseases we can use the labels to find count of co-occurence of each disease, and display count of top 10 pairs (out of the 196 pairs)

Classification display:
The classification of a random image can be displayed. User can turn on the switch to see the explanation of the classification. Meanwhile, different model settings can be adjust down below for user to see how explanation changes along different models.

![圖片](https://hackmd.io/_uploads/Byuk4QmyA.png)

