# Bike Sharing Demand Prediction

This project aims to predict the demand for bike sharing using machine learning algorithms. The goal is to accurately predict the number of rental bikes needed on an hourly basis based on various weather conditions, seasons, and other factors.

## Project Overview

### Abstract
The project uses multiple regression techniques to predict the hourly demand for bike rentals. We utilized several machine learning models, including Linear Regression, Support Vector Regressor, Random Forest Regressor, and more. The dataset used for this project is the [Seoul Bike Sharing Demand dataset](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand) from the UCI Machine Learning Repository. The best model achieved an R<sup>2</sup> score of 0.93 using the Random Forest Regressor.

### Key Features
- Data Analysis and Visualization
- Data Preprocessing
- Feature Engineering
- Model Selection and Training
- Model Evaluation
- Model Deployment

## How to Run the Project

### Prerequisites
- Python 3.6+
- Git

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/NirajBhakhar/Bike-Sharing-Demand-Prediction.git
    cd Bike-Sharing-Demand-Prediction
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv bike_sharing_env
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```sh
      bike_sharing_env\Scripts\activate
      ```
    - On macOS and Linux:
      ```sh
      source bike_sharing_env/bin/activate
      ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Exploring the Project

5. **Explore the Jupyter notebooks**:
    Navigate to the `notebooks/` directory and open the Jupyter notebooks to explore data analysis, preprocessing, model training, and evaluation steps.

### Running Inference

6. **Run the inference script**:
    Use the provided inference script to make predictions with the trained model.
    ```sh
    python -m src.inference
    ```

## Results

### Model Evaluation Metrics
The project evaluated models using various metrics such as Mean Square Error (MSE), Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and R<sup>2</sup> Score. The Random Forest Regressor performed the best with an R<sup>2</sup> score of 0.925.

| Model                  | R<sup>2</sup> Score |
|------------------------|----------|
| Ridge Regression       | 0.54     |
| Lasso Regression       | 0.54     |
| Polynomial Features    | 0.71     |
| Support Vector Regressor | 0.84   |
| K Nearest Neighbors    | 0.77     |
| Decision Tree Regressor| 0.84     |
| Random Forest Regressor| 0.93     |

## Deployment

The model has been serialized using Python's pickle library and can be used for real-time predictions. The `inference.py` module facilitates predictions based on user inputs.
