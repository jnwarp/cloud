from subprocess import call

def read_file(path):
    file = open(path, "r")
    content = []

    # save file into array
    for line in file:
        content.append(line)

    return content


def write_file(path, content):
    # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
    print('\033[1;32mConfiguring:\033[1;33m', path, '\033[0;0m')

    file = open(path, "w")

    # write content into file
    for line in content:
        file.write(line)

    file.close()


def execute_block(title, content):
    # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
    print('\033[1;32mConfiguring:\033[1;31m', title, '\033[0;0m')
    for line in content:
        call(line, shell=True)

    # print blank line to separate output of commands
    print()


def find_char(line, chars=' \t'):
    for pos in range(len(line)):
        for char in chars:
            if line[pos] == char:
                return pos
    return -1


def find_line(content, keyword):
    for line_num in range(len(content)):
        if content[line_num][0:len(keyword)] == keyword:
            return line_num
    return -1


def modify_block(path, content):
    # read the target file and modify in memory
    target_content = read_file(path)

    for line in content:
        pos = find_char(line)
        if pos > 0:
            line_num = find_line(target_content, line[0:pos])

            # if the line is not found, add it to bottom of file
            if line_num < 0:
                print('\033[0;33m  +', line[:-1], '\033[0;0m')
                target_content.append(line)
                continue

            # skip operation if the lines are the same
            if target_content[line_num] == line:
                continue

            # print and highlight changes
            print('\033[0;0m  -', target_content[line_num][:-1], '\033[0;0m')
            print('\033[0;33m  +', line[:-1], '\033[0;0m')

            # modify the line in the file
            target_content[line_num] = line
    
    write_file(path, target_content)


def process(content):
    # define variables
    execute_flag = False
    modify_flag = False
    i = 0

    for line in content:
        if execute_flag == False and modify_flag == False and line == '```\n':
            modify_flag = i

        elif line == '```bash\n':
            execute_flag = i

        elif line == '```\n':
            if execute_flag != False:
                # use line above start as title, remove newline
                # remove start indicator, only pass commands
                execute_block(
                    content[execute_flag - 1][:-1],
                    content[(execute_flag + 1):i]
                )
            elif content[modify_flag - 1][0:1] == '*':
                # immediatly write the file
                write_file(
                    content[modify_flag - 1][1:-2],
                    content[(modify_flag + 1):i]
                )
            else:
                # use line above as path, remove newline
                modify_block(
                    content[modify_flag - 1][:-1],
                    content[(modify_flag + 1):i]
                )

            # reset flag variables
            execute_flag = False
            modify_flag = False
        i += 1


#process(read_file("test/test.md"))