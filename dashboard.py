from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = Path("jobs.csv")

LOCATION_COORDS = {
    "Worldwide": (20.0, 0.0),
    "USA Only": (39.8283, -98.5795),
    "United States": (39.8283, -98.5795),
    "Canada": (56.1304, -106.3468),
    "Europe": (54.5260, 15.2551),
    "UK": (55.3781, -3.4360),
    "United Kingdom": (55.3781, -3.4360),
    "Germany": (51.1657, 10.4515),
    "France": (46.2276, 2.2137),
    "Spain": (40.4637, -3.7492),
    "Netherlands": (52.1326, 5.2913),
    "Australia": (-25.2744, 133.7751),
    "India": (20.5937, 78.9629),
    "Latin America": (-14.2350, -51.9253),
    "South America": (-8.7832, -55.4915),
    "Asia": (34.0479, 100.6197),
    "Africa": (-8.7832, 34.5085),
}


def load_data() -> pd.DataFrame:
    """Load generated job data from CSV."""
    if not DATA_FILE.exists():
        st.error("jobs.csv was not found. Run `python scraper.py` first.")
        st.stop()

    return pd.read_csv(DATA_FILE)


def build_map_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Map free-form location strings to approximate regional coordinates."""
    rows: list[dict[str, float | str]] = []

    for location in dataframe["location"].dropna():
        location_text = str(location)

        for key, coordinates in LOCATION_COORDS.items():
            if key.lower() in location_text.lower():
                rows.append(
                    {
                        "location": location_text,
                        "lat": coordinates[0],
                        "lon": coordinates[1],
                    }
                )
                break

    return pd.DataFrame(rows)


def main() -> None:
    st.set_page_config(page_title="Job Listings Dashboard", layout="wide")

    dataframe = load_data()

    st.title("Job Listings Dashboard")
    st.caption("Remote job data collected from the Remotive public API")

    st.subheader("Summary Statistics")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Jobs", len(dataframe))

    with col2:
        unique_companies = (
            dataframe["company"].nunique() if "company" in dataframe.columns else 0
        )
        st.metric("Unique Companies", unique_companies)

    st.subheader("Job Locations Map")
    map_dataframe = build_map_data(dataframe)

    if not map_dataframe.empty:
        map_counts = (
            map_dataframe.groupby(["location", "lat", "lon"])
            .size()
            .reset_index(name="job_count")
        )

        map_figure = px.scatter_geo(
            map_counts,
            lat="lat",
            lon="lon",
            size="job_count",
            hover_name="location",
            hover_data={"job_count": True, "lat": False, "lon": False},
            title="Approximate Job Locations Around the World",
            projection="natural earth",
        )
        st.plotly_chart(map_figure, use_container_width=True)
    else:
        st.info("No mappable job locations were found.")

    st.subheader("Jobs by Location")
    location_counts = dataframe["location"].fillna("Unknown").value_counts().reset_index()
    location_counts.columns = ["location", "count"]

    location_figure = px.bar(
        location_counts,
        x="location",
        y="count",
        title="Number of Jobs per Location",
    )
    st.plotly_chart(location_figure, use_container_width=True)

    st.subheader("Job Listings Table")
    st.dataframe(dataframe, use_container_width=True)


if __name__ == "__main__":
    main()
