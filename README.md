# Customer Churn Prediction - End-to-End MLOps Deployment

An end-to-end Machine Learning deployment project developed as part of the ** End-to-End AI Project Deployment Capstone**.

This project demonstrates how an existing trained XGBoost Customer Churn Prediction model can be transformed into a deployable web application using REST API development, Docker containerization, and deployment-oriented engineering practices.

## Project Overview

The project takes an existing trained Customer Churn Prediction model and integrates it into a complete application consisting of a FastAPI backend and an interactive Streamlit dashboard.

The primary focus is on **MLOps and deployment engineering** - packaging, serving, containerizing, and preparing an existing machine learning model for cloud deployment rather than training a new model.

## Technology Stack

- **Programming Language:** Python
- **Machine Learning Model:** Pre-trained XGBoost Classifier
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Model Serialization:** Joblib
- **Containerization:** Docker
- **Container Orchestration:** Docker Compose
- **API Validation:** Pydantic

## Project Structure

```text
CustomerChurn-MLOps/
|
|-- app/
|   |-- main.py
|   |-- dashboard.py
|
|-- models/
|   |-- churn_model.joblib
|
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Key Features

- Loads and serves an existing trained XGBoost model.
- Exposes a REST API using FastAPI.
- Provides a health-check endpoint to monitor API and model availability.
- Validates prediction inputs using Pydantic.
- Generates customer churn predictions through the backend API.
- Provides an interactive Streamlit dashboard.
- Connects the frontend to the backend through HTTP requests.
- Packages the application into Docker containers.
- Runs the API and dashboard as separate services using Docker Compose.

## Running the Project Locally

### Prerequisites

- Python 3.12
- Docker Desktop
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/shrustipandey/CustomerChurn-MLOps.git
cd CustomerChurn-MLOps
```

### 2. Build and Start the Containers

```bash
docker compose up --build -d
```

### 3. Access the Application

| Component | URL |
|---|---|
| Streamlit Dashboard | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| Interactive API Documentation | http://localhost:8000/docs |
| API Health Check | http://localhost:8000/health |

### 4. Stop the Containers

```bash
docker compose down
```

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks API availability and model loading status |
| POST | `/predict` | Accepts customer information and returns a churn prediction |

Interactive API documentation is available at:

`http://localhost:8000/docs`

## MLOps Implementation Workflow

1. **Model Reuse:** Integrate an existing trained XGBoost model.
2. **Model Serialization:** Load the serialized model using Joblib.
3. **API Development:** Build prediction and health-check endpoints using FastAPI.
4. **Frontend Integration:** Connect the Streamlit dashboard to the backend API.
5. **Containerization:** Package the application and its dependencies using Docker.
6. **Orchestration:** Run the backend and frontend as separate services using Docker Compose.
7. **Deployment Preparation:** Prepare the containerized application for cloud deployment.

## Project Objective

The objective of this capstone is to demonstrate the engineering process involved in taking an existing machine learning model and converting it into an accessible, containerized application.

It highlights practical MLOps concepts, including model serving, REST API integration, application architecture, Docker containerization, and deployment preparation.

---

**Capstone:** End-to-End AI Project Deployment  
**Project:** Customer Churn Prediction - End-to-End MLOps Deployment  
**Domain:** Machine Learning and MLOps  
**Model:** XGBoost Customer Churn Predictor