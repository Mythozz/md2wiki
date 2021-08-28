f = open("/home/mythozz/Workspace/md2wiki/mdtestfile", "r")
f_target = open("/home/mythozz/Workspace/md2wiki/wikitestfile", "w+")

file = f.readlines()

for line in file:
    if line.find("# ") > -1:
        num_items = line.count("#")
        line_new = line.replace("#", "=", num_items)
        line_new = line_new.replace("\n", "")

        addSign = ""
        counter = 0
        while counter < num_items:
            addSign = addSign + "="
            counter = counter + 1
        line_new = line_new + " " + addSign
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