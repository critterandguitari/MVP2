

import pickle

class PickleableModuleWrapper(object):
    def __init__(self, module):
        # make a copy of the module's namespace in this instance
        self.__dict__ = dict(module.__dict__)
        # remove anything that's going to give us trouble during pickling
        self.remove_unpickleable_attributes()

    def remove_unpickleable_attributes(self):
        for name, value in self.__dict__.items():
            try:
                pickle.dumps(value)
            except Exception:
                del self.__dict__[name]



import masktest

masktest.inc()
masktest.inc()

p = pickle.dumps(PickleableModuleWrapper(masktest.bg))
wrapped_mod = pickle.loads(p)

print p
