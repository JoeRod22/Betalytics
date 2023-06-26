import requests
import pandas as pd

api_key = "efe85aae1f873986a4c5ff4c26b60e52"
url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=efe85aae1f873986a4c5ff4c26b60e52&regions=us&markets=h2h,spreads&oddsFormat=american'

headers = {
    "x-api-key": api_key
}

params = {
    "regions": "us",
    "oddsFormat": "american"
}

response = requests.get(url, headers=headers, params=params)

# Process the response data as needed
data = response.json()

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as an HTML file
df.to_html('odds_data.html')
