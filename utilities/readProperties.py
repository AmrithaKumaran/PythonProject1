import configparser # configparser is required to read the data from the configuration file, which is ini file
import os #os is required to configure the path
#So whenever you want to read the data from the ini files, we have to use configparser, class or package which you need to import.
# This property file is the connection between ini file and test cases ini file->property->testcase

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configuration\\config.ini')

class ReadConfig():
    # So when you create any method with static,
    # that method we can directly call by using a class.no need to create an object.
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password


#Testing above methods - optional Code
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())

