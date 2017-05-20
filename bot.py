import mechanize
from bs4 import BeautifulSoup
import cookielib


 #aca va tu mail entre comilla
USERNAME = 
# aca tu password tambien entre comillas
PASSWORD =  
URL = 'https://playfulbet.com/users/sign_in?locale=en'
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#cookiejar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)




br.open(URL)
br.select_form(nr = 0)

br.form['user[login]'] = USERNAME
br.form['user[password]'] = PASSWORD


br.submit()

print br.response().read()



