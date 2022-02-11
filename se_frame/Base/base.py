from Common.Log import framelog
#对base代码进行优化、增加
class base():
    def __init__(self,driver):
        self.driver = driver
        self.log =framelog().log()
     #id
    def by_id(self,element):
        try :
            self.log.info("开始对元素"+element+"操作")
            return  self.driver.find_element_by_id(element)
        except:
            self.log.error("找不到元素："+element)
            return  None
    #name
    def by_name(self,element):
        return self.driver.find_element_by_name(element)
    #xpath
    def by_xpath(self,element):
        return  self.driver.find_element_by_xpath(element)
    #css
    def by_css(self,element):
        return  self.driver.find_element_by_css_selector(element)
    #url
    def dr_url(self):
        return self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()

    # 前进
    def forword(self):
        self.driver.forward()
    #退出

    def quit(self):
        self.driver.quit()

