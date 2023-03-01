# APMA-2070 and ENGN 2912: Deep Learning for Scientistis and Engineers

The main objective of this course is to teach concepts and implementation of deep learning techniques for scientific and engineering problems to first year graduate students. This course entails various methods, including theory and implementation of deep leaning techniques to solve a broad range of computational problems frequently encountered in solid mechanics, fluid mechanics, non destructive evaluation of materials, systems biology, chemistry, and non-linear dynamics.


# Workload

#### Over the 13 weeks of this course (including reading period), students will spend three hours in class per week (39 hours total). A reasonable estimate to support this course’s learning outcomes is 100 hours total. Project based homework assignments may take ~30 hours, and students are expected to allocate ~30 hours to the final project.


# Instructors  
1. [Prof. George Em Karnidakis, Division of Applied Mathematics, Brown University](https://scholar.google.com/citations?user=yZ0-ywkAAAAJ&hl=en&oi=ao)
2. [Dr. Khemraj Shukla, Division of Applied Mathematics, Brown University](https://scholar.google.com/citations?user=XMWXf8sAAAAJ&hl=en&oi=ao)


## 


# Syllabus, Lectures and Codes 


**Textbook and Other Reading Materials** 

* [<span style="color:blue"> <em>Deep Learning by Ian Goodfellow, Yoshua Bengio and Aaron Courville </em> </span>](https://www.deeplearningbook.org)

* [<span style="color:blue"> <em>Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow by Auréliean Géron</em> </span>](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)

* [<span style="color:blue"> <em>Conceptual Programming with Python by Thorsten Altenkirch and Isaac Triguero</em> </span>](https://www.google.com/books/edition/Conceptual_Programming_with_Python/nUO0DwAAQBAJ?hl=en&gbpv=1&dq=conceptual+programming+with+python&printsec=frontcover)



**Learning curve**
![Learning curve](images/learning_curve.png?raw=true "Title") 



## Module I: Basics 

**Lecture 1 : Introduction** [Slides: (Jan 25,2023)](https://www.dropbox.com/s/nct8ohrir7ogiy0/Lecture_01_Introduction.pptx?dl=0)  
[No Homework]()   

**Lecture 2 : A primer on Python, NumPy, SciPy and jupyter notebooks** [Slides: (Jan 25, 2023)](https://www.dropbox.com/s/r6olq0vijentewj/Lecture_02_Primer_Python_Final.pptx?dl=0) [Jupyter Notebook](https://github.com/raj-brown/APMA2070/blob/main/Lecture_2_Notebook/python_primer.ipynb)  
[Homework\_L2](Homeworks/HW\_L2.pdf) Due Date: 2/1/2023, 11:59 PM ET

**Lecture 3: Deep Learning Networks** [Slides: (Feb 1, 2023)](https://www.dropbox.com/s/r3y5a4k0xh1r8tt/Lecture_03_Deep_Neural_Networks.pptx?dl=0) [Jupyter Notebook](Lecture_3_Notebook/lec_03.ipynb)  
[Homework\_L3](Homeworks/HW\_L3.pdf) Due Date: 3/01/2023, 11:59 PM ET


**Lecture 4: A primer on TensorFlow, PyTorch and JAX** [Slides: (Feb 8, Feb 15, 2023)](https://www.dropbox.com/s/lbwfadrl6itluos/Lecture_04_Primer_PyT_TF_JAX.pptx?dl=0) [Jupyter\_Notebook](Lecture_4_Notebook/1-pytorch.ipynb)  
[Homework\_L4](Homeworks/HW\_L4.pdf) Due Date: 3/15/2023, 11:59 PM ET


**Lecture 5: Training and Optimization** [Slides: (Feb 15, Feb 22, 2023)](https://www.dropbox.com/s/h90pl64rbqfa5jx/Lecture_05_Training_and_Optimization.pptx?dl=0) [Jupyter\_Notebook](Lecture_5_Notebook/learning_rate_scheduler.ipynb)  
[Homework\_L5]()

**Lecture 6: Neural Network Architectures** [Slides: (Feb 22, March 1, 2023)](https://www.dropbox.com/s/nen0yfkqmtptwl8/Lecture_06_NN_Architectures.pptx?dl=0) [Jupyter\_Notebook](Lecture_6_Notebook/nn_architectures.ipynb)  
[Homework\_6]()  
[end\_of\_semester\_FUN\_homework](Homeworks/end\_of\_semester\_FUN\_homeowrk.pdf) Due Date: 4/30/2023

[Feb 15, 2023: end of Module I Homework L6]::

## Module II: Neural Differential Equations

**Lecture 7: Discovering Differential Equations** [Slides: (March 1, 2023)](https://www.dropbox.com/s/fmyae0djx8l2qyh/Lecture_07_DynSystems.pptx?dl=0) [Jupyter\_Notebook](Lecture_7_Notebook/dynSys.ipynb)  


**Lecture 8: Physics-Informed Neural Networks (PINNs)- Part I**

**Lecture 9: Physics-Informed Neural Networks (PINNs)- Part II**


## Module III: Neural Operators

**Lecture 10: Deep Operator Network (DeepONet)**

**Lecture 11: Fourier Neural Operator (FNO)**

## Module IV: SciML Uncertainty Quantification (SciML-UQ)

**Lecture 12: Machine Learning using Multi-Fidelity Data**

**Lecture 13: Uncertainty Quantification(UQ) in Scientific Machine Learning**



## Advanced Topics

1. **DeepXDE framework**
2. **Multi-GPU Scientific Machine Learning** 



### Office hours  
Monday 3:00 - 5:00 PM, Location: 170 Hope St., Room No: 308, Providence RI 02906




# Term Projects

1. **Biomedicine**
   * Solving forward and inverse problems in mathematical modeling of blood coagulation: [Project Description](Projects/Projects1/blood_coagulation.pdf)  
   * Predicting drug absorption using a physics-informed neural network
   * Parameter identification in Glucose-Insulin interaction: [Project Description]
   * Parameter Estimation in Thrombus Formation: [Project Description]

2. **Dynamical Systems**
   * Charged particle in a electromagnetic field 
   * Learning dynamical systems from data
   * Stiff ODE systems

3. **Engines**
   * Learning engine parameters

4. **Fluid Mechanics**
   * Modeling Bubble Growth Dynamics
   * Reconstruction of flow past a cylinder
   * Reconstruction of flow field for a lid driven cavity flow
   * Solving forward and inverse problems in mathematical modeling of wave propagation

5. **Geophysics**
   * Microseismic hypocenter localization using PINNs
   * Diffusion-Reaction in porous media
   * Estimating sea-surface temperature using multi-fidelity data

6. **Heat Transfer**
   * Inverse heat transfer problem
   * Steady state non-linear inverse heat conduction problem
   * Heat Conduction in Double Layered Structures exposed to Ultra-short Pulsed Laser

7. **Materials**
   * Inverse Problem on Modulus Identification of Hyperelastic Material
   * Characterizing surface breaking crack using ultrasound data and PINNs

