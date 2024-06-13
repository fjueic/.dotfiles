try:
    import sys
    stdin = sys.stdin.read().split('\n\n\n')[0]
    stdin = stdin.split('\n')
    mice = []
    for i in range(len(stdin)):
        if "Mouse at" in stdin[i]:
            mice.append(stdin[i+1].strip())

    print('\n'.join(mice))
except Exception as e:
    import subprocess
    # send a critical error message via notify-send
    subprocess.run(['notify-send', '-u', 'critical', 'Error in get_all_mice.py', str(e)])
