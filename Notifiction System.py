# This program gives us notifications about real time Covid-19 cases in Indian states.
# This program is based on the concept of Web Scraping


from plyer import notification #For Giving Notification
import requests # For getting HTML text
from bs4 import BeautifulSoup # For Web Scraping
import time # For setting time interval between each notifiction(30 minutes)

def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\User\\Downloads\\Coronavirus.ico", # Remember that icon can only have images in .ico format
        timeout = 15
    )
# In line 14 we gave that image in ico(icon) format which was converted from other format online for free
def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # notify_me("Alert", "Stay Safe from Coronavirus")
    myHTMLdata = getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHTMLdata, 'html.parser')
    mystr = ""
    for table in soup.find_all('tbody'):
        mystr += table.get_text()

    mystr = mystr[1:]
    itemlst = mystr.split("\n\n\n")
    state = input("Enter the name of the state you want details about")
    while True:
        for item in itemlst[0:33]:
            data = item.split("\n")
            td = -1
            if data[1] == state:
                td = 1
                break

            elif data[2] == state:
                td = 2
                break

        break


    if td == 1:
            title = "Coronavirus Cases"
            text = f"State: {data[1]}\nTotal Confirmed Cases: {data[2]}\nCured\Discharged: {data[3]}\nDeaths: {data[4]}"
            notify_me(title, text)
            time.sleep(1800)

    elif td == 2:
            title = "Coronavirus Cases"
            text = f"State: {data[2]}\nTotal Confirmed Cases: {data[3]}\nCured\Discharged: {data[4]}\nDeaths: {data[5]}"
            notify_me(title, text)
            time.sleep(1800)

    else:
        print("Please Check your spelling.First letter of name should be capital.\nFor example:- 'Uttar Pradesh'")








