def files_writer():
    data = []
    i = 1
    while i <= 3:
        file_name = f'file{i}.txt'
        with open(file_name) as f:
            lines = f.readlines()
            data.append([len(lines), i, file_name, lines])
        i += 1
    data.sort()
    # print(data)
    with open("output_file.txt", "w") as out:
        for each in data:
            out.write(f'file{each[1]}.txt\n')
            out.write(str(each[0]) + "\n")
            for line in each[3]:
                out.write(line)
            out.write("\n")
    print("Done, check output_file")


files_writer()
