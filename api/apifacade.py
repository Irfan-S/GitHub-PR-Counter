from datetime import datetime
from github import Github


class GithubAPI:
    WAIT_TIME = 100 # configure this your tier

    def __init__(self, key):
        self.__instance = Github(key)
        self.__status = True
        self.__disabled_time = None

    def get_status(self):
        self.__wait_check()
        return self.__status

    def __wait_check(self):
        if not self.__status and (datetime.now() - self.__disabled_time).seconds > self.WAIT_TIME:
            self.__status = True
            self.__disabled_time = None

    def disable(self):
        self.__status = False

    def get_instance(self):
        return self.__instance


class GithubAPIFacade:
    def __init__(self, keys):
        self.__apis = [GithubAPI(key) for key in keys]
    
    def get_api(self):
        for api in self.__apis:
            if api.get_status():
                return api.get_instance()
        raise Exception('All api keys were expired!')
