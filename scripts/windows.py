from os import system
from utils import run_command
class Window:
    def __init__(self, s):
        self.input = s
        t = s.split()
        self.id = t[0]
        self.desktop = t[1]
        self.host = t[2]
        self.title = ' '.join(t[3:])
    def change_workspace(self, workspace):
        system(f'wmctrl -i -r {self.id} -t {workspace.index}')
    def bring_to_front(self):
        system(f'wmctrl -i -a {self.id}')
    def __str__(self):
        return f"""input: {self.input}
id: {self.id}
desktop: {self.desktop}
host: {self.host}
title: {self.title}"""

def get_window_list():
    return [Window(i) for i in
            list(
                filter(lambda x:x != "",
                       run_command('wmctrl -l').split('\n')
                       )
    )
    ]