import os
import pandas as pd
import streamlit as st
from a_PyCaller import process_urls
from tqdm import tqdm
from datetime import datetime

def process_and_print_results(url, all_pole_studio_data, all_workshops_data, all_workshop_details_data, all_urls_data):
    data = process_urls([url])

    if data:
        for key, df in data.items():
            if df is not None and not df.empty:
                tqdm.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - INFO - Scraping Data from: {url}")
                tqdm.write(f"{key.replace('_', ' ').title()}: {len(df)} entries")

                # Update the appropriate DataFrame
                if key == 'pole_studio_data':
                    all_pole_studio_data = pd.concat([all_pole_studio_data, df], ignore_index=True)
                elif key == 'workshops_data':
                    all_workshops_data = pd.concat([all_workshops_data, df], ignore_index=True)
                elif key == 'workshop_details':
                    all_workshop_details_data = pd.concat([all_workshop_details_data, df], ignore_index=True)

    # Add URLs to DataFrame
    all_urls_data = pd.concat([all_urls_data, pd.DataFrame({'URL': [url]})], ignore_index=True)

    return all_pole_studio_data, all_workshops_data, all_workshop_details_data, all_urls_data

def main():
    # Title of the app
    st.title("URL Processing App")

    # Upload file
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read file
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.write("Uploaded data:")
        st.write(df)

        # Choose column
        column_name = st.selectbox("Select the column to process", df.columns)

        # Select number of rows to scrape
        num_rows = st.slider("Select the number of rows to scrape", min_value=1, max_value=len(df), value=len(df))

        # Choose where to save files
        save_csv = st.checkbox("Save as CSV")
        save_excel = st.checkbox("Save as Excel")

        # Start button
        if st.button("Start"):
            # Process the URLs
            initial_urls = df[column_name][:num_rows].tolist()
            all_pole_studio_data = pd.DataFrame()
            all_workshops_data = pd.DataFrame()
            all_workshop_details_data = pd.DataFrame()
            all_urls_data = pd.DataFrame(columns=['URL'])

            # Process each URL with tqdm
            with tqdm(initial_urls, desc="Processing URLs", dynamic_ncols=True) as pbar:
                for url in pbar:
                    all_pole_studio_data, all_workshops_data, all_workshop_details_data, all_urls_data = process_and_print_results(
                        url, all_pole_studio_data, all_workshops_data, all_workshop_details_data, all_urls_data
                    )

            # Save files
            if save_csv:
                if not os.path.exists("CSV"):
                    os.makedirs("CSV")
                all_pole_studio_data.to_csv("CSV/Pole_Studio_Übersicht_S.csv", index=False)
                all_workshops_data.to_csv("CSV/Workshop_Liste_SW.csv", index=False)
                all_workshop_details_data.to_csv("CSV/Workshop_Übersicht_E.csv", index=False)
                all_urls_data.to_csv("CSV/All_URLs.csv", index=False)

            if save_excel:
                if not os.path.exists("Excel"):
                    os.makedirs("Excel")
                all_pole_studio_data.to_excel("Excel/Pole_Studio_Übersicht_S.xlsx", index=False)
                all_workshops_data.to_excel("Excel/Workshop_Liste_SW.xlsx", index=False)
                all_workshop_details_data.to_excel("Excel/Workshop_Übersicht_E.xlsx", index=False)
                all_urls_data.to_excel("Excel/All_URLs.xlsx", index=False)

            # Show processed data
            st.write("Processed data:")
            st.write(all_pole_studio_data)
            st.write(all_workshops_data)
            st.write(all_workshop_details_data)
            st.write(all_urls_data)

if __name__ == "__main__":
    main()