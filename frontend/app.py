# pylint: disable=C0103,C0114,C0115

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from typing import Any, Dict, List


st.set_page_config(layout="wide", page_title="Energy Dashboard")
st.title("Energy Consumption and Price Dashboard")

BACKEND_URL = "http://backend:8888"


def fetch_records_from_backend() -> List[Dict[str, Any]]:
    try:
        response = requests.get(f"{BACKEND_URL}/records")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        st.error(f"Error fetching data from backend: {exc}")
        return []


def display_records_table(records_data: List[Dict[str, Any]]) -> pd.DataFrame:
    if not records_data:
        st.write("No data available.")
        return pd.DataFrame()

    data_frame = pd.DataFrame(records_data)
    if "id" in data_frame.columns:
        st.dataframe(
            data_frame[[
                "id", "timestep", "consumption_eur", "consumption_sib",
                "price_eur", "price_sib"
            ]],
            use_container_width=True
        )
    else:
        st.dataframe(data_frame, use_container_width=True)
    return data_frame


def display_data_charts(data_frame: pd.DataFrame):
    if data_frame.empty:
        st.write("No data for charts.")
        return

    st.subheader("Charts")

    try:
        fig_consumption = px.line(
            data_frame, x="timestep", y=["consumption_eur", "consumption_sib"],
            title="Energy Consumption Dynamics (EUR vs SIB)"
        )
        st.plotly_chart(fig_consumption, use_container_width=True)
    except Exception as exc:
        st.error(f"Error displaying consumption chart: {exc}")

    try:
        fig_prices = px.line(
            data_frame, x="timestep", y=["price_eur", "price_sib"],
            title="Energy Price Dynamics (EUR vs SIB)"
        )
        st.plotly_chart(fig_prices, use_container_width=True)
    except Exception as exc:
        st.error(f"Error displaying price chart: {exc}")


def render_add_record_form():
    st.subheader("Add New Record")
    with st.form("add_record_form"):
        timestamp_input = st.text_input("Timestamp (YYYY-MM-DD HH:MM:SS)")
        consumption_eur_input = st.number_input(
            "Consumption (EUR)", min_value=0.0, format="%.2f"
        )
        consumption_sib_input = st.number_input(
            "Consumption (SIB)", min_value=0.0, format="%.2f"
        )
        price_eur_input = st.number_input("Price (EUR)", min_value=0.0, format="%.2f")
        price_sib_input = st.number_input("Price (SIB)", min_value=0.0, format="%.2f")

        submitted = st.form_submit_button("Add Record")
        if submitted:
            new_record_data = {
                "timestep": timestamp_input,
                "consumption_eur": consumption_eur_input,
                "consumption_sib": consumption_sib_input,
                "price_eur": price_eur_input,
                "price_sib": price_sib_input,
            }
            try:
                response = requests.post(
                    f"{BACKEND_URL}/records", json=new_record_data
                )
                response.raise_for_status()
                st.success("Record added successfully!")
                st.experimental_rerun()
            except requests.exceptions.RequestException as exc:
                st.error(f"Error adding record: {exc}")
                try:
                    error_detail = response.json().get("detail", str(exc))
                    st.error(f"Error details: {error_detail}")
                except Exception:  # Исправлено: E722 do not use bare 'except'
                    pass


def render_delete_record_form():
    st.subheader("Delete Record")
    record_id_to_delete = st.number_input(
        "Enter ID of record to delete", min_value=1, step=1, key="delete_id"
    )

    if st.button("Delete Record"):
        try:
            response = requests.delete(
                f"{BACKEND_URL}/records/{record_id_to_delete}"
            )
            response.raise_for_status()
            st.success(f"Record with ID {record_id_to_delete} deleted successfully!")
            st.experimental_rerun()
        except requests.exceptions.RequestException as exc:
            st.error(f"Error deleting record: {exc}")
            try:
                error_detail = response.json().get("detail", str(exc))
                st.error(f"Error details: {error_detail}")
            except Exception:  # Исправлено: E722 do not use bare 'except'
                pass


if __name__ == "__main__":
    all_records = fetch_records_from_backend()

    st.subheader("Current Records Table")
    data_frame_for_charts = display_records_table(all_records)

    if data_frame_for_charts is not None and not data_frame_for_charts.empty:
        display_data_charts(data_frame_for_charts)
    else:
        st.write("No data to display charts.")

    st.markdown("---")

    render_add_record_form()

    st.markdown("---")

    render_delete_record_form()
