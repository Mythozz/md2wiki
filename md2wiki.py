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
                counter += 1
            line_new = line_new + " " + add_sign
        elif line.find("- ") > -1:
            substring = line[0:line.find("- ")]
            intend_count = int(calculate_indentation(substring))
            line_new = line.replace("- ", "* ")

            counter = 0
            line_new = line_new[line_new.find("*"):len(line_new)]
            while counter < intend_count:
                line_new = "*" + line_new
                counter += 1

            line_new = line_new.replace("\n", "")
        else:
            line_new = line.replace("\n", "")

        line_new = line_new + " " + "\n"
        f_target.writelines(line_new)


def calculate_indentation(substring):
    if substring.count("  ") % 2 == 0:
        resulting_blanks = substring.count("  ") / 2
    else:
        resulting_blanks = substring.count("  ")
    return resulting_blanks + substring.count("\t")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        convert(sys.argv[1], sys.argv[2])
    else:
        print("Error. No paths specified.")
        exit(1)
