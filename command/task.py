import argparse
import pendulum
import pandas as pd
from orator import DatabaseManager

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': './database/data.db',
        'prefix': ''
    }
}

db = DatabaseManager(config)

ap = argparse.ArgumentParser()
ap.add_argument('-u', '--url', required=True, help='URL to parse')
args = vars(ap.parse_args())

data = pd.read_html(args['url'])

# Prepare data
collect = data[0][3:].values.tolist()

total= collect.pop()
total.pop(0)
total.pop(2)
total.append(data[1].values[0][1])
total.append(pendulum.now().to_datetime_string())

print(total)
db.insert('insert into totals (new_cases, total_cases, deceased, recovered, last_update) values (?, ?, ?, ?, ?)', total)

for item in collect:
    # recovered, last_update rows
    item.append(data[1].values[0][1])
    item.append(pendulum.now().to_datetime_string())

    db.insert('insert into daily_reports (region, new_cases, total_cases, percentage_of_total_cases, deceased, recovered, last_update) values (?, ?, ?, ?, ?, ?, ?)', item)
