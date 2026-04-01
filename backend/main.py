import os
import time
from typing import List, Dict

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

DATA_FILE = "data.csv"


class RecordBase(BaseModel):
    timestep: str
    consumption_eur: float
    consumption_sib: float
    price_eur: float
    price_sib: float


class RecordCreate(RecordBase):
    pass


class Record(RecordBase):
    id: int


def fetch_csv_data() -> pd.DataFrame:
    start_time = time.time()

    if not os.path.exists(DATA_FILE):
        columns = [
            "id", "timestep", "consumption_eur", "consumption_sib",
            "price_eur", "price_sib"
        ]
        empty_df = pd.DataFrame(columns=columns)
        print(f"[Timer] load_data (new file): {time.time() - start_time:.4f}s")
        return empty_df

    try:
        data_frame = pd.read_csv(DATA_FILE)

        if (
            "id" not in data_frame.columns or
            data_frame["id"].isnull().any() or
            data_frame["id"].duplicated().any()
        ):
            if not data_frame.empty:
                data_frame["id"] = range(1, len(data_frame) + 1)
            else:
                data_frame["id"] = pd.Series(dtype="int")
        else:
            data_frame["id"] = pd.to_numeric(data_frame["id"], errors="coerce")
            if data_frame["id"].isnull().any():
                data_frame.dropna(subset=["id"], inplace=True)
                if not data_frame.empty:
                    data_frame["id"] = range(1, len(data_frame) + 1)
                else:
                    data_frame["id"] = pd.Series(dtype="int")

        print(f"[Timer] load_data ({len(data_frame)} rows): {time.time() - start_time:.4f}s")
        return data_frame

    except Exception as exc:
        print(f"[Timer] load_data failed: {exc}")
        raise HTTPException(
            status_code=500,
            detail=f"Error loading data from {DATA_FILE}: {exc}"
        )


def persist_csv_data(data_frame: pd.DataFrame):
    try:
        data_frame.to_csv(DATA_FILE, index=False)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error saving data to {DATA_FILE}: {exc}"
        )


@app.get("/records", response_model=List[Record])
async def get_all_records():
    start_time = time.time()
    data_frame = fetch_csv_data()
    records_list = data_frame.to_dict("records")
    print(f"[Timer] GET /records: {time.time() - start_time:.4f}s")
    return records_list


@app.post("/records", response_model=Record)
async def create_new_record(record: RecordCreate):
    data_frame = fetch_csv_data()

    if not data_frame.empty:
        new_record_id = int(data_frame["id"].max() + 1)
    else:
        new_record_id = 1

    new_record_dict = {
        "id": new_record_id,
        "timestep": record.timestep,
        "consumption_eur": record.consumption_eur,
        "consumption_sib": record.consumption_sib,
        "price_eur": record.price_eur,
        "price_sib": record.price_sib,
    }

    new_row_df = pd.DataFrame([new_record_dict])
    data_frame = pd.concat([data_frame, new_row_df], ignore_index=True)

    persist_csv_data(data_frame)
    return new_record_dict


@app.delete("/records/{record_id}", response_model=Dict[str, str])
async def remove_record_by_id(record_id: int):
    data_frame = fetch_csv_data()

    if record_id not in data_frame["id"].values:
        raise HTTPException(
            status_code=404,
            detail=f"Record with ID {record_id} not found."
        )

    data_frame = data_frame[data_frame["id"] != record_id]
    persist_csv_data(data_frame)

    return {"message": f"Record with ID {record_id} successfully deleted."}


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": f"Unexpected error occurred: {str(exc)}"},
    )
