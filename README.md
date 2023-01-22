# Deep Learning for Scientistis and Engineers: Brown University

The main objective of this course is to teach concepts and implementation of deep learning techniques for scientific and engineering problems to first year graduate students. This course entails various methods, including theory and implementation of deep leaning techniques to solve a broad range of computational problems frequently encountered in solid mechanics, fluid mechanics, non destructive evaluation of materials, systems biology, chemistry, and non-linear dynamics.

![title](./images/logos.png)












# Syllabus, Lectures and Codes 

**Lectures**: Pre-recorded videos and PDFs 

**Textbook and Other Reading Materials**: 

* [<span style="color:blue"> <em>Deep Learning by Ian Goodfellow, Yoshua Bengio and Aaron Courville </em> </span>](https://www.deeplearningbook.org)

* [<span style="color:blue"> <em>Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow by Auréliean Géron</em> </span>](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)

  



## Module I: Basics 

1. **Introduction** 
   * Deep learning: An overview
   * Deep learning in computational science and engineering (Scientific Machine Learning)
   * Types of learning
     * Supervised learning
     * Semi-supervised learning
     * Unsupervised learning
     * Self-supervised learning
     * Adversarial learning 
   
2. **A primer on Python, NumPy, SciPy and jupyter notebooks** 
   * Getting familiar with programming environment of the course 
   * Introduction of ***jupyter*** notebook and setting it up on your machine.
   * Basics of data structure and operation in NumpPy and SciPy 
   * Installation of deep learning frameworks TensorFlow and PyTorch
   * Introduction to Nvidia's deep learning container and installation

3. **Deep Learning Networks** 
   * Basics of regression model
   * Fully connected feed-forward neural networks 
   * Mathematics of neural network- The Universal Approximation Theorem 
   * Training of neural Network: Loss functions, Forward and Backward passes
   * Automatic-Differentiations: Reverse and Forward modes
   * Connection of ReLU DNN with adaptive finite elements

4. **A primer on TensorFlow and PyTorch**  
   * Brief introduction of tensors and algebraic operations on tensors using PyTorch and TensorFlow
   * A brief introduction on preparing data for training processes
   * An example of implementation of regression problem in python with and with out PyTorch and TensorFlow 
   * Demonstration on implementation of feed-forward fully-connected network in PyTorch and TensorFlow
   * Demonstration on implementation of AD process in PyTorch and TensorFlow 
   
5. **Training and Optimization** 
   * Definition and mathematics of optimization 
   * Over-fitting and under-fitting
   * Methods to solve the optimization problems
   * Demonstration on implementation of the various optimization methods in PyTorch and TensorFlow

6. **Neural Network Architectures** 
   * Convolution Neural Netowrks (CNN), Generative adversarial networks (GAN), Residual Neural Network (ResNet), Recurrent Neural Network (RNN), Long-short Time Memory Network (LSTM) 
   * Demonstration on implementation of CNN, GAN, ResNet and LSTM in PyTorch and TensorFlow



## Module II: PDEs and Operators

1. **Multi-fiiedlity Training of Neural Networks** 
   
   * Definition and mathematics of multi-fidelity data fusion and muti-fidelity neural networks
   * Demonstration on implementation of multi-fiedlity neural networks in PyTorch
   
2. **Data-Driven Dynamical Systems** 
   
   * Solving Ordinary Differential Equations (ODEs) through Neural Ordinary Differential Equation and its implementation in PyTorch
   * Multi-step and Runge-Kutta Neural Networks and demonstration of their implementation in TensorFlow
   
3. **Physics-informed Neural Networks (PINNs) for ODEs and PDEs** 
   
   * Basic concepts of PINNs
   * Demonstration on implementation of PINNs for ODEs in PyTorch and TensorFlow
   * Demonstration on implementation of PINNs for PDEs in PyTorch and TensorFlow
   
4. **PINN Extensions and Features**
   
   * vPINN, hp-VPINNs, cPINN, gPINN and XPINN etc
   * Introduction of GAN and physics-informed GANs (PI-GANs)for stochastic PDEs
   * Demonstration on implementation of GAN and PI-GAN in PyTorch
   * Introduction and theoretical background of adaptive activation function, dynamic weights and self adaptive PINNs
   * Demonstration on implementation of adaptive activation function, dynamic weights, and self adaptive PINNs in TensorFlow, SimNet and PyTorch
   
5. **Neural Operators: DeepONet and Forier Neural Operator (FNO)**

   * Introduction to operator learning - Universal approximation theorem
   * Learning operator through DeepONet and Fourier Neural Operator (FNO) approach
   * Demonstration and implementation of DeepONet in TensorFlow and Fourier Neural Operator in PyTorch
   * Uncertainity Qunatification in SciML

6. **Uncertainity Quantification in SciML**

   * Introduction and theoretical Bayesian physics-informed neural networks (B-PINNs)
   * Introduction and theoretical estimation of functional priors and posteriors using GANs
   * Demonstration and implementation of B-PINNs and functional priors and posteriors in TensorFlow
   * Demonstration of package **U-SciML**: A package for quantifying Uncertainity  in SciML
   
     

## Module III: Codes and Scalability

1. **DeepXde Library**
   
   * Introduction to Brown's DeepXde packages for PINNs.
   * Building and installing the DeepXde
   * Hands on demonstration on implementation of PINNs using DeepXde and other relevant implementation suchas debugging, geometry implementation, sampling of data points for training and testing etc.
   
2. **MODULUS Library**
   * Introduction to NVIDIA's MODULUS package for PINNs and Design pattern
   * Building MODULUS by using NVIDIA GPU CLOUD (NGC) containers
   * Demonstration on implementation of PINNs using MODULUS
   * Implementation of computational graph compilation, XLA based (Accelerated Linear Algebra) compilation, choice of precision for floats (TF32, BF16 (bFloat), FP16, FP32, FP.) vis-a-vis training cost on Nivida's latest GPU based on Ampere architecture (A100 and RTX3090) using MODULUS
   
3. **Multi-GPU Scientific Machine Learning**

   * Introduction of data parallel approach for PINN on distributed (multi-GPU) computing platform
   * Introduction of domain decomposition methods: Conservative PINN (cPINN) and Extended PINN (XPINN)
   * Sampling of training and testing data for PINNs on simple, complex and irregular geometries
   * Implementation of multi-GPU PINNs using data parallel approach in SimNet (TensorFlow) and PyTorch and MODULUS
   * Demonstration on implementation of multi-GPU cPINN and XPINN using PyTorch and TensorFlow


# Homeworks

1. **Loss Landscape**
![Function-approximation-loss-landscape](images/func.gif)



# Term Projects

1. **Biomedicine**
   * Solving forward and inverse problems in mathematical modeling of blood coagulation: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-1.pdf)  
   * Predicting drug absorption using a physics-informed neural network: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-2.pdf) 
   * Parameter identification in Glucose-Insulin interaction: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-3.pdf)
   * Parameter Estimation in Thrombus Formation: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-4.pdf)

2. **Dynamical Systems**
   * Charged particle in a electromagnetic field: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-5.pdf) 
   * Learning dynamical systems from data: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-6.pdf) 
   * Stiff ODE systems: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-7.pdf)

3. **Engines**
   * Learning engine parameters: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-8.pdf)

4. **Fluid Mechanics**
   * Modeling Bubble Growth Dynamics: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-9.pdf)
   * Reconstruction of flow past a cylinder: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-10.pdf)
   * Reconstruction of flow field for a lid driven cavity flow: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-11.pdf)
   * Solving forward and inverse problems in mathematical modeling of wave propagation: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-12.pdf)

5. **Geophysics**
   * Microseismic hypocenter localization using PINNs: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-13.pdf) 
   * Diffusion-Reaction in porous media: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-14.pdf)
   * Estimating sea-surface temperature using multi-fidelity data: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-15.pdf)

6. **Heat Transfer**
   * Inverse heat transfer problem: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-16.pdf)
   * Steady state non-linear inverse heat conduction problem: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-17.pdf)
   * Heat Conduction in Double Layered Structures exposed to Ultra-short Pulsed Laser: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-18.pdf)

7. **Materials**
   * Inverse Problem on Modulus Identification of Hyperelastic Material: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-19.pdf)
   * Characterizing surface breaking crack using ultrasound data and PINNs: [Project Description](https://github.com/raj-brown/SciML_Nvidia_Brown/blob/main/Projects/Project-20.pdf)

