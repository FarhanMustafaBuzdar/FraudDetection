# Fraud Detection System

A machine learning project that detects whether a transaction is likely to be **fraudulent or legitimate**.

The project includes the complete workflow, starting from data preprocessing and model training to exposing the trained model through a **FastAPI** backend. The API can be used to send transaction details and get a fraud prediction.

## What This Project Does

The main goal of this project is to build a simple fraud detection system using machine learning.

The workflow includes:

* Data preprocessing and cleaning
* Exploratory data analysis
* Feature preparation
* Training a machine learning model
* Evaluating the model
* Saving the trained model
* Creating a REST API using FastAPI
* Containerizing the application using Docker

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* FastAPI
* Docker
* Git & GitHub

## Project Structure

```text
Fraud-Detection/
│
├── data/
├── models/
├── notebooks/
├── src/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

> The exact files and folders may vary depending on the current version of the project.

## Machine Learning

The model was trained using a fraud transaction dataset.

Before training, the data was processed and prepared for the machine learning algorithm. Different evaluation metrics were used to check how well the model performs.

Since fraud detection is a classification problem, the model predicts one of two classes:

* `0` → Legitimate transaction
* `1` → Fraudulent transaction

## FastAPI

The trained model is connected to a FastAPI application.

The API accepts transaction information and returns a prediction from the trained machine learning model.

For example:

```json
{
    "prediction": 0
}
```

A prediction of `0` means the transaction is considered legitimate, while `1` means it is considered potentially fraudulent.

FastAPI also provides automatic API documentation, which makes it easy to test the endpoints during development.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Fraud-Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

```bash
uvicorn app:app --reload
```

The API should now be available at:

```text
http://127.0.0.1:8000
```

You can also open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Running with Docker

If Docker is installed, the application can also be run inside a container.

Build the image:

```bash
docker build -t fraud-detection-api .
```

Run the container:

```bash
docker run -p 8000:8000 fraud-detection-api
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Future Improvements

Some things that could be added to the project in the future:

* Improve model performance
* Try different machine learning algorithms
* Add more detailed API validation
* Add authentication to the API
* Deploy the API to a cloud platform
* Add monitoring for model predictions
* Create a simple frontend for interacting with the API

## Disclaimer

This project is built for learning and demonstration purposes. The predictions should not be treated as a replacement for a production-level fraud detection system.

## Author

**M.Farhan Mustafa Buzdar**

If you found this project useful or have suggestions for improvement, feel free to check out the repository and contribute.
