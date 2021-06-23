import pytest
from utilities.readProperties import readConfig
from selenium import webdriver
from pageObject.loginpage import Loginpage

class Test_0002_login:
    base_url= readConfig.getURL()
    username= readConfig.getUsername()
    password= readConfig.getPassword()

    def test_userlogin(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickButton()
        act_title = self.driver.title
        self.lp.clickLogout()
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\screenShot\\" +  "userlogintitle.png")
            assert False

