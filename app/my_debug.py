def debug_print(msg, f='mark_debug.txt'):
    with open(f, 'a+') as ff:
        print(msg, file=ff)
