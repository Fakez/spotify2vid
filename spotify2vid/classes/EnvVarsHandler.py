import re
import environ

class EnvVarsHandler:
    def __init__(self):
        self.env_getter = environ.Env()
        ###comment this in production###
        #environ.Env.read_env() 
        ###comment this in production###

    def get_env_var(self, var_name):
        return self.env_getter(var_name)
    