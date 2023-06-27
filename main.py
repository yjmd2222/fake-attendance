import json

def load_json(stats):
    with open(f'{stats}.json', 'r') as fh:
        now = json.load(fh)
    with open(f'{stats}_before.json', 'r') as fh:
        before = json.load(fh)
    return now, before

def timestamp_list(stats, before):
    return {before[stats][i]['timestamp']: i for i in range(len(before[stats]))}

def append_json(stats, timestamps, before, now):
    latest = dict(before)
    for i in range(len(now[stats])):
        timestamp = now[stats][i]['timestamp']
        if timestamp in timestamps:
            latest[stats][timestamps[timestamp]] = now[stats][i]
        else:
            latest[stats].append(now[stats][i])
    return latest

def sum_counts(latest, stats):
    latest['count'] = sum(map(lambda x: int(x['count']), latest[stats]))
    latest['uniques'] = sum(map(lambda x: int(x['uniques']), latest[stats]))
    return latest

sort_key = lambda x: x['timestamp']

def merge_counts(timestamps, stats_var):
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
    with open(f'{stats}.json', 'w', encoding='utf-8') as fh:
        json.dump(latest, fh, ensure_ascii=False, indent=4)

def run(stats):
    now, before = load_json(stats)
    timestamps = timestamp_list(stats, before)
    latest = append_json(stats, timestamps, before, now)
    latest = sum_counts(latest, stats)
    stats_var = latest[stats]
    stats_var = merge_counts(timestamps, stats_var)
    stats_var.sort(key=sort_key, reverse=True)
    dump_json(stats, latest)

for stats in ['clones', 'views']:
    run(stats)