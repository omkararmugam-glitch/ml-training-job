# MLOps Model Training Pipeline using Jenkins

## Project Overview

This project demonstrates a simple **Machine Learning Operations (MLOps) pipeline** implemented using Jenkins.
The pipeline automates the workflow of training, validating, testing, and preparing a machine learning model for deployment.

The goal of this project is to simulate a **CI/CD pipeline for machine learning models**, where each stage represents a step in the lifecycle of model development.

---

## Pipeline Stages

The Jenkins pipeline consists of **7 stages**:

1. **Checkout Code**
   Simulates retrieving source code from a repository.

2. **Install Dependencies**
   Installs the required libraries for the machine learning project.

3. **Train Model**
   Executes the training script that builds the machine learning model.

4. **Archive Model**
   Saves the trained model as a Jenkins build artifact.

5. **Model Validation**
   Performs validation checks to ensure the model meets quality requirements.

6. **Model Testing**
   Runs testing procedures on the trained model.

7. **Deployment Ready**
   Prepares the trained model for deployment.

---

## Project Structure

```
ml-training-job
│
├── data
│   └── dataset.csv
│
├── src
│   └── train_model.py
│
├── requirements.txt
│
└── Jenkinsfile
```

---

## Technologies Used

* **Python** – Model training script
* **Jenkins** – CI/CD pipeline automation
* **GitHub** – Source code management
* **scikit-learn** – Machine learning library
* **pandas / numpy** – Data processing libraries

---

## Requirements

Install the required Python packages using:

```
pip install -r requirements.txt
```

---

## How the Pipeline Works

1. Jenkins starts the pipeline.
2. Dependencies are installed.
3. The training script runs.
4. A trained model is generated.
5. The model is validated and tested.
6. The trained model artifact is archived.
7. The model becomes ready for deployment.

---

## Expected Output

After successful execution of the pipeline:

* A trained model file is generated.
* Jenkins archives the model artifact.
* The pipeline completes all stages successfully.

---

## Learning Objectives

This project demonstrates:

* CI/CD for Machine Learning
* Jenkins pipeline automation
* Artifact archiving in Jenkins
* Basic MLOps workflow

---

## Author

**Omkar Sanjay**

---

## License

This project is created for educational and experimental purposes.
