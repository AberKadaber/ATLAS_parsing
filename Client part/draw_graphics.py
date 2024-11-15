import matplotlib.pyplot as plt
import datetime
import os
import matplotlib.dates as mdates

for filename in os.listdir("merged_result"):
    with open(f"merged_result/{filename}", "r") as f:
        date = []
        value = []
        for i in f.readlines():
            date.append(datetime.datetime.fromisoformat(i.split("\t")[0]))
            value.append(float(i.split("\t")[1]))

        plt.figure(figsize=(10, 6))
        plt.plot(date, value, marker='.', linestyle='', color='b',
                 label=filename.split(".")[0])

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.tight_layout()

        plt.savefig(f"graphics/{filename.split('.')[0]}.jpg", dpi=300)
