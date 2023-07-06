'''
MIT License

Copyright (c) 2021 Monirul Shawon
Copyright (c) 2023 yjmd2222

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Python script to update traffic data on given repository
Original code by @MShawon for simple clone count at https://github.com/MShawon/github-clone-count-badge
Modified by @yjmd2222 to support total view counts as well as latest clone and view counts

See https://raw.githubusercontent.com/yjmd2222/fake-attendance/main/.github/workflows/stats.yml for whole process
(also copyrighted under the same license)
'''
import json

def load_json(stats):
    'loads newly pulled and saved json'
    with open(f'{stats}_now.json', 'r', encoding='utf-8') as file:
        now = json.load(file)
    with open(f'{stats}_before.json', 'r', encoding='utf-8') as file:
        before = json.load(file)
    return now, before

def timestamp_list(stats, before):
    'makes list of timestamps to compare new and saved json data by date'
    return {before[stats][i]['timestamp']: i for i in range(len(before[stats]))}

def append_json(stats, timestamps, before, now):
    'uses above timestamp list to merge new data into the previous data'
    latest = dict(before)
    for i in range(len(now[stats])):
        timestamp = now[stats][i]['timestamp']
        if timestamp in timestamps:
            latest[stats][timestamps[timestamp]] = now[stats][i]
        else:
            latest[stats].append(now[stats][i])
    return latest

def sum_counts(latest, stats):
    'sum merged counts'
    latest['count'] = sum(map(lambda x: int(x['count']), latest[stats]))
    latest['uniques'] = sum(map(lambda x: int(x['uniques']), latest[stats]))
    return latest

def sort_key(item):
    'sort by time'
    return item['timestamp']

def merge_counts(timestamps, stats_var):
    '''
    merge past data if data gets too long
    It currently supports up to 100 months
    '''
    if len(timestamps) > 100:
        remove_this = []
        stats_var.sort(key=sort_key)
        for i in range(len(timestamps) - 35):
            stats_var[i]['timestamp'] = stats_var[i]['timestamp'][:7]
            if stats_var[i]['timestamp'] == stats_var[i+1]['timestamp'][:7]:
                stats_var[i+1]['count'] +=  stats_var[i]['count']
                stats_var[i+1]['uniques'] +=  stats_var[i]['uniques']
                remove_this.append(stats_var[i])

        for item in remove_this:
            stats_var.remove(item)

    return stats_var

def dump_json(stats, latest):
    'dump processed data back to json'
    with open(f'{stats}.json', 'w', encoding='utf-8') as file:
        json.dump(latest, file, ensure_ascii=False, indent=4)

def run(stats):
    'runs the whole process'
    now, before = load_json(stats)
    timestamps = timestamp_list(stats, before)
    latest = append_json(stats, timestamps, before, now)
    latest = sum_counts(latest, stats)
    stats_var = latest[stats]
    stats_var = merge_counts(timestamps, stats_var)
    stats_var.sort(key=sort_key, reverse=True)
    dump_json(stats, latest)

for statistics in ['clones', 'views']:
    run(statistics)
