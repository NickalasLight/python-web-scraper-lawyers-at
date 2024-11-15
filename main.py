from itertools import count

import requests
from bs4 import BeautifulSoup

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
main_page = requests.get(url)
print(main_page.status_code)
soup = BeautifulSoup(main_page.text, 'html.parser')
#print(soup)
#firstName_elements = soup.find_all(class_='firstname')
lastName_elements = soup.find_all(class_='lastname')
email_elements = []
urls = [span.find_parent('a')['href'] for span in lastName_elements]
urls = urls[:5] #remove, for testing only
#lastname_links = soup.find_all('a', class_=['lastname'])


#print(urls)
#so we get all lawyer names, indexed by last name alphabetically. 50 results at a time.
indexer = count(start=1,step=1)
for item in urls:
    print(f"Item {next(indexer)}: {item}")
    #go in
    mini_page = requests.get('https://www.oerak.at'+item)
    print('Url for minipage is: ' + mini_page.url)

    mini_soup = BeautifulSoup(mini_page.text, 'html.parser')
    #in case of multiple emails
    #emails = mini_soup.find_all(class_='email')

    email_list_items = mini_soup.find_all(class_='email')

    # Extract URLs from the <a> tags inside these <li> elements
    #emails = [li.find('a')['href'] for li in email_list_items if li.find('a')]




    for item in email_list_items:
        email_elements.append(item.text)
#gottem so we go back to main
    main_page = requests.get(url)











indexer = count(start=1,step=1)
if (len(lastName_elements) == len(email_elements)):
    for email,lastName in zip(email_elements,lastName_elements):
        index = next(indexer)
        print(f"Index: {index}, Primary Item: {lastName}, Email: {email}")
else:
    for emai in email_elements:
        print(f"Email {next(indexer)}: {item}")
"""
such is what the links to lawyers on the page look like. 
<a href="/en/support-and-services/services/find-a-lawyer/?tx_rafinden_simplesearch%5Blid%5D=1853&amp;tx_rafinden_simplesearch%5Baction%5D=show&amp;tx_rafinden_simplesearch%5Bcontroller%5D=LawyerSearch&amp;cHash=c03db335e19db3d6dfec345926213cd6">
<span class="lastname">ABEL</span>
<br>
<span class="firstname">Norbert</span>
<span class="title">Mag.</span>
</a>

"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
