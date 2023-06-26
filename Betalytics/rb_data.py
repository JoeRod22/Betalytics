import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2022/rushing.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

# Check if the table exists
if table is None:
    print(f"No table found on page {url}")
    exit()

# Get header rows
header_row = table.find('thead').find_all('tr')[-1]
headers = [header.text for header in header_row.find_all('th')][1:]  # Exclude the first column
print(f"Number of headers: {len(headers)}")

# Get all rows in the table body
rows = table.find('tbody').find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text for col in cols]
    data.append(cols)

print(f"Number of columns in data rows: {len(data[0])}")

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=headers)

# Save the DataFrame as an HTML file
df.to_html('rb_data.html', index=False)
