# Website Data Scraper Dashboard for Job Listings

## Executive Summary

This project developed a web-based dashboard that automates the collection and visualization of job-listing data. The goal was to reduce the inefficiency of manually browsing job boards by gathering, processing, and presenting job data in a structured and interactive format.

The solution used Python to access the Remotive public API, which provides remote job listings. The collected data was cleaned, organized, and stored in a CSV file. A Streamlit dashboard then displayed the data through summary metrics, charts, a world map, and a full table.

The project demonstrates how scripting can automate a data workflow and convert raw API data into useful information.

## Introduction

Job-search platforms contain large amounts of information, but manually browsing listings can be time-consuming. This project created a Python-based workflow that collects remote-job data and presents it through an interactive dashboard.

The primary libraries and services were:

- Requests for API calls
- Pandas for data handling
- Streamlit for the web interface
- Plotly for charts and geographic visualization
- Remotive public API as the data source

## Scope

The project was designed to:

- Collect real job data using an API
- Store job data in CSV format
- Analyze and visualize the data
- Provide an interactive user interface

## Team Responsibilities

According to the original report:

- Kabir handled the scraper and dashboard coding.
- Nathan tested the script and made adjustments to the dashboard.
- Brett handled the presentation and report and also tested the code.

## Analysis and Design

The system followed this data flow:

```text
Remotive API -> scraper.py -> jobs.csv -> dashboard.py
```

The scraper retrieved data from the Remotive API and saved selected fields to CSV. The dashboard then loaded that CSV file and displayed the results.

The project used an API instead of scraping sites such as LinkedIn or Indeed because those sites can restrict or block automated scraping.

## Data Collection

The scraper processed JSON returned by the Remotive API and extracted fields including:

- Job title
- Company
- Location
- Category
- Job type
- Salary
- Publication date
- Job link
- Source
- Scrape timestamp

The collected records were saved to `jobs.csv`, with duplicate listings removed using job title, company, and job link.

## Dashboard

The Streamlit dashboard loaded `jobs.csv` with Pandas and presented:

- Total job count
- Unique company count
- Approximate world map of job locations
- Jobs-by-location bar chart
- Full job-listing table

Plotly was used for the map and bar chart.

## Results and Analysis

In the documented demo, the system collected 21 job listings from categories including software development, AI/ML, marketing, and customer service.

The data indicated that many remote listings were concentrated in the United States. The dashboard made it easier to identify patterns such as:

- Which locations had the most listings
- Which companies were hiring
- What types of jobs were available

## Limitations

The report identified two main limitations:

- Location data was not always exact.
- The project depended on the availability and structure of the external API.

The dashboard used approximate regional coordinates rather than full geocoding, so the map should be interpreted as a high-level visualization.

## Future Improvements

The original report proposed:

- Adding filters
- Storing data in a database
- Automatically updating job data

Additional portfolio-oriented improvements could include better geocoding, richer filtering, search, and deployment of the Streamlit application.

## Conclusion

This project demonstrates how Python can automate data collection and create useful visualizations. Instead of manually searching for jobs, the system collects remote-job data and presents it in an interactive interface.

Streamlit made it possible to build the dashboard without a separate frontend stack, while Requests, Pandas, and Plotly handled data retrieval, transformation, and visualization.
