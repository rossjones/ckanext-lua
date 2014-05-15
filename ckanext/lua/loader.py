import os
import uuid

import lupa
from lupa import LuaRuntime

class LuaLoader(object):

    def __init__(self, root_folder):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.function_cache = {}
        self.root_folder = root_folder

    def load_func(self, name):
        """
        Loads a function from disk and gives it an ID.
        """
        uid = str(uuid.uuid4())
        path = os.path.join(self.root_folder, name)
        self.function_cache[uid] = self.lua.eval(open(path).read())

        return uid

    def get_func(self, id):
        """
        Returns the function based on the random id
        """
        return self.function_cache[id]