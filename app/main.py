from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(
    title="ConnectTel Churn Prediction API",
    description="Persevex End-to-End AI Deployment Capstone",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except Exception as exc:
    raise RuntimeError(
        f"Could not load the trained model from {MODEL_PATH}"
    ) from exc


class CustomerInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    gender: str
    SeniorCitizen: int = Field(ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: int = Field(ge=0, le=1000)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)
    TotalChargesPerTenure: float = Field(ge=0)
    ServiceCount: int = Field(ge=0, le=6)
    HasMultipleServices: int = Field(ge=0, le=1)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


@app.post("/predict")
def predict(customer: CustomerInput):
    try:
        customer_df = pd.DataFrame([customer.model_dump()])
        prediction = int(model.predict(customer_df)[0])
        probabilities = model.predict_proba(customer_df)[0]
        churn_probability = float(probabilities[1])

        return {
            "prediction": "Yes" if prediction == 1 else "No",
            "churn_probability": round(churn_probability, 4),
            "churn_probability_percent": round(
                churn_probability * 100, 2
            ),
        }

    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid customer input: {exc}",
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Check server logs.",
        ) from exc
