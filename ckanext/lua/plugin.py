import ckan.plugins as p
from loader import LuaLoader

class LuaPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def update_config(self, config):
        """
        Configures where the lua code can be found and also provides
        Lua the opportunity to change configuration.
        """
        self.loader = LuaLoader('/vagrant/src/ckanext-lua/default')
        pass

    def _lua_func_wrapper(self, folder, function):
        """
        Looks for the function called {{function}} in
            {{folder}}/{{function}}.lua
        and returns a python function that can be used to
        call it.
        """
        id = self.loader.load_func("{0}/{1}.lua".format(folder,function))

        # Now we need a wrapper than can look up the function by ID and
        # just pass all of it's arguments to it.
        def wrapper(*args):
            """ When called, lookup the function in the loader and call it with
            all of the args we have """
            return self.loader.get_func(id)(*args)

        return wrapper


    def get_helpers(self):
        """
        Looks for all .lua files in the configured directory and
        then will return a dictionary containing the names (based on the
        first part of the file name) and a python function wrapper around
        the contained lua code. The helper function should be named after
        the function, so 'capitalize' will be provided in helpers/capitalize.lua
        in a function called capitalize.
        """
        return {
            # For testing. When implementing just look in the folder.
            'capitalize': self._lua_func_wrapper('helpers','capitalize'),
        }