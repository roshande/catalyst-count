import numpy as np
import pandas as pd
from .models import Companies


def preprocess_companies(chunk):
    column_renames = {
        "size range": "size_range", "year founded": "year_founded",
        "linkedin url": "linkedin_url",
        "current employee estimate": "current_employee_estimate",
        "total employee estimate": "total_employee_estimate"
    }
    csv_data = chunk.rename(columns=column_renames)
    csv_data["year_founded"] = pd.to_numeric(
        csv_data["year_founded"], errors="coerce")
    csv_data["current_employee_estimate"] = pd.to_numeric(
        csv_data["current_employee_estimate"], errors="coerce")
    csv_data["total_employee_estimate"] = pd.to_numeric(
        csv_data["total_employee_estimate"], errors="coerce")
    csv_data["year_founded"] = csv_data["year_founded"].replace({np.nan: None})
    csv_data = csv_data.where(pd.notnull(csv_data), None)
    csv_data = csv_data.where(pd.notna(csv_data), None)
    records = csv_data.to_dict(orient="records")
    return records


def save_chunk(chunk):
    records = preprocess_companies(chunk)
    records = [Companies(**rec) for rec in records]
    Companies.objects.bulk_create(records, 9999)
