# Skin-Disease-Identification-Using-Image-Analysis
Skin Diseases Identification Using Image Analysis

Contents
1. INTRODUCTION

1.1 Overview

1.2 Purpose

2. LITERATURE SURVEY

2.1 Existing problem

2.2 Proposed solution

3. THEORETICAL ANALYSIS

3.1 Block diagram

3.2 Software designing

4. EXPERIMENTAL INVESTIGATION

5. FLOWCHART

6. RESULT

7. ADVANTAGES AND DISADVANTAGES

8. APPLICATIONS

9. CONCLUSION

10. FUTURE SCOPE

11. BIBLIOGRAPHY APPENDIX

                                                 1.INTRODUCTION

1.2 Purpose
Most of the skin diseases appear different on different skin tone. In most of the cases dermatologists are available in rural areas. In urban areas, people stall to consult medical help. So, image processing techniques help to build automated screening system for dermatology at an initial stage. The extraction of features plays a key role in helping to classify skin diseases. 
So to overcome this problem, our project provides an approach to use various computer vision based techniques like Deep Learning to find out the pattern of skin disorders and  automatically predict the various kinds of skin diseases.

1.1 Overview
Dermatological disorders are one of the most widespread diseases in the world. Skin diseases can place a heavy emotional and psychological burden on patients that may be far worse than the physical impact. 

The Dermatology remains the most uncertain and complicated branch of science because of it complicity in the  procedures involved in diagnosis of diseases related to hair, skin, nails. Increased consciousness especially among the youth of their body and beauty further aggravates


2. LITERATURE SURVEY
2.1 Existing problem
Feed forward back propagation artificial neural network is used in most of the existing systems, where the nonlinear data may not be evenly distributed. The data gets transformed by the Hidden layer (middle layer) of the multi layer network and learns the data transformation to make it linearly separable. This is an approach which gives comparatively less accurate results  A)Feed Forward Neural Network (FFNN) .These FFNN systems make use of single perception, multiple perception or Hidden layer network. The inputs are fed in such a way that no cycle is formed. Thus only the forward nodes make use of the given input and thus, reuse cannot be possible in this case leading to lesser accuracy. In single perception FFNN, the inputs are fed directly to the output node using few weights. Other networks used are hidden layer etc..           B) Hidden Layer Neural Network (HLNN). The hidden layer neural networks uses concept of abstraction. In these networks the input is fed to output nodes as a result of a function.

The estimation of output is based on the provided input. This results in a slightly more accurate result, however as the input is used only once, the possibility of cycle being formed is limited, thus achieving high accuracy is impossible. Thus an alternate solution is formed which is using convolutional neural networks  which will increase the accuracy and performance of the system to a larger extent.


2.2 Proposed solution
Uses convolutional neural network which is more accurate and data sets are faster to train. Convolutional neural network is a type of neural network which has some or all convolutional layers, it performs better in terms of large scale data and real time usage. The main contribution of our approach is as follows: 
1. A skin disease detection approach is proposed, which is based on convolution neural network using Gradient Descent Algorithm . Besides some scalable applications are proposed, for example, we explore how the system is identifying the diseases based on deep learning . This showed significant improvement in accuracy of skin disease detection.
 2. Datasets and KERAS are used Features of Proposed System 
• Based on the application the user can easily and clearly understand about the disease
• User will consult a doctor after knowing about the disease The convolutional models are prototyped and build using KERAS. The python web framework called flask is used to interact with the fire base and host web API.



   3. THEORETICAL ANALYSIS

3.1 Block diagram
![Block diagram]("https://github.com/Krisshvamsi/Skin-Disease-Identification-Using-Image-Analysis/blob/main/pic.jpg")
 

4. EXPERIMENTAL INVESTIGATION
The model is trained on processor Intel, core i5 and RAM 8GB. The system type is windows 10 ultimate of 64 bit operating.

The result has a good amount of accuracy. This model is tested with various images
and the results are good.


  
5. FLOWCHART

 

6. RESULT

When it comes to deep learning and its application for medical diagnosis, there are two main approaches. The first approach is classification that includes reducing potential outcomes (diagnosis) by mapping data to specific outcomes. The second approach is physiological data which includes medical images and data from other sources are used to identify and diagnose tumors, or other diseases .
In addition, deep learning can be used for dietary assessment support. For a certainty, deep learning is applied in various ways when it comes to medical diagnosis.

7. ADVANTAGES AND DISADVANTAGES    
     
 ADVANTAGES:
1.	CNNs currently take seconds to minutes to arrive at diagnosis when confronted with an image of a skin lesion. The inputs, algorithms, and outputs can be undertaken outside office hours and can be accessible to anyone with access to the internet. Compare this short time with the wait and travel times associated with a dermatologist appointment, which is often several months in the future or longer.
2.	The algorithms can be adaptive and they can learn from adding new images over time.
3.	CNNs are predicted to be able to diagnose lesions for a fraction of the cost of a visit to a dermatologist.
4.	CNNs have been able to perform as well as board-certified dermatologists in limited circumstances, and their accuracy will continue to improve in the future .

       DISADVANTAGES:
5.	CNNs and any tools offering diagnostic support will need to be officially approved as medical devices, and then re-approved as their algorithms expand .
6.	CNNs will likely be entirely online, using cloud-based storage, and will need to have excellent cybersecurity systems to ensure backup in case of database or server failure, and authentication processes to prevent unauthorized access. 
	
8. APPLICATIONS
Skin disease prediction :  
Acute prediction of diseases available first on hand to every citizen who uses this application, Disease Analysis possible right from home, sparing the need to visit Hospitals, Nursing homes or health centers.
Disease identification is easier using this . One can predict it without much effort.
so it can be used in small medical clinics in rural areas.

9. CONCLUSION

In this field of application, the analysis on skin disease images dataset is employed to identify five common skin diseases with a maximum accuracy level of 75% . A number of irrelevant attributes are reduced through image resizing, image rotation, are done in image preprocessing. A CNN model is trained and tested until it gives a good accuracy. Then model is saved and a UI is built using flask and HTML. Therefore, it will be the focus of next step to recognize different types of skin diseases.

10. FUTURE SCOPE

Here we made a few example disease and few example images in a datasets to identify. In future many skin diseases and not only disease based on skin every type of disease and wound can be implemented in the system for future enhancement .
This process can be extended to make this model a standard procedure for preliminary skin disease diagnosis method as it will reduce the treatment and diagnosis time.


11. BIBLIOGRAPHY APPENDIX

1.	WHO, 1997. Improving Child Health. Integrated Management of Childhood Illnesses: the Integrated Approach. World Health Organization, Geneva, WHO/CHD/97.12.

2.	WHO, Epidemiology and Management of Common Skin Diseases in Children in Developing Countries

3.	Classification of breast cancer histology images using Convolutional Neural Networks. [Teresa Araújo  ,Guilherme Aresta ,Eduardo CastroJosé Rouco,Paulo Aguiar,Catarina Eloy,António Polónia,Aurélio Campilho]

4.	IEEE,Medical image classification with convolutional neural network




