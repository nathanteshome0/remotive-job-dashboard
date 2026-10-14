from datetime import datetime

import pandas as pd
import requests

URL = "https://remotive.com/api/remote-jobs"
OUTPUT_FILE = "jobs.csv"


def scrape_jobs() -> list[dict[str, str]]:
    """Fetch remote job listings from the Remotive API."""
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    data = response.json()
    job_listings = data.get("jobs", [])
    jobs: list[dict[str, str]] = []

    for job in job_listings:
        jobs.append(
            {
                "job_title": job.get("title", "N/A"),
                "company": job.get("company_name", "N/A"),
                "location": job.get("candidate_required_location", "N/A"),
                "category": job.get("category", "N/A"),
                "job_type": job.get("job_type", "N/A"),
                "salary": job.get("salary", "N/A"),
                "publication_date": job.get("publication_date", "N/A"),
                "job_link": job.get("url", "N/A"),
                "source": "Remotive",
                "date_scraped": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return jobs


def save_to_csv(jobs: list[dict[str, str]], output_file: str = OUTPUT_FILE) -> None:
    """Remove duplicate listings and save the data to CSV."""
    dataframe = pd.DataFrame(jobs)

    if dataframe.empty:
        print("No jobs were returned by the API.")
        return

    dataframe.drop_duplicates(
        subset=["job_title", "company", "job_link"], inplace=True
    )
    dataframe.to_csv(output_file, index=False)
    print(f"Saved {len(dataframe)} jobs to {output_file}")


def main() -> None:
    try:
        jobs = scrape_jobs()
        save_to_csv(jobs)
    except requests.RequestException as exc:
        raise SystemExit(f"Failed to retrieve job data: {exc}") from exc


if __name__ == "__main__":
    main()
