import csv
import pdb
import datetime
import json
import hashlib
import pprint

def output_data():
    with open('covid_case_table.csv') as csvfile:
        series_data = []
        cr = csv.DictReader(csvfile)
        valid_dates = []
        for fieldname in cr.fieldnames:
            try:
                valid_dates.append((fieldname, datetime.datetime.strptime(fieldname, '%m/%d/%y').date()))
            except ValueError:
                pass
        reversed_dates = valid_dates[::-1]
        current_date_key = reversed_dates[0][0]
        reversed_dates_in_pairs = list(zip(reversed_dates, reversed_dates[1:]))
        for row in cr:
            place = row['Combined_Key']
            current_cases = int(row[current_date_key])
            if current_cases < 2000:
                continue
            data = calculate_data(row, reversed_dates_in_pairs)
            if data == []:
                continue
            series_data.append({
                'name': place,
                'color': color_for(place),
                'data': data
            })
    f = open("data.js","w")
    f.write("series_data = " + json.dumps(series_data))
    f.close()

# A random color to use on the chart based on the place's name
def color_for(place):
    hex_hash = hashlib.sha1(place.encode('utf-8')).hexdigest()
    primary_colors = (
        int(hex_hash[0:2], 16),
        int(hex_hash[2:4], 16),
        int(hex_hash[4:6], 16),
    )
    return "rgba(%02d, %02d, %02d, .5)" % primary_colors

# Work backwards in time from the present.
def calculate_data(row, reversed_dates_in_pairs):
    result = []
    for today, yesterday in reversed_dates_in_pairs:
        today_cases, yesterday_cases = int(row[today[0]]), int(row[yesterday[0]])
        # Stop when we get to 200 cases -- small numbers aren't great on this graph.
        if today_cases < 200:
            return result
        if yesterday_cases == 0:
            return result
        new_cases = today_cases - yesterday_cases
        if new_cases < 0:
            continue # we can't represent negative growth.
        result.insert(0, { 'x': today_cases, 'y': new_cases, 'name': today[0] })
    return result

output_data()