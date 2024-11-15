from os import listdir
from datetime import datetime, timedelta
from collections import defaultdict

split_by_id: defaultdict[int, list[tuple[datetime, int]]] = defaultdict(list)

for filename in listdir("parsed_result"):
    with open(f"parsed_result/{filename}", "r") as f:
        for line in f.readlines()[1:]:
            id_, date, time, signal = line.split("\t")
            date_time = datetime.fromisoformat(date + " " + time)
            split_by_id[int(id_)].append((date_time, int(signal.split(".")[0])))

for id_ in split_by_id.keys():
    data = split_by_id[id_]
    current_main_data = datetime.fromisoformat("1970-01-01 00:00:00")
    merged_result = dict()
    for i in data:
        if i[0] - current_main_data >= timedelta(minutes=5):
            current_main_data = i[0]
            merged_result[i[0]] = [i[1], 1]
        else:
            merged_result[current_main_data][0] += i[1]
            merged_result[current_main_data][1] += 1

    updated_merged_result = dict()
    for i in merged_result:
        updated_merged_result[i] = merged_result[i][0] / merged_result[i][1]

    with open(f"merged_result/{id_}.txt", "w") as f:
        for k in updated_merged_result:
            f.write(str(k) + "\t" + str(updated_merged_result[k]) + "\n")
