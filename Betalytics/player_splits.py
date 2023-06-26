import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_player_game_splits(player, season):
    url = f"https://www.pro-football-reference.com/players/{player[0]}/{player}/splits/{season}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')

    # Check if the table exists
    if table is None:
        print(f"No table found on page {url}")
        return None

    # get header rows
    headers_row = table.find('thead').find_all('tr')[-1]  # get the last row of the thead
    headers = [header.text for header in headers_row.find_all('th')]
    print(f"Number of headers (Game Splits): {len(headers)}")  # print number of headers

    # get all rows in the table body
    rows = table.find('tbody').find_all('tr')

    data = []
    for row in rows:
        if row.attrs.get('class'):
            # if the row has a class attribute, it's not a regular data row and we skip it
            continue

        cols = row.find_all('td')
        cols = [col.text for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=headers[1:])
    return df

def get_player_game_logs(player, season):
    url = f"https://www.pro-football-reference.com/players/{player[0]}/{player}/gamelog/{season}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')

    # Check if the table exists
    if table is None:
        print(f"No table found on page {url}")
        return None

    # get header rows
    headers_row = table.find('thead').find_all('tr')[-1]  # get the last row of the thead
    headers = [header.text for header in headers_row.find_all('th')]
    print(f"Number of headers (Game Logs): {len(headers)}")  # print number of headers

    # get all rows in the table body
    rows = table.find('tbody').find_all('tr')

    data = []
    for row in rows:
        if row.attrs.get('class'):
            # if the row has a class attribute, it's not a regular data row and we skip it
            continue

        cols = row.find_all('td')
        cols = [col.text for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=headers[1:])
    return df

# Get game splits data
game_splits_df = get_player_game_splits("PresDa01", 2022)
game_splits_df = get_player_game_splits("BradTo00", 2022)

# Get game logs data
game_logs_df = get_player_game_logs("PresDa01", 2022)
game_logs_df = get_player_game_logs("BradTo00", 2022)

# Save the DataFrames as HTML files
game_splits_df.to_html('game_splits.html')
game_logs_df.to_html('game_logs.html')

