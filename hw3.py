def files_writer():
    data = []
    file_number = 1
    while file_number <= 3:
        with open(f'file{file_number}.txt') as f:
            file_name = f'file{file_number}.txt'
            # print(file_name)
            data.append([len(f.readlines()), file_number, file_name])
        file_number += 1
    data.sort()
    # print(data)
    with open("output_file.txt", "w") as out:
        for each in data:
            with open(f'file{each[1]}.txt') as fi:
                out.write(f'file{each[1]}.txt\n')
                out.write(str(each[0]) + "\n")
                for line in fi:
                    out.write(line)
                out.write("\n")


files_writer()
