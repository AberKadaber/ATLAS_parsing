with open("client_files/test.out", "r") as f:
    first_line = f.readline()
    f_out = open(f"split_files/{first_line.split()[-1]}", "w")
    for i in f.readlines():
        if i[:8] == "filename":
            f_out.close()
            f_out = open(f"split_files/{i.split()[-1]}", "w")
        elif i == "end of all files":
            break
        else:
            f_out.write(i)
