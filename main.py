from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from itertools import count
import selenium
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field,asdict
from typing import List

@dataclass
class Lawyer:
    first_name: str
    last_name: str
    emails: List[str] = field(default_factory=list)
    address: str = ""
    telephone: str = ""
    fax: str = ""
    web: str = ""
    professional_title: str = ""
    law_firm: str = ""
    law_firm_reg_num: str = ""
    lawyer_reg_num: str = ""
    areas_of_work: List[str] = field(default_factory=list)
    language: str = ""
    digitalSignature: str = ""

    def __str__(self):
        return (f"Lawyer({self.first_name} {self.last_name}, "
                f"Email: {', '.join(self.emails)}, "
                f"Address: {self.address}, "
                f"Telephone: {self.telephone}, "
                f"Fax: {self.fax}, "
                f"Web: {self.web}, "
                f"Professional Title: {self.professional_title}, "
                f"Law Firm: {self.law_firm}, "
                f"Law Firm Registration Number: {self.law_firm_reg_num}, "
                f"Lawyer Registration Number: {self.lawyer_reg_num}, "
                f"Areas of Work: {', '.join(self.areas_of_work)}, "
                f"Language: {self.language})"
                f"DigitalSignature: {self.digitalSignature}")

def BuildLawyer(driver):




    myfirst_name = ""
    mylast_name = ""
    myemails = []
    myaddress = ""
    mytelephone = ""
    myfax = ""
    myweb = ""
    myprofessional_title = ""
    myregistration_number = ""
    mylaw_firm = ""
    mylaw_firm_reg_num = ""
    mylawyer_reg_num = ""
    myareas_of_work = []
    mylanguage = ""
    mydigitalsignature = ""

    #lastname
    try:
        element = driver.find_element(By.CLASS_NAME,"lastname")
        mylast_name=element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    #email
    try:
        element = driver.find_element(By.CLASS_NAME, "email")
        myemails.append(element.text) #remove/string clean Email prefix

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    #web
    try:
        element = driver.find_element(By.XPATH, "//li[contains(text(), 'Web:')]/a")
        myweb=element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    #fax
    try:
        element = driver.find_element(By.XPATH, "//li[contains(text(), 'Fax:')]")
        myfax=element.text #remove fax from text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    #telephone
    try:
        element = driver.find_element(By.XPATH, "//li[contains(text(), 'Telephone:')]")
        mytelephone=element.text #remove telephone

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    #professional title
    try:
        element = driver.find_element(By.XPATH, "//tr[td[normalize-space(text())='Professional title:']]/td[2]")
        myprofessional_title = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    # lawyers registration number
    try:
        element = driver.find_element(By.XPATH, "//tr[td[normalize-space(text())='Lawyers‘ registration number:']]/td[2]")
        mylawyer_reg_num = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    # Law Firm
    try:
        element = driver.find_element(By.XPATH,"//tr[td[normalize-space(text())='Law firm:']]/td[2]")
        mylaw_firm = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    # Law Firm Reg Num
    try:
        element = driver.find_element(By.XPATH, "//tr[td[normalize-space(text())='Law firm registration number:']]/td[2]")
        mylaw_firm = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    # Areas of Work
    try:
        element = driver.find_element(By.XPATH, "//tr[td[normalize-space(text())='Law firm registration number:']]/td[2]")
        mylaw_firm = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    # Areas of Work
    try:
        element = driver.find_element(By.XPATH,"//tr[td[normalize-space(text())='Areas of work:']]/td[2]")
        myareas_of_work.append(element.text)

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    # Language
    try:
        element = driver.find_element(By.XPATH, "//tr[td[normalize-space(text())='Language:']]/td[2]")
        mylanguage = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    # Digital Signature

    try:
        element = driver.find_element(By.XPATH, "//li[contains(text(), 'Digital Signature:')]/a")
        mydigitalsignature = element.text

    except Exception as e:
        print(f"An error occurred: {e}")
        pass



    new_lawyer = Lawyer(
        first_name=myfirst_name,
        last_name=mylast_name,
        emails=myemails,
        address=myaddress,
        telephone=mytelephone,
        fax=myfax,
        web=myweb,
        professional_title=myprofessional_title,
        law_firm=mylaw_firm,
        law_firm_reg_num=mylaw_firm_reg_num,
        lawyer_reg_num=mylawyer_reg_num,
        areas_of_work=myareas_of_work,
        language=mylanguage,
        digitalSignature = mydigitalsignature
    )

    return new_lawyer

def IterateThroughDieAnwaltin(driver):

    lawyers: List[Lawyer] = []
    lastNames = driver.find_elements(By.CLASS_NAME,"lastname") #in theory we receive element that can be clicked?


#make list containing first, last, and emails per profile, 2d array, of variable length
    for i in range(0,len(lastNames)-1):
        lastNames[i].click()
        myWait(driver)
        new_lawyer = BuildLawyer(driver)


        lawyers.append(new_lawyer)
        driver.back()
        myWait(driver)
        lastNames = driver.find_elements(By.CLASS_NAME, "lastname")
        myWait(driver)
    return lawyers

def bruteForceAcceptCookies(driver):

    try:
        button = driver.find_element(By.XPATH,"//button[contains(@class, 'ccm--save-settings') and contains(@class, 'ccm--button-primary')]")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    if(not button.is_displayed()):
        return 0



    try:
        button = driver.find_element(By.CSS_SELECTOR, ".button.ccm--save-settings.ccm--button-primary.ccm--ctrl-init")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.CSS_SELECTOR, "button:contains('Alle Cookies akzeptieren')")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.CSS_SELECTOR, "button[data-full-consent='true']")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.XPATH, "//button[@data-full-consent='true']")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.XPATH, "//button[text()='Alle Cookies akzeptieren']")
        button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0


    try:
        button = driver.find_element(By.XPATH, "//button[@data-full-consent='true' and contains(text(), 'Alle Cookies')]")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Alle Cookies')]")
        button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Alle Cookies')]")
        button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0

    try:
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Alle Cookies')]")
        button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        pass


    if(not button.is_displayed()):
        return 0


def myWait(driver,impWaitTime=0):

    driver.implicitly_wait(impWaitTime)
    driver.implicitly_wait(5)

    WebDriverWait(driver, 10).until(
        lambda d: driver.execute_script("return document.readyState") == "complete"
    )









# List of supposed codes, will double check later for hallucinations.
# Informational responses (100–199)
# 100 Continue: The server has received the request headers and the client can proceed with sending the request body.
# 101 Switching Protocols: The requester has asked the server to switch protocols and the server has agreed.
# 102 Processing: The server is processing the request but has not completed it yet (WebDAV).

# Success responses (200–299)
# 200 OK: The request was successful.
# 201 Created: The request was successful and a new resource was created.
# 202 Accepted: The request has been received but not yet acted upon.
# 203 Non-Authoritative Information: The request was successful but the response is from a third-party.
# 204 No Content: The request was successful, but there is no content to send in the response.
# 205 Reset Content: The request was successful, and the client should reset the view.
# 206 Partial Content: The server is delivering only part of the resource due to a range header sent by the client.

# Redirection messages (300–399)
# 300 Multiple Choices: The request has more than one possible response.
# 301 Moved Permanently: The URL of the requested resource has been changed permanently.
# 302 Found: The resource resides temporarily under a different URI.
# 303 See Other: The response can be found under a different URI and should be retrieved using a GET request.
# 304 Not Modified: The resource has not been modified since the last request.
# 307 Temporary Redirect: The resource resides temporarily under a different URI but should use the original method.
# 308 Permanent Redirect: The resource is permanently located at another URI and should use the original method.

# Client error responses (400–499)
# 400 Bad Request: The server could not understand the request due to invalid syntax.
# 401 Unauthorized: The client must authenticate itself to get the requested response.
# 402 Payment Required: Reserved for future use (commonly associated with payment-based APIs).
# 403 Forbidden: The client does not have access rights to the content.
# 404 Not Found: The server cannot find the requested resource.
# 405 Method Not Allowed: The request method is not supported for the requested resource.
# 406 Not Acceptable: The server cannot produce a response matching the client's Accept headers.
# 407 Proxy Authentication Required: The client must authenticate with the proxy to access the requested resource.
# 408 Request Timeout: The server did not receive a complete request within the specified time.
# 409 Conflict: The request conflicts with the current state of the server.
# 410 Gone: The resource is no longer available and will not be available again.
# 411 Length Required: The server requires the Content-Length header in the request.
# 412 Precondition Failed: The client has indicated preconditions that the server does not meet.
# 413 Payload Too Large: The request entity is larger than the server is willing to process.
# 414 URI Too Long: The request URI is longer than the server can process.
# 415 Unsupported Media Type: The server does not support the media type of the request.
# 416 Range Not Satisfiable: The client requested a range that is not available for the resource.
# 417 Expectation Failed: The server cannot meet the requirements of the Expect header.
# 418 I'm a Teapot: A playful acknowledgment of HTTP/1.0 spec RFC 2324.
# 422 Unprocessable Entity: The server understands the content but cannot process it (WebDAV).
# 429 Too Many Requests: The user has sent too many requests in a given amount of time.

# Server error responses (500–599)
# 500 Internal Server Error: The server encountered an unexpected condition.
# 501 Not Implemented: The server does not support the functionality required to fulfill the request.
# 502 Bad Gateway: The server received an invalid response from the upstream server.
# 503 Service Unavailable: The server is not ready to handle the request.
# 504 Gateway Timeout: The server did not get a response in time from an upstream server.
# 505 HTTP Version Not Supported: The server does not support the HTTP version used in the request.
# 507 Insufficient Storage: The server cannot store the representation needed to complete the request (WebDAV).
# 511 Network Authentication Required: The client needs to authenticate to gain network access.

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your co+de.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# based on the tutorial most websites should reject a webscraper without a proper header, this ran without a proper header lmao, good job guys
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
headers=headers
url = 'https://www.oerak.at/en/support-and-services/services/find-a-lawyer/?tx_rafinden_simplesearch%5Blimit%5D=25&tx_rafinden_simplesearch%5Baction%5D=fullList&tx_rafinden_simplesearch%5Bcontroller%5D=LawyerSearch&cHash=a23a49c3c51b91abedd4e66a07a2bf1a'
baseSiteUrl = 'https://www.oerak.at'
print("loading page")

#main_page
#main_page = requests.get(url)

driver = webdriver.Chrome()


driver.get(url)





# "button ccm--save-settings ccm--button-primary ccm--ctrl-init"
#wait = WebDriverWait(driver, 10)

#WebDriverWait(driver, 10).until(
#    lambda d: driver.execute_script("return document.readyState") == "complete"
#)

myWait(driver)

bruteForceAcceptCookies(driver)

while(True):

    myWait(driver)

    myLawyers = IterateThroughDieAnwaltin(driver)

    #append to csv in current dur
    with open("output.txt", "w") as file:
        for item in myLawyers:
            file.write(str(asdict(item)) + "\n")

    #click next? wait, do it again
    try:
        button = driver.find_element(By.XPATH,"//a[contains(@class, 'button1') and contains(@class, 'arrowRight') and contains(@class, 'grey') and contains(@class, 'rounded') and text()[normalize-space()='Next']]")
        button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass










