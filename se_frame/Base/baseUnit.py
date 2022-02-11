#conding:uft-8
import  unittest
from Common.function import configUrl
from selenium import  webdriver
#抽离单元测试中setUp与tearDown
class unitBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = 'E:/chromedriver.exe'
        cls.driver = webdriver.Chrome(path)
        cls.driver.get(configUrl())
        cls.driver.maximize_window()

    def tearDownClass(cls):
        cls.driver.quit()
