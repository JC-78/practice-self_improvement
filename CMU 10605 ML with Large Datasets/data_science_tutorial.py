# -*- coding: utf-8 -*-
"""data_science_tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1doqj9dQzazSqW1kaOD20qN3cVCVzwZPV

# Tutorial for Pytorch with MNIST Dataset

To begin with, we need to import pytorch to design the neural networks for training. At the same time, we can use torchvision to download the MNIST dataset and utilizer a dataloader.

Before you start, it's important that you first set-up google colab to allow for GPU. This will make running the neural network much faster. In order to do this, go to Runtime -> Change runtime type -> In Hardware Selector, change the box to GPU -> Click Save

For google colab, all of the libraries should be installed for usage, so you won't have to install pytorch, torchvision, numpy, or matplotlib. However, on a local machine, it is important to install these libraries before progressing with the tutorial.

## Tutorial Outline
For this tutorial, we're going to cover:

1. How to download MNIST with torchvision
2. How to display images from a dataset with numpy and matplotlib
3. What is a neuron and a basic neural network
4. How to create test and train functions for a neural network
5. How to tune parameters and get the gradient descent and loss functions from pytorch
6. Finally, how to display the change in loss and accuracy over time with matplotlib
7. Repeat the entire process with Fashion MNIST dataset

## Downloading MNIST Dataset
"""

import torch
from torch import nn, optim, utils
from torchvision import datasets, transforms

"""For the torchvision datasets, it is easier for future access to store them in seperate folders. As a result, it is easiest to make new directiories for the training and test folders."""

# Commented out IPython magic to ensure Python compatibility.
#Make Directories
# %mkdir mnist_train_data
# %mkdir mnist_test_data

"""The parameters defined below serve two purposes. The first purpose is to define the paths we made above.

Second, we have something called "batch_size", which is used for batched training that helps for better and more accurate training of neural networks. Specifically, the goal is that instead of training a image at a time, we use the network to train multiple images at a time (in this case 64). Furthermore, in this dataset, the number of classes to be classified are 10 (which means the data is labeled into 10 seperate classes).
"""

#Parameters
batch_size = 64
classes = 10

#Paths
trainPath = "./mnist_train_data/"
valPath = "./mnist_test_data/"

"""With using torchvision for loading datasets, the paths are defined to be where the data will be saved, the download parameter makes sure the dataset is downloaded, and finally the transform parmater is used to set-up the images as matricies for training. 

Furthermore, the loader uses the batch size we defined above, with shuffle parameter on for better training during each loop of the data. However, test doesn't need shuffle parameter on since it isn't being used for training.
"""

#Get Train and Train Data
trainData = datasets.MNIST(trainPath,download=True,
                           train=True,transform=transforms.ToTensor())
testData = datasets.MNIST(valPath,download=True,
                           train=False,transform=transforms.ToTensor())
#Load The Images
trainLoader = utils.data.DataLoader(trainData, batch_size=batch_size,
                                    shuffle=True)
testLoader = utils.data.DataLoader(testData, batch_size=batch_size,
                                    shuffle=False)

"""## Displaying MNIST Dataset

To display some of the images within mnist, we need to download matplotlib's pyplot and numpy.
"""

#Images Displayed
import matplotlib.pyplot as plt
import numpy as np

"""In this case, we can treat the dataloader as a python iterator and grab the first batch (which is of size 64 as defined in batchsize). As we see below, the shape is 64, 1, 28, 28, which means there are 64 images of size 28 by 28 stored.

The images are actually displayed below in the subplot, where we take all 64 images and display them in a 8 x 8 grid by turning the matricies back into images.

As we can see, the MNIST dataset are small images of numbers and the goal is for the neural network to actually identify the number based on the image. In this case, the only numbers are from 0-9.
"""

#Get a Batch of Images
testImages, _ = iter(trainLoader).next()
print(testImages.shape)

#Display Images
for idx in range(0,batch_size):
  plt.subplot(np.sqrt(batch_size),np.sqrt(batch_size),idx+1)
  plt.axis('off')
  plt.imshow(testImages[idx].numpy().squeeze(), cmap='gray_r')

"""

The basic layout of a neuron, where a neuron accepts inputs from an aribitrarily large number of inputs. In this case, the number of inputs is 2 (X1, X2). The nueron preforms a weighted sum on the inputs (w1* X1 + w2*X2) with an additional bias term (b).

In general, during gradient descent, the weights and the bias are adjusted iteratively to train the neural network to better classify on a specific problem.

After the weighted sum of the inputs with a bias is taken, than the output of that neuron goes onto an activation function. There are many types of activation functions, but the basic one is ReLU which takes the max of the output and 0. In other words, it makes all negative outputs of a nueron become 0.

### Neural Network

In the overall network, this neuron structure is repeated multiple times in a layer with the layers being stacked. Furthermore, it will take the neurons of the previous layer as inputs

However, for the output neuron, it may still take a weighted-average of the neurons, but it may not use a activation function. 

For our problem, we will have 10 output nodes, which each represent the confidence of the input being a number from 0-9. 

As a result, we will take the outputs and preform a log-softmax, which is a function that basically makes the node with the largest output and accentuates it more while reducing other outputs.

For this network, if we were to design it in pytorch, we would make it: 

**nn.linear(3 (# of Inputs), 4 (# of Hidden Nodes in Layer 1))** <- Function for layer for neuron.

**nn.ReLU (Activation Function)** <- Function to call ReLU Activation Function

**nn.linear(4 (# of Hidden Nodes in Layer 1), 4 (# of Hidden Nodes in Layer 2))**

**nn.ReLU (Activation Function)**

**nn.linear(4 (# of Hidden Nodes in Layer 1), 1 (# of Output Nodes))**

Then, we would take the output and treat that as the result.
"""

#Define Module Dimensions
#We Get 784, since 28 * 28 = 784
layer1 = 784

#Other Layers are more arbitrary
layer2 = 512
layer3 = 128

"""For this network, as seen above, we will make three linear layers where the first layer will taken in an input of size 784 (the 28 by 28 image compressed as one row) into a hidden layer of size 512.

The second hidden layer will take the previous layer of size 512 and output a layer of size 128.

The final layer will take the hidden layer of size 128 and turn it into a output layer of size 10.

Finally, we will do a log-softmax of the output layer and return that as the prediction of the neuron for the probability of the image being a specific number. The specific formula and parameters can be found: [Log Softmax](https://pytorch.org/docs/stable/generated/torch.nn.LogSoftmax.html)
"""

#Make the Model
class mnistDataSetModule(nn.Module):
  def __init__(self, num_class):
    super(mnistDataSetModule,self).__init__()
    #Make Different layers
    self.linOne = nn.Sequential(nn.Linear(layer1,layer2),nn.ReLU())
    self.linTwo = nn.Sequential(nn.Linear(layer2,layer3),nn.ReLU())
    self.linThree = nn.Linear(layer3,num_class)
    #Output Layer Softmax
    self.softMax = nn.LogSoftmax(dim=1)
  def forward(self,batchInput):
    #Go Through
    hiddenOutput = self.linOne(batchInput)
    hiddenOutput = self.linTwo(hiddenOutput)
    hiddenOutput = self.linThree(hiddenOutput)
    #Real Output
    realOutput = self.softMax(hiddenOutput)
    return realOutput

"""## Test and Train Functions

For the test function, we are going to take our neural network model and see how well it performs in the dataset.

### Test Variables
The input variable model represents the neural network being trained. The input variable test_load is the actual test dataloader. The variable device refers to using GPU or CPU to run dataset, where GPU is much faster than CPU. Finally, the criterion variable is the loss function we are testing against. Later on we will delve into the loss function, which it is used to see how well the output preforms against the truth.

### Test Function
The general loop of the function takes a batch of images, and the targets which are the numbers the images are trying to represent, to see how well the model predicts.

First of all, the "to" function transfers variables to GPU for faster computation, and the "views" function compress inputs to be one-dimension for each image (length: 784). Furthermore, the outputs is the result after the model, and the criterion is the loss of the output. 

We can create a prediction of the ouputs by taking the argmax for each of the 10 output rows, of an image, and say the index is our prediction on the image's number.

We will store the loss and accuracy over all images and return the results.
"""

#Test Function
def test(model, test_load, device, criterion):
  #Set Model to Eval
  model.eval()
  accuracy = 0.0
  total = 0
  test_loss = []

  #Go Through Loop
  for batch_idx, (inputs, targets) in enumerate(test_load):
     #Move it to device
     inputs = inputs.to(device)
     targets = targets.to(device)

     #Flatten Image
     inputs = inputs.view(inputs.shape[0],-1)

     #Train the Model for output
     outputs = model(inputs)
     loss = criterion(outputs, targets)
     prediction = torch.argmax(outputs,dim=1)

     #Get Accuracy
     accuracy += torch.sum(torch.eq(prediction, targets)).item()
     total += torch.numel(targets)

     #Get Loss
     test_loss.append(loss.item())

     #Empty Cache And Delete Variables
     del inputs
     del targets
     del outputs
     torch.cuda.empty_cache()
   
  #Return Average Accuracy and Loss
  return np.mean(test_loss), accuracy/total

"""### Train Variables
The input variable model represents the neural network being trained. The input variable test_load/train_load is the actual test and train dataloader respectively. The variable device refers to using GPU or CPU to run dataset. The optimizer refers to Batch Gradient Descent, which was used to train the dataset. Finally, the criterion variable is the loss function we are testing against.

### Train Function
The general loop of the function is taking a batch of images, and the targets, to improve the model based on the result. However, this loop occurs multiple times which takes into account the number of epochs to go over the training images

Again, the variables are transferred to GPU for faster computation, and the views function compress inputs to be one-dimension for each image (length: 784). 

Furthermore, the outputs is the result after the model, and the criterion is how well the loss function preformed. 

Here, the model is trained by using loss.backward and optimizer.step, which preform gradient descent to train the parameters.

Afterwards, we clear the GPU cache and delete all parameters for another loop. At the end of an epoch, we can call the test function to see how well we trained the model parameters.
"""

#Train Function
def train(model, optimizer, device, criterion, train_load, test_load):
  #Move and Set Up Variables
  criterion = criterion.to(device)
  model = model.to(device)
  model.train()

  #Get Plot of Test_Acc, Test_Loss
  test_acc_list = []
  test_loss_list = []

  #Main Loop
  for epoch in range(epochs):
    avg_loss = 0.0
    for batch_idx, (inputs, targets) in enumerate(train_load):
      #Move it to device
      inputs = inputs.to(device)
      targets = targets.to(device)

      #Flatten Image
      inputs = inputs.view(inputs.shape[0],-1)

      #Train the Model for output
      outputs = model(inputs)
      loss = criterion(outputs, targets)

      #Learn by Backpropagation
      loss.backward()

      #Optimize the Weights
      optimizer.step()

      #Print Epoch Info
      avg_loss += loss.item()
      if batch_idx % 150 == 0 and batch_idx != 0:
        print('Epoch: {}\tBatch: {}\tAvg-Loss: {:.4f}'.format(epoch+1, batch_idx, avg_loss/150))
        avg_loss = 0
      
      #Empty Cache, Delete Variables, Reset Optimizer
      optimizer.zero_grad()
      del inputs
      del targets
      del outputs
      torch.cuda.empty_cache()

    #After Epoch Send it Through Test
    test_loss, test_acc = test(model,test_load, device, criterion)
    test_acc_list.append(test_acc)
    test_loss_list.append(test_loss)
    print('Test Loss: {:.4f}\tTest Accuracy: {:.4f}\n'.
                  format(test_loss, test_acc))

    #Optional: Save Model
    #torch.save(model, './model_epoch_' + str(epoch)) 
  #Return Test Accuracy and Loss
  return test_acc_list, test_loss_list

"""## Final Parameters and Tuning

We define the epochs to be 25 and learn rate to be 0.001 as ideal parameters for the network
"""

#Other Params
epochs = 25
learn_rate = 0.001

"""Here, we can set the model to be the one we designed. At the same time, we set the loss/criterion as Negative Log Likelihood Loss, which is a popular loss module for multi-classification. 

Basically, it treats the loss as the average difference between the prediction and result across all the batches. 

The specific formula and parameters can be found: [Negative Log Likelihood Loss](https://pytorch.org/docs/stable/generated/torch.nn.NLLLoss.html)

Finally, the optimizer is normal stochastic gradient descent where the parameters and learning rate are set.
We finally train the model and see the result.
"""

#Define Main Parameters
model = mnistDataSetModule(classes)
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(),lr=learn_rate)
device = "cuda" if torch.cuda.is_available() else "cpu"

#Go Through Actual Iterations of the Model
test_acc_list, test_loss_list = train(model, optimizer, device, criterion, trainLoader, testLoader)

"""## Display Loss OverTime

We can use some simple matplotlib functions to display the test loss and accuracy changing over time.
"""

def display(test_loss, test_acc):
  #Normalize Test Loss and Add 0 for Better Display
  test_loss = [i/max(test_loss) for i in test_loss]
  test_loss.insert(0,1.0)
  test_acc.insert(0,0.0)

  #Print The Results
  plt.plot(test_loss, label = "Test Loss")
  plt.plot(test_acc, label = "Test Accuracy")
  plt.ylabel('Percent')
  plt.xlabel('Epoch')
  plt.legend()
  plt.show()

#Display Result
display(test_loss_list,test_acc_list)

"""# Fashion MNIST Dataset Walkthrough

We are going to repeat the process with a new dataset called the Fashion MNIST dataset. This dataset is similiar to normal MNIST dataset, with 10 classes, but the images being classified are clothing items. The goal of this walkthrough is to show that neural network models can be trained on a different dataset.

In this case, the type of clothes that can be found are: 

0: T-shirt/Top

1: Trouser

2: Pullover

3: Dress

4: Coat

5: Sandal

6: Shirt

7: Sneaker

8: Bag

9: Ankle Boot

## Download FMNIST Dataset
"""

# Commented out IPython magic to ensure Python compatibility.
#Make Directories
# %mkdir fmnist_train_data
# %mkdir fmnist_test_data
#Parameters
batch_size = 64
classes = 10
#Paths
trainPath = "./fmnist_test_data/"
valPath = "./fmnist_testData/"

#Get Train and Train Data
trainData = datasets.FashionMNIST(trainPath,download=True,
                           train=True,transform=transforms.ToTensor())
testData = datasets.FashionMNIST(valPath,download=True,
                           train=False,transform=transforms.ToTensor())
#Load The Images
trainLoader = utils.data.DataLoader(trainData, batch_size=batch_size,
                                    shuffle=True)
testLoader = utils.data.DataLoader(testData, batch_size=batch_size,
                                    shuffle=False)

"""## Display FMNIST Dataset"""

#Get a Batch of Images
testImages, _ = iter(trainLoader).next()
print(testImages.shape)

#Display Images
for idx in range(0,batch_size):
  plt.subplot(np.sqrt(batch_size),np.sqrt(batch_size),idx+1)
  plt.axis('off')
  plt.imshow(testImages[idx].numpy().squeeze(), cmap='gray_r')

"""## Final Parameters and Tuning"""

#Define Main Parameters
model = mnistDataSetModule(classes)
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(),lr=learn_rate)
device = "cuda" if torch.cuda.is_available() else "cpu"

#Go Through Actual Iterations of the Model
test_acc_list, test_loss_list = train(model, optimizer, device, criterion, trainLoader, testLoader)

"""## Display Changes in Accuracy/Loss"""

#Display Actual Plot
display(test_loss_list,test_acc_list)

"""# Further Resources

The tutorial only highlighted a few elements of what's possible with a MLP network in PyTorch and Torchvision. You can see and explore more in the links below:

1. [Other Torchvision Datasets](https://pytorch.org/vision/stable/datasets.html) 
2. [Different Torchvision Transformations](https://pytorch.org/vision/stable/transforms.html) 
3. [Different PyTorch Layers](https://pytorch.org/docs/stable/nn.html) 
4. [Different Neural Network Architectectures](https://towardsdatascience.com/the-mostly-complete-chart-of-neural-networks-explained-3fb6f2367464)
"""