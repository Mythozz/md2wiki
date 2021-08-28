import sys


def convert(source_path, target_path):
    f_input = open(source_path, "r")
    f_target = open(target_path, "w+")
    file = f_input.readlines()

    for line in file:
        if line.find("# ") > -1:
            num_items = line.count("#")
            line_new = line.replace("#", "=", num_items)
            line_new = line_new.replace("\n", "")

            add_sign = ""
            counter = 0
            while counter < num_items:
                add_sign = add_sign + "="
                counter = counter + 1
            line_new = line_new + " " + add_sign
            # print(line_new)
        elif line.find("- ") > -1:
            line_new = line.replace("- ", "* ")
            line_new = line_new.replace("\n", "")
            # print(line_new)
        else:
            line_new = line.replace("\n", "")
            # print(line_new)
        line_new = line_new + " " + "\n"
        f_target.writelines(line_new)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        convert(sys.argv[1], sys.argv[2])
    else:
        print("Error. No paths specified.")
        exit(1)