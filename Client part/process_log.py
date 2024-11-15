from os import listdir

for filename in listdir('split_files'):
    with open(f"split_files\\{filename}", "r") as f:
        with open(f"parsed_result\\{filename}", "w") as f_out:
            f_out.write("id\tdate\ttime\tsignal\n")
            for line in f.readlines():
                s_line = line.split()
                if len(s_line) > 2 and s_line[2] == "[Thread-6]":
                    try:
                        if s_line[9] != "does":
                            f_out.write(f"{s_line[9]}\t{s_line[0]}\t{s_line[1]}\t{s_line[12][:-1]}\n")
                    except :
                        ...
