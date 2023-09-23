from utils import run_command
class Workspace:
    def __init__(self, s):
        self.input = s
        t = s.split()
        self.index = t[0]
        self.active = t[1] == '*'
        self.desktop_geometry = t[3]
        self.viewport = t[5]
        self.workarea_start = t[7]
        self.workarea_geometry = t[8]
        self.name = " ".join(t[9:])

    def __str__(self):
        return f"""input: {self.input}
id: {self.index}
active: {self.active}
desktop_geometry: {self.desktop_geometry}
viewport: {self.viewport}
workarea_start: {self.workarea_start}
workarea_geometry: {self.workarea_geometry}
name: {self.name}"""


def get_workspace_list():
    return [Workspace(i) for i in
            list(
                filter(lambda x:x != "",
                       run_command('wmctrl -d').split('\n')
                       )
    )
    ]


def get_current_workspace():
    res = get_workspace_list()
    for i in res:
        if i.active:
            return i
    return None