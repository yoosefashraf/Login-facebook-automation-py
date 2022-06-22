from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Disable Notifications Facebook 
option = Options()
option.add_argument('--disable-notifications')
web = webdriver.Chrome("path chrome driver", chrome_options=option) # Web Driver

# [1]- For => Change Size And Browser Position 
# [2]- For => Go To Url Facebook 
def notifications():
   web.set_window_position(50, 50) # Change Position Browser
   web.set_window_size(1400, 1000) # Change size Browser
   web.get("https://www.facebook.com/login") # Url Page Facebook Login


# [1]- For => Call Notifications Function  
# [2]- For => username_box => Go To Element input username and send data from function 
# [3]- For => pass box => Go To Element input pass and send data from function 
# [4]- For =>  click on Login Button

def login_facebook(user,passW):
  notifications() # Function
  username_box = web.find_element_by_id('email').send_keys(user) # Input username field
  pass_box = web.find_element_by_id('pass').send_keys(passW) # Input username field
  login_box = web.find_element_by_xpath('//*[@id="loginbutton"]').click() # Login Button


show_login = login_facebook("username", "password") # Enter Your Data To  Login
