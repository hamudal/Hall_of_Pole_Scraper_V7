# Pole Studio Scraper

## Overview

The Pole Studio Scraper is a comprehensive tool designed to collect and analyze data from pole dancing studios listed on eversports.de. The scraper handles URL reconstruction, validation, data extraction, and storage, making it a robust solution for gathering structured data from multiple sources.

## Features

- **URL Reconstruction**: Extracts and reformats URLs from the main studio page.
- **URL Validation**: Ensures URLs are reachable before attempting to scrape.
- **Data Scraping**: Collects detailed information about studios, workshops, and their specifics.
- **Data Storage**: Organizes and saves the collected data into CSV files for easy access and analysis.
- **Error Handling**: Continues processing despite encountering errors, ensuring maximum data retrieval.
- **Progress Tracking**: Provides real-time progress updates using `tqdm`.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pole-studio-scraper.git
    cd pole-studio-scraper
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare Initial Data**: Ensure the `polestudios_neue_liste.csv` file containing initial URLs is present in the project directory.

## Usage

1. **Run the Main Script**:
    - The main entry point for the scraper is the `a_MainFrame.ipynb` notebook, which orchestrates the entire scraping process.

    ```python
    import pandas as pd
    from a_PyCaller import process_urls
    from tqdm import tqdm

    def main():
        all_uRLs = pd.read_csv("polestudios_neue_liste.csv")
        initial_urls = all_uRLs["URL_S"].to_list()[:5]

        all_pole_studio_data = pd.DataFrame()
        all_workshops_data = pd.DataFrame()
        all_workshop_details_data = pd.DataFrame()
        all_urls_data = pd.DataFrame(columns=['URL'])

        with tqdm(initial_urls, desc="Processing URLs", dynamic_ncols=True) as pbar:
            for url in pbar:
                data = process_urls([url])
                if data:
                    # Processing logic

        # Export DataFrames to CSV
        all_pole_studio_data.to_csv("Pole_Studio_Übersicht_S.csv", index=False)
        all_workshops_data.to_csv("Workshop_Liste_SW.csv", index=False)
        all_workshop_details_data.to_csv("Workshop_Übersicht_E.csv", index=False)
        all_urls_data.to_csv("All_URLs.csv", index=False)

    if __name__ == "__main__":
        main()
    ```

2. **Process URLs**:
    - The `a_PyCaller.py` script handles the core processing, including URL reconstruction, validation, and data scraping.

    ```python
    from a_URLS_Reconstruction import reconstruct_urls_and_extract_buttons
    from b_URLS_Validation import validate_urls
    from c_PoleStudio_Overview_S import scrape_pole_studio
    from d_Workshop_List_SW import scrape_workshops
    from e_Workshop_Overview_E import scrape_workshop_details
    import pandas as pd

    def process_urls(urls):
        # URL processing logic
        return results
    ```

## Contributing

1. **Fork the Repository**: Click the 'Fork' button at the top right of the repository page.
2. **Create a New Branch**: 
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit Your Changes**: 
    ```bash
    git commit -m 'Add new feature'
    ```
4. **Push to the Branch**:
    ```bash
    git push origin feature-branch
    ```
5. **Create a Pull Request**: Submit your changes for review.

---

This project demonstrates a practical approach to web scraping and data collection, showcasing my skills in Python programming, data processing, and error handling. If you have any questions or suggestions, feel free to reach out.
