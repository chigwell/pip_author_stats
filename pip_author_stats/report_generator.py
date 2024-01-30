import requests
import pandas as pd
from pypistats import python_major
import matplotlib.pyplot as plt
import json
def process_row(row: pd.Series) -> pd.Series:
    row['downloads'] = int(row['downloads'])
    row['stars'] = int(row['stars'])
    row['last_updated'] = pd.to_datetime(row['last_updated'])
    return row

def calculate_summary_stats(df: pd.DataFrame) -> dict:
    total_downloads = df['downloads'].sum()
    average_stars = df['stars'].mean()
    most_recent_update = df['last_updated'].max()
    return {'total_downloads': total_downloads, 'average_stars': average_stars, 'most_recent_update': most_recent_update}

def generate_report(df: pd.DataFrame) -> None:
    if df.empty:
        print('Error: DataFrame is empty')
        return

    df = df.apply(process_row, axis=1)

    stats = calculate_summary_stats(df)

    print(f'Total downloads: {stats["total_downloads"]}')
    print(f'Average stars: {stats["average_stars"]:.2f}')
    print(f'Most recent update: {stats["most_recent_update"].date()}')
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

    # Manually process each row and convert to appropriate types
    detailed = []
    for _, row in df.iterrows():
        record = {}
        for key, value in row.items():
            # Convert pandas types to native Python types
            if pd.api.types.is_integer_dtype(type(value)):
                record[key] = int(value)
            elif pd.api.types.is_float_dtype(type(value)):
                record[key] = float(value)
            elif pd.api.types.is_object_dtype(type(value)):
                record[key] = str(value)
            else:
                record[key] = value
        detailed.append(record)

    # Calculate total downloads
    total_downloads = sum(record['total_downloads'] for record in detailed if 'total_downloads' in record)

    summary = {
        'Total Packages': len(detailed),
        'Total Downloads': total_downloads,
        'Average Downloads': total_downloads / len(detailed) if detailed else 0,
        'Max Downloads': max(record['total_downloads'] for record in detailed if 'total_downloads' in record),
        'Min Downloads': min(record['total_downloads'] for record in detailed if 'total_downloads' in record),
        'Package with Most Downloads': max(detailed, key=lambda x: x['total_downloads'])['package'] if detailed else None
    }

    return json.dumps({"Summary Report": summary, "Detailed Report": detailed}, indent=4)
