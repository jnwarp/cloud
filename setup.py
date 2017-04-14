import argparse
from glob import glob
from subprocess import call

def read_folder(folder):
    files = glob(folder + '/*.md')
    for i in range(len(files)):
        files[i] = files[i][(len(folder) + 1):-3]
    return files


def read_file(path):
    file = open(path, "r")
    content = []

    # save file into array
    for line in file:
        content.append(line)

    return content


def write_file(path, content, test_mode=True):
    # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
    print('\033[1;32mConfiguring:\033[1;33m', path, '\033[0;0m')

    # do not actually save while in test mode
    if test_mode:
        return False

    file = open(path, "w")

    # write content into file
    for line in content:
        file.write(line)

    file.close()


def execute_block(title, content, test_mode=True):
    # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
    print('\033[1;32mConfiguring:\033[1;31m', title, '\033[0;0m')

    for line in content:
        # do not execute commands while in test mode
        if test_mode:
            print(line, end='')
        else:
            call(line, shell=True)

    # print blank line to separate output of commands
    print()


def find_char(line, chars=' \t'):
    flag = False

    for pos in range(len(line)):
        for char in chars:
            if flag and line[pos] == char:
                return pos
            else:
                flag = True
    return -1


def find_line(content, keyword):
    keyword = keyword.strip()
    
    # exit if the keyword is too short
    if (len(keyword) < 2):
        return -2
    
    for line_num in range(len(content)):
        line = content[line_num].strip()
        if keyword[0] == '#' and keyword[1] != ' ':
            if line[1:] == keyword[1:]:
                return line_num
            elif line[0:] == keyword[1:]:
                return line_num
        elif line[0:(len(keyword) + 1)] == ('#' + keyword):
            return line_num
        elif line[0:(len(keyword) + 2)] == ('//' + keyword):
            return line_num
        elif line[0:len(keyword)] == keyword:
            return line_num
            
    return -1


def modify_block(path, content, exact = False, test_mode = True):
    # read the target file and modify in memory
    target_content = read_file(path)
    
    # create print buffer
    print_buffer = '';

    for line in content:
        if exact:
            pos = len(line) - 1
        else:
            pos = find_char(line)

        # do not allow single character keywords
        if pos > 1:
            line_num = find_line(target_content, line[0:pos])

            # if the line is not found, add it to bottom of file
            if line_num == -1:
                print_buffer += '\033[0;33m  + ' + line[:-1] + '\033[0;0m\n'
                target_content.append(line)
                continue

            # skip operation if the lines are the same
            if target_content[line_num] == line:
                continue

            # print and highlight changes
            print_buffer += '\033[0;0m  - ' + target_content[line_num][:-1] + '\033[0;0m\n'
            print_buffer += '\033[0;33m  + ' + line[:-1] + '\033[0;0m\n'

            # modify the line in the file
            target_content[line_num] = line

    write_file(path, target_content, test_mode)
    
    # output the print buffer
    print(print_buffer)


def process(content, test_mode = False):
    # define variables
    execute_flag = False
    modify_flag = False
    i = 0

    for line in content:
        if execute_flag == False and modify_flag == False and (line == '```\n' or line == '```yaml\n'):
            modify_flag = i

        elif line == '```bash\n':
            execute_flag = i

        elif line == '```\n':
            if execute_flag != False:
                if content[execute_flag - 1][0:1] == '!':
                    i += 1
                    continue

                # use line above start as title, remove newline
                # remove start indicator, only pass commands
                execute_block(
                    content[execute_flag - 1][:-1],
                    content[(execute_flag + 1):i],
                    test_mode
                )

            elif content[modify_flag - 1][0:1] == '*':
                # immediatly write the file
                write_file(
                    content[modify_flag - 1][1:-2],
                    content[(modify_flag + 1):i],
                    test_mode
                )
            elif content[modify_flag - 1][0:1] == '!':
                i += 1
                continue
            else:
                # use exact pattern matching if * indicated
                if (content[modify_flag - 1][-2] == '*'):
                    # use line above as path, remove newline
                    modify_block(
                        content[modify_flag - 1][:-2],
                        content[(modify_flag + 1):i],
                        True,
                        test_mode
                    )
                else:
                    # use line above as path, remove newline
                    modify_block(
                        content[modify_flag - 1][:-1],
                        content[(modify_flag + 1):i],
                        False,
                        test_mode
                    )

            # reset flag variables
            execute_flag = False
            modify_flag = False
        i += 1


if __name__ == '__main__':
    # create a parser for getting the distro, server(s), and host
    parser = argparse.ArgumentParser(
        description='Deploy a server based on configurations specified in ' +
        'markdown format.'
    )

    parser.add_argument(
        '--distro',
        '-d',
        default='ubuntu',
        help='Run the basic distro configuration first',
        choices=read_folder('distro')
    )

    parser.add_argument(
        '--server',
        '-s',
        help='Specify a list of servers to install and configure',
        choices=read_folder('server'),
        nargs='*'
    )

    parser.add_argument(
        '--host',
        '-H',
        help='Custom settings for the host specified',
        choices=read_folder('host')
    )

    parser.add_argument(
        '--test',
        '-t',
        help='Simulate commands and file changes',
        default='true',
        choices=['true', 'false']
    )


    # run configurations based on the selections
    args = parser.parse_args()

    # set test mode or not
    if args.test == 'false':
        test_mode = False
    else:
        test_mode = True

    if type(args.distro) == str:
        # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
        print('\033[1;31mDistro:\033[1;31m', args.distro, '\033[0;0m')
        print('\033[1;31m==================================\033[0;0m')
        process(read_file('distro/' + args.distro + '.md'), test_mode)
        print()

    if type(args.server) == list:
        for path in args.server:
            # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
            print('\033[1;31mServer:\033[1;31m', path, '\033[0;0m')
            print('\033[1;31m===========================\033[0;0m')
            process(read_file('server/' + path + '.md'), test_mode)
            print()

    if type(args.host) == str:
        # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
        print('\033[1;31mHost:\033[1;31m', args.host, '\033[0;0m')
        print('\033[1;31m==============================\033[0;0m')
        process(read_file('host/' + args.host + '.md'), test_mode)
        print()
    
    if type(args.server) == list:
        valid_servers = read_folder('server')
        for path in args.server:
            path += '-defer'
            for server in valid_servers:
                if path == server:
                    # \033[1;32m = [0 none 1 bold; 0 none 31 red 32 green 33 yellow
                    print('\033[1;31mServer:\033[1;31m', path, '\033[0;0m')
                    print('\033[1;31m===========================\033[0;0m')
                    process(read_file('server/' + path + '.md'), test_mode)
                    print()
