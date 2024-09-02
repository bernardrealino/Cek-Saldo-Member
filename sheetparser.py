import pandas as pd
import re

def read_google_sheet_value_by_id(sheet_url, row_id):
    # Extract the sheet_id from the URL
    sheet_id = re.search(r"/d/([a-zA-Z0-9-_]+)", sheet_url).group(1)
    
    # Extract the sheet_name from the URL or default to 'Sheet1'
    sheet_name_match = re.search(r"gid=([0-9]+)", sheet_url)
    if sheet_name_match:
        sheet_name = "Sheet1"  # Assuming GID corresponds to the default sheet name
    else:
        sheet_name = "Sheet1"
    
    # URL to access the Google Sheet as CSV
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    # Read the sheet into a pandas DataFrame
    df = pd.read_csv(url)
    
    # Find the row that matches the provided ID
    row_data = df[df['id'] == row_id]
    
    if row_data.empty:
        return f"No data found for ID: {row_id}"
    
    return row_data.iloc[0]  # Return the first matching row (as a Series)

# Example usage:

if __name__ == "__main__":
    sheet_url = "https://docs.google.com/spreadsheets/d/18LKei_sTHq6nJ7pqanun0GWbCiwF7WE-pwZQqbGL84o/edit?usp=sharing"
    row_id = "abc12"
    row_data = read_google_sheet_value_by_id(sheet_url, row_id)
    print(row_data)
