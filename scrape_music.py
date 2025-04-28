import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def clean_views(views_str):
    """Convert views string to integer (e.g., '1,234M' to 1234000000)."""
    cleaned = re.sub(r'[^\d,]', '', views_str).replace(',', '')
    try:
        return int(cleaned)
    except ValueError:
        return 0

def scrape_year(year):
    """Scrape top 500 songs for a given year from kworb.net."""
    url = f"https://kworb.net/youtube/topvideos_published_{year}.html"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table')
        if not table:
            print(f"No table found for {year}")
            return []
        
        data = []
        rows = table.find_all('tr')[1:501]  # Skip header, limit to 500
        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 2:
                continue
                
            video = cols[0].text.strip()
            views = cols[1].text.strip()
            
            # Split video into artist and song
            try:
                artist, song = video.split(' - ', 1)
            except ValueError:
                artist, song = video, "Unknown"
                
            views_num = clean_views(views)
            
            data.append({
                'Artist': artist.strip(),
                'Song': song.strip(),
                'Views': views_num,
                'Year': year
            })
            
        print(f"Scraped {len(data)} songs for {year}")
        return data
        
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    """Main function to scrape data from 2010 to 2023 and save to CSV."""
    all_data = []
    for year in range(2010, 2024):
        yearly_data = scrape_year(year)
        all_data.extend(yearly_data)
    
    if all_data:
        # Create DataFrame
        df = pd.DataFrame(all_data)
        
        # Save to CSV
        output_file = '/Users/oluayinde/top_songs_2010_2023.csv'
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
        
        # Display first few rows
        print("\nFirst 5 rows of data:")
        print(df.head())
    else:
        print("No data was scraped.")

if __name__ == "__main__":
    main()