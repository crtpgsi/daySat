from selenium import webdriver
from utilities.readProperties import readConfig

class Test_0001_title:
    base_url=readConfig.getURL()


    def test_homepage(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        act_title=self.driver.title
        time
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False
