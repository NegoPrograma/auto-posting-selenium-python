import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
Selenium-Webdriver needs a browser driver to run, do not forget to download it before running the script!

Instructions on usage:

first things first:

run pip install selenium-webdriver

download geckodriver(if using firefox) or the driver of your preference(this code defaults to firefox, if you
want to use another browser, do not forget to replace the driver build)

For posting into facebook groups you will need to log in first, replace the fields on the code with
your personal data after downloading this source. do not run this code before replacing the data!!

the data on email and password fields are fictional, just for instructional purpouses!

How to replace data:


{1} - Email

{2} - Password

{3} - List of Groups URL 

{4} - Post Content



"""


driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.facebook.com")
emailInputField = driver.find_element_by_xpath('.//*[@id="email"]')

""" {1} Your Email goes down below!"""

emailInputField.send_keys("replace this sentence with your email")


passwordInputField = driver.find_element_by_xpath('.//*[@id="pass"]')

"""{2} Your Password right here"""
passwordInputField.send_keys('replace this sentence with your password')





loginButton = driver.find_element_by_xpath('.//*[@id="loginbutton"]')
loginButton.click()
time.sleep(5)

"""
{3} - group url:

you must enter the groups URLs as such:

listOfGroups = ["https://linkone.com","https://linktwo.com","https://dontforgetthequotes.com"]


"""
listOfGroups = ["every","item of","this array","should be","a facebook group URL"]

for group in listOfGroups:
    driver.get(group)
    time.sleep(2)
    """
    Generally you can't simply choose the posting input field by default because they do element hidding,
    but due to their UX design, once you choose one way of media sending 
    e.g. clicking the "photo/videos" option and then click manually on the "write post"
    the posting input field is triggered and you can finally select it!

    That's the basis for the code below.

    """
    postMediaOptions = driver.find_elements_by_class_name('_1tm3')
    time.sleep(5)
    #selecting the "photo/videos"
    postMediaOptions[1].click()
    time.sleep(5)
    #selecting "write post" and trigger input field
    postMediaOptions[0].click()
    time.sleep(5)
    postInputField = driver.find_element_by_css_selector('div[contenteditable="true"]')
    time.sleep(5)
    
    
    """{4} Post your text content between the quotes on the line below. protip: you can use "\n" for line breaking. """
    postInputField.send_keys("""Hi! i'm your post text, edit meeeee please""")



    time.sleep(5)
    post_element = driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
    time.sleep(5)
    post_element.click()
    time.sleep(2)
    
    """
    ps: I learnt very introdutory content on selenium, all those "time.sleeps" probably already told you that.
    if i ever need to develop real professional test cases, i'll learn about selenium best practices 
    and develop better, readable code.

    ps2: this script is made only for educational purpouses, do not sell or spam. For properly posting, please
    refer yourself to Facebook's very own API.
    """