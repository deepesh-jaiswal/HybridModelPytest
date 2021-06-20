import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/kumard/PycharmProjects/HybridModelPytest/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Login Details','baseURL')
        return url

    @staticmethod
    def getUsername():
        userName=config.get('Login Details','userName')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('Login Details', 'password')
        return password