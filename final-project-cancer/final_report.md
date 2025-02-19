# Project Proposal

## Goal

We (J-how, Parth, Joong Ho and Varun) are all first-year MCDS students who are interested in improving the interpretability of AI in the medical field. To be specific, we are focusing on chest cancer, which is a leading cause of cancer-related deaths worldwide. 

Decisions based on AI recommendations directly impact patient care and outcomes. Healthcare professionals rely on AI algorithms for diagnosis, treatment planning, and prognosis. However, opaque or black-box algorithms can make it difficult for practitioners to understand how decisions are reached.  An interpretable AI model for chest cancer diagnosis provides clear explanations for its predictions, highlighting the radiological features indicative of malignancy, such as the presence of nodules, masses, or abnormal tissue densities. By understanding how the AI algorithm analyzes chest X-ray or CT images and identifies potential cancerous lesions, radiologists can corroborate the findings and make informed decisions regarding further diagnostic tests or treatment options. 

In addition,in spite of recent advances in AI technology, errors in chest cancer diagnosis can occur, leading to delayed or incorrect treatment decisions. Interpretable AI models facilitate error detection and correction by elucidating the factors contributing to misdiagnoses or false positives/negative. Thus, we emphasize the importance of nterpretable AI models that provide insights into the reasoning behind recommendations, fostering trust and confidence among healthcare providers. 

## Research Question

We have a two major data science pursuits in this project :
* First, we try to find the correlation between different types of lung diseases present in the dataset. We do this by exploratory data analysis on the image classes and different clustering algorithms applied on the images.
* Secondly, we will try to show if there are any specific image patterns that can be used to detect the disease the person has been facing.

Here are some steps we plan to perform:

* Data Exploration: To uncover correlation patterns in the dataset we will do exploratory data analysis. We will use the multilabel classes as features and try to find which sort of diseases occur together and try to generate visualizations to view the patterns.
* Clustering: To find similarities between images of different diseases, we will try to use different clustering techniques to help identify the cluster center for different disease groups and compare how similar they are to figure out if there are any similar features that lead to different diseases.
* Model Creation: To try to classify the different types of disease images we will create a model involving CNNs which will output the probabilities of each disease for every image provided.
* Interpretability Visualizations: In this section we will try to show the interpretability of the CNN model that we create by trying to visualize what sort of features different filters are focussing on.

## Related Work

To ensure AI models' reliablity and safe application, the European Union has proposed seven key requirements. They consist of the followings: (1) human agency and oversight; (2) technical robustness and safety; (3) privacy and data governance, (4) transparency; (5) diversity, non-discrimination, and fairness; (6) social and environmental well-being,(7) accountability.

To improve the AI's performance in terms of these requirements, explainable AI (XAI) has emerged. This field focuses on explaining the reasoning behind the inference of black-box model of deep learning. 

![sensors-23-00634-g003](https://hackmd.io/_uploads/Hyf1QGkb0.jpg)

For our investigation, we will apply Grad-CAM, which falls under the explanation forms category of XAI method. 

Grad-CAM is a technique for producing visual explanations that highlight important regions in an input image, thereby making the decisions of CNN-based models more transparent. Unlike previous methods that relied on attention mechanisms or modification of model architectures, Grad-CAM utilizes the gradients of any target concept flowing into the final convolutional layer to generate coarse localization maps. We felt this technique is relevant as it addresses the critical need for understanding the decision-making process of complex AI models, particularly in high-stakes applications like medical imaging, where the ability to interpret model predictions is essential for trust and adoption by healthcare professionals.

As it produces visual explanations in the form of localization maps, Grad-CAM naturally falls under the XAI's explanation forms category. This method primarily focuses on feature importance, being relatively model-agnostic, and offering instance-level explanations. By generating transparent and interpretable visualizations of CNN-based model decisions, Grad-CAM can enhance the understanding and trustworthiness of AI systems.

## Dataset

We will be exploring ChestMNIST under MedMNIST, which is a large-scale MNIST-like collection of biomedical images. MedMNIST consists of 12 datasets for 2D and 6 datasets for 3D images, which are all either preprocessed into 28x28 or 28x28x28. In addition, the dataset is standardized. To be specific, each sub-dataset is preprocessed into same format, and this allows the users to work with this data without any background knowledge. 


ChestMNIST, which is one of MedMNIST's datasets, contains 112,120 frontal-view
X-Ray images of 30,805 unique patients with the text-mined 14 disease labels, which could be
formalized as a multi-label binary-class classification task. The dataset consists of 78,468
training points, 11,219 validation points and 22,433 test points).

To access the dataset, we employ the medmnist Python library as shown below :



```
!pip install medmnist
import medmnist
from medmnist import ChestMNIST
train_dataset = ChestMNIST(split="train", download=True, size=224)
val_dataset = ChestMNIST(split="val", download=True, size=224)
test_dataset = ChestMNIST(split="test", download=True, size=224)
```

![Screenshot 2024-04-04 at 17.20.43](https://hackmd.io/_uploads/rk6ntq2k0.png)

The distribution of the dataset is shown below:

![Screenshot 2024-04-04 at 17.21.10](https://hackmd.io/_uploads/r1RRY5h1R.png)

To augment our data, we are considering other potential data sources that could complement our main data by providing more features we could explore. They are:

* MedMNIST (ChestX-ray 14): https://nihcc.app.box.com/v/ChestXray-NIHCC (huggingface)

Available through the NIH ChestX-ray14 dataset, this resource provides a collection of chest X-ray images annotated with 14 different thoracic diseases, including pneumonia, pneumothorax, and cardiomegaly.

* CheXpert: https://stanfordmlgroup.github.io/competitions/chexpert/

Released by the Stanford Machine Learning Group, CheXpert is a large dataset of chest radiographs annotated with expert radiologist interpretations for 14 common thoracic diseases.

* MIMIC-CXR: https://physionet.org/content/mimic-cxr/2.0.0/

Available through the MIMIC-CXR database hosted on PhysioNet, this dataset contains over 350,000 chest X-ray images obtained from the Medical Information Mart for Intensive Care (MIMIC) database, annotated with radiologist reports and labels for various findings and diseases.

* Vindr-CXR: https://github.com/vinbigdata-medical/vindr-cxr

Developed by the VinBigData Medical Imaging Team, Vindr-CXR is a dataset of chest X-ray images annotated with findings related to pulmonary diseases, cardiac abnormalities, and other thoracic conditions.

* PadCHEST: https://github.com/auriml/Rx-thorax-automatic-captioning

PadCHEST is a dataset of chest X-ray images collected from various sources and annotated with structured labels for pulmonary diseases, cardiac abnormalities, and other thoracic findings.

These five potential supplementary datasets cover different imaging modalities. Thus, integrating data from these sources in our future work could potentially enhance the diversity and generalization capabilities of our model and our findings later on.

### Exploratory Data Analysis

We have visualized the counts of various chest diseases present in our dataset. The plot is shown below : 

![Screenshot 2024-04-04 at 16.30.33](https://hackmd.io/_uploads/rycxAKny0.png)

From above, we can observe the label imbalance. It seems the nodule, Actelectasis and infiltration are the top 3 most commonly recorded diseases, which each has frequency of higher than 8000. On the other hand, Hermia, Pneumothorax and Effusion seem to be the least 3 recorded sieases, which each frequency of about or less than 2000. 

The correlation between the occurence of various diseases can be viewed through a heatmap shown below : 

![Screenshot 2024-04-18 at 6.02.19 PM](https://hackmd.io/_uploads/ryBY_Gk-C.png)

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


## Method

In this project, we visualized which parts of an input image are crucial for the model's prediction. First, we load either pre-trained ResNet-18 model or VGG-19 model, commonly used neural network architectures. Then, we load images from ChestMNIST and prepare it for analysis. 

Our second step is image-preprocessing. We resize the image to a standard size of 224x224 pixels and convert it into a tensor format, a data structure compatible with deep learning frameworks like PyTorch. Following this, we normalize the tensor, ensuring that its values fall within a specific range, which aids in model training and convergence. Crucially, we enable gradient computation for the input tensor, which is essential for visualization techniques relying on backpropagation, allowing us to understand how changes in the input affect the model's output. 

Next, we create an instance of SmoothGradCAM++, a method used for visualizing which image regions the model focuses on during prediction. By passing the input image tensor through the pre-trained model, we obtain the model's prediction, enabling us to identify the predicted class index. Using this index and the model's output, we extract the Class Activation Map (CAM), highlighting regions of interest in the image that contribute most to the prediction, as shown in the figure below. 

Finally, we overlay this CAM on the original image, allowing us to visually interpret the model's decision-making process and gain insights into its behavior.

![Screenshot 2024-04-27 at 6.03.36 PM](https://hackmd.io/_uploads/ryTrUgsZC.png)


## Results

An iterative example of our interpretability visualization is shown below : 

![Screenshot 2024-04-27 at 18.25.40](https://hackmd.io/_uploads/HyQ_oxsbC.png)

This shows how the model narrows its focus on the right section of the image to identify the disease as it is trained for more epochs.
 
This shows model interpretability in the sense that the medical practioners using this model can exactly see which section of the image the model is attending to when making the prediction. So the doctors can be more confident in using the models and also makes it much easier for the to verify if the model is making the right prediction.

Another interesting visualization is the heatmap shown in the dataset section. This will help the doctors realize which other diseases to test for in case of highly correlated diseases. This helps lower the cost of medical tests as it narrows down which tests are being done.

## Discussion

The histogram reveals that certain lung diseases are far more prevelant than other lung diseases, for example, Nodule, Infiltration and Atelectasis.

As observed from the correlation matrix, pairs of certain diseases can appear at the same time.  Examples of such pairs would be (Pleural Thickening, Edema) or (Pneumothorax, Emphysema). This observation is apparent from the visualization, and would aid doctors to recognize pairs of such diseases, and speculatively give medicines for both diseases for faster patient recovery. Our tool would basically assist doctors with diagnosis, potentially reducing their workload.

From the perspective of Neural Network Interpretability, our work provides a clear indication of how CNNs get better at focusing specific parts of the image, and extracting relevant information that is useful for making the prediction for classification purposes. Medical practitioners can look at such per epoch images and see if the model has correctly identified relevant locations in the image.

## Future work: 
For our future work, our directions consist of two tasks. 

Firstly, live GradCam generation.

The application itself does not support live GradCam generation yet, right now all of the images that show how models interpret the disease are pre-computed. Adding the feature of live GradCam generation adds more degree of freedom for people to play with their own data. For example they will be able to upload their own pair of lungs and see how models interact with them, or repeatedly observe a specific sequence of images to find pattern out of the model's GradCam.

Secondly, model diagnosis. 
GradCam is limited to the overall significance of each part of the image. While we might want to dissect the model and see the behaviors of different layers, more methods we need to try to analyze the explainable aspect of our CNN models.
