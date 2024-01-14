import requests
import pandas as pd
from pypistats import python_major
import matplotlib.pyplot as plt
import json
from bs4 import BeautifulSoup

def fetch_packages_by_author(author):
    url = f"https://pypi.org/user/{author}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    package_names = [elem.find('h3', class_='package-snippet__title').text.strip() for elem in soup.find_all('a', class_='package-snippet') if elem.find('h3', class_='package-snippet__title')]
    return package_names

def fetch_download_stats(package_name):
    try:
        response = python_major(package_name, format="json")
        stats = json.loads(response) if isinstance(response, str) else response
        if not stats.get('data'):
            return {'package': package_name, 'total_downloads': 0}
        total_downloads = sum(item.get('downloads', 0) for item in stats['data'])
        return {'package': package_name, 'total_downloads': total_downloads}
    except Exception as e:
        return {'package': package_name, 'error': str(e)}

def generate_report(author):
    packages = fetch_packages_by_author(author)
    all_stats = [fetch_download_stats(package) for package in packages]
    df = pd.DataFrame(all_stats)

    if df.empty or not pd.api.types.is_numeric_dtype(df['total_downloads']):
        return json.dumps({"message": "No valid download data available for any packages."})

    # Convert int64 fields to native Python int for JSON serialization
    df['total_downloads'] = df['total_downloads'].apply(lambda x: int(x) if pd.notnull(x) else x)

    # Calculate total downloads
    total_downloads = df['total_downloads'].sum()

    summary = {
        'Total Packages': len(df),
        'Total Downloads': total_downloads,
        'Average Downloads': df['total_downloads'].mean() if not df.empty else 0,
        'Max Downloads': df['total_downloads'].max() if not df.empty else 0,
        'Min Downloads': df['total_downloads'].min() if not df.empty else 0
    }

    if not df.empty and 'total_downloads' in df and df['total_downloads'].max() > 0:
        most_downloaded_package = df.sort_values('total_downloads', ascending=False).iloc[0]
        summary['Package with Most Downloads'] = most_downloaded_package['package']

    detailed = df.sort_values(by='total_downloads', ascending=False).to_dict(orient='records')
    return json.dumps({"Summary Report": summary, "Detailed Report": detailed}, indent=4)

# Example usage
# author = "eugene.evstafev"
# combined_json_report = generate_report(author)
# print(combined_json_report)


# Example usage
author = "eugene.evstafev"
combined_json_report = generate_report(author)
print(combined_json_report)