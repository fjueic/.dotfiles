from os import system
import sys
from time import sleep
from workspace import get_current_workspace
from windows import get_window_list

argv = sys.argv

def get_hyper_terminal():
    res = get_window_list()
    for i in res:
        if 'Hyper' in i.title:
            return i
    return None

def create_new_terminal(path = ""):
    system(f'hyper "{path}"')

def main():
    term = get_hyper_terminal()
    if term:
        workspace = get_current_workspace()
        if workspace:
            term.change_workspace(workspace)
            term.bring_to_front()
            if len(argv) > 1:
                sleep(0.1)
                system('xdotool key Ctrl+Shift+e')
                sleep(0.1)
                system(f"xdotool type 'cd {argv[1]}\n'")
        else:
            print('No workspace found')
    else:
        t = ""
        if len(argv) > 1:
            t = argv[1]
        create_new_terminal(t)

if __name__ == '__main__':
    main()
