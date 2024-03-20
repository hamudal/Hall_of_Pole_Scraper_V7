import os
import pandas as pd
import streamlit as st
from tqdm import tqdm
from datetime import datetime

# Import the process_urls function from pycaller
from a_PyCaller import process_urls

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
            
            # Call process_urls function from pycaller
            results = process_urls(initial_urls)
            
            # Save files
            if save_csv:
                if not os.path.exists("CSV"):
                    os.makedirs("CSV")
                for key, value in results.items():
                    value.to_csv(f"CSV/{key}.csv", index=False)

            if save_excel:
                if not os.path.exists("Excel"):
                    os.makedirs("Excel")
                for key, value in results.items():
                    value.to_excel(f"Excel/{key}.xlsx", index=False)

            # Show processed data
            st.write("Processed data:")
            for key, value in results.items():
                st.write(f"{key}:")
                st.write(value)

if __name__ == "__main__":
    main()
