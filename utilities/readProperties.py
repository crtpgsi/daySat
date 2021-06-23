import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class readConfig:
    @staticmethod
    def getURL():
        URL=config.get('common info','base_url')
        return URL

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
