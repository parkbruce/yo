import os
import time
import fnmatch
import collections


class Timer:
    def __init__(self):
        self.start_t = None
        self.stop_t = None
        self.total_t = None

    def start(self):
        # if self.start_t:
            # return False
        self.start_t = time.time()

    def stop(self):
        # if self.stop_t:
            # return False
        self.stop_t = time.time()
        self.total_t = self.stop_t - self.start_t

    def get_msg(self):
        if self.total_t:
            return '\n\n\n\nTimer: %s' % self.total_t
        return False




ftype_dict = collections.defaultdict(list)
def get_fnlist(path='.', ftype=None, ext=None, regex=None):
    #TODO map ftype to ext
    if ftype:
        pass
    elif ext:
        return [fn for fn in os.listdir(path) if fn.endswith(ext)]
    elif regex:
        return [fn for fn in os.listdir(path) if fnmatch.fnmatch(fn,regex)]
    return os.listdir(path)


def get_current_directory_fnlist():
    return get_fnlist(path='.')


mydicts = ['words', 'cracklib-small']
def get_dicts():
    return [df for df in mydicts if df in os.listdir('.')]
    # for df in mydicts for fn in os.listdir('.') if df is fn


