![1268108 (1)](https://user-images.githubusercontent.com/30645315/68544440-37ffdd80-03e9-11ea-8acd-3f3f9b6fc8b3.png)


# Automatic leaf infection identification


[![Join the chat at https://gitter.im/Automatic-leaf-infection-identification/Lobby](https://badges.gitter.im/Automatic-leaf-infection-identification/Lobby.svg)](https://gitter.im/Automatic-leaf-infection-identification/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### List of contents

- [Introduction](#introduction)
- [Working](#working)
- [Installation](#installation)
- [Dataset creation](#dataset-creation)
- [Running](#running)
- [License](#license)



## Introduction
---
[(Back to top)](#list-of-contents)

Since, disease detection in plants plays an important role in the agriculture field, as having a disease in plants are quite natural. If proper care is not taken in this area then it can cause serious effects on plants and due to which respective product quality, quantity or productivity is also affected.
Plant diseases cause a periodic outbreak of diseases which leads to large-scale death. These problems need to be solved at the initial stage, to save life and money of people.
Automatic detection of plant diseases is an important research topic as it may prove benefits in monitoring large fields of crops, and at a very early stage itself it detects the symptoms of diseases means when they appear on plant leaves. Farm landowners and plant caretakers (say, in a nursery) could be benefited a lot with an early disease detection, in order to prevent the worse to come to their plants and let the human know what has to be done beforehand for the same to work accordingly, in order to prevent the worse to come to him too.

This enables machine vision that is to provide image-based automatic inspection, process control. 
Comparatively, visual identification is labor intensive less accurate and can be done only in small areas. 
The project involves the use of self-designed image processing algorithms and techniques designed using python to segment the disease from the leaf while using the concepts of machine learning to categorise the plant leaves as healthy or infected.
By this method, the plant diseases can be identified at the initial stage itself and the pest and infection control tools can be used to solve pest problems while minimizing risks to people and the environment.



## Working
---
[(Back to top)](#list-of-contents)

In the initial step, the RGB images of all the leaf samples were picked up.
The step-by-step procedure of the proposed system:

+ RGB image acquisition;
+ Convert the input image from RGB to HSI format;
+ Masking the green-pixels;
+ Removal of masked green pixels;
+ Segment the components;
+ Obtain useful segments;
+ Evaluating feature parameters for classification;
+ Configuring SVM for disease detection.


**Colour Transformation:**
HSI (hue, saturation, intensity) color model is a popular color model because it is based on human perception. 
After transformation, only the H (hue) component of HSI colour space is taken into account since it provides us with the required information.

**Masking Green Pixels:**
This is performed as green colour pixel represent the healthy region of a leaf.
Green pixels are masked based on the specified threshold values.

**Segmentation:**
The infected portion of the leaf is extracted by segmenting the diseased part with other similar coloured parts (say, a brown
coloured branch of a leaf that may look like the disease) which have been considered in the masked out image, are filtered here.
All further image processing is done over a region of interest (ROI) defined at this stage.

**Classification:**
From the previous results we analyze and evaluate the features like the area of the leaf, percentage(%) of the leaf infected, the perimeter of the leaf, etc., for all the leaf images, and pass it to the SVM classifier.


## Installation
---
[(Back to top)](#list-of-contents)

These instructions assume you have `git` installed for working with Github from command window.

1. Clone the repository, and navigate to the downloaded folder. Follow below commands.
```
git clone https://github.com/johri002/Automatic-leaf-infection-identifier.git
cd Automatic-leaf-infection-identifier
```

2. Install few required pip packages, which are specified in the requirements.txt file .
```
pip3 install -r requirements.txt
```
or
```
sudo python3 setup.py install
```

3. That's it. You are ready to test the application.


## Dataset creation
---
[(Back to top)](#list-of-contents)

In `leaf sampler` directory run:
```shell
python3 leafdetectionALLsametype.py -i .
```
or
```shell
python3 leafdetectionALLmix.py -i .
```
`leafdetectionALLsametype.py` for running on one same category of images (say, all images are infected) and `leafdetectionALLmix.py` for creating dataset for both category (infected/healthy) of leaf images, in the working directory.
*Note: The code is set to run for all `.jpg`,`.jpeg` and `.png` file format images only, present in the specified directory.
       If you wish, you can add more file format support by intoducing it in the conditional statement of line 52 of both the        files.*


## Running
---
[(Back to top)](#list-of-contents)

Run the following code:
```shell
python3 GUIdriver.py
```
*where {Browse} is used to select the input image file for classifier*

The code runs on two files:
+ First, `main.py` for image segmentatin and feature extraction.
+ Second, `classifier.py` is called in `main.py` for classifying the leaf in the input image as "infected" or "healthy".

![leafdetection](https://user-images.githubusercontent.com/30645315/49014339-cb72db00-f1a5-11e8-9ceb-4010a860e162.gif)


## Links
----
[(Back to top)](#list-of-contents)

- Repository: https://github.com/johri002/Automatic-leaf-infection-identifier
- Issue tracker: https://github.com/johri002/Automatic-leaf-infection-identifier/issues
  - In case of sensitive bugs or issues, please contact shikharjohri123@gmail.com directly instead of using issue tracker. We value your effort to improve the efficiency of this project!
- Site: https://johri002.github.io/Automatic-leaf-infection-identifier/


## License
---
[(Back to top)](#list-of-contents)

The code in this project is licensed under the MIT license 2018 - Shikhar Johri.
