from fake_useragent import UserAgent
from conf.Settings import *
import os




class UAPool:
    def __init__(self):
        self.UAfilePath = os.path.dirname(os.path.dirname(__file__)) + '/libs/fake_useragent.json'

    def get_header(self):
        if USER_AGENT is None:
            ua = UserAgent(path=self.UAfilePath)
            return ua.random
        else:
            return USER_AGENT
