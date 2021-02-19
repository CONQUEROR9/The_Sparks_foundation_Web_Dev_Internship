import unittest

from time import sleep

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

from selenium.webdriver import ActionChains

class The_sparks_foundation_task_6(unittest.TestCase):
   
    @classmethod

    def setUpClass(cls):
       
        cls.driver=webdriver.Firefox()

        cls.driver.maximize_window()

    def test_mainpage(self):
        
        driver=self.driver
       
        #Entering the url
        
        driver.get("https://www.thesparksfoundationsingapore.org")
       
        #Check whether the title is correct or not
        
        self.assertIn("The Sparks Foundation",driver.title)
       
        #Check whether the logo is displayed or not
        
        logo=driver.find_element_by_class_name('col-md-6.navbar-brand')
        
        logo.is_displayed()

        #Check whether the navigation bar is displayed or not
        
        nav=driver.find_element_by_class_name('nav.navbar-nav')
        
        nav.is_displayed()

        #clicking the nav bar
        
        nav.click()
        
        sleep(2)
       
        #Checking whether about us is accessible or not
        
        check_about_us=driver.find_element_by_class_name('dropdown-toggle.menu__link')
       
        #Clicking the about us in the navigation bar
        
        check_about_us.click()


    def test_join_us(self):
        
        driver=self.driver
        
        driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")
        
        sleep(2)

        #Assigning the values to variables to input the data in the form
        
        Name=driver.find_element_by_name("Name")

        Email=driver.find_element_by_name("Email")
        
        form=driver.find_element_by_class_name("form-control")
        
        #Scrolling down to the form
        
        scroll=driver.find_element_by_class_name('para-w3-agile.white-w3ls')
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        
        sleep(1)
        
        #Checking whether the form takes values or not in the join us page 
        
        Name.send_keys("Lakshmi narayana Naidu")
        
        sleep(1)
        
        Email.send_keys("lakshminarayananaidu09@gmail.com")
        
        sleep(1)
        
        drop=Select(form)
        
        drop.select_by_visible_text("Intern")
        
        sleep(2)
        
        driver.get("https://www.thesparksfoundationsingapore.org/join-us/internship-positions")

        #Scrolling down the page
        
        scroll=driver.find_element_by_class_name("media-body")
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        
        sleep(3)


    def test_programs(self):
        
        driver=self.driver
        
        driver.get("https://www.thesparksfoundationsingapore.org/programs/student-scholarship-program/")
        
        sleep(2)

        #scrolling down the page
        
        scroll=driver.find_element_by_class_name("media")
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll)

        driver.get("https://www.thesparksfoundationsingapore.org/programs/student-mentorship-program/")
        
        sleep(2)

        #scrolling down the page
        
        scroll1=driver.find_element_by_class_name("media-body")
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll1)
        
        sleep(2)


    def test_about_us(self):
        
        driver=self.driver
        
        driver.get("https://www.thesparksfoundationsingapore.org/about/vision-mission-and-values/")
        
        sleep(2)

        #Scrolling down the page
        
        scroll=driver.find_element_by_class_name("footer-row.w3layouts-agile")
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        
        sleep(2)

        #Entering another page using the buttons provided
        
        driver.get("https://www.thesparksfoundationsingapore.org/about/advisors-and-patrons")
        
        sleep(2)

        #Scrolling down the page
        
        scroll1=driver.find_element_by_class_name('copyright-wthree')
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll1)
        
        sleep(3)

        #Checking whether the 'Go to the top' button working or not
        
        top_scroll=driver.find_element_by_id("toTopHover")
        
        top_scroll.click()
        
        sleep(3)


    def test_contact_us(self):
        
        driver=self.driver
        
        driver.get("https://www.thesparksfoundationsingapore.org/contact-us/")
        
        sleep(2)

        #Scrolling down the page
        
        scroll=driver.find_element_by_class_name("map-agileits")
        
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        
        sleep(3)

        #Checking whether we can go to the main page by clicking on the logo
        
        logo=driver.find_element_by_class_name("col-md-6.navbar-brand")
        
        logo.click()
        
        sleep(3)


    @classmethod

    def tearDownClass(cls):
        
        #Close the browser
        
        cls.driver.close()


if __name__=="__main__":

    unittest.main()

