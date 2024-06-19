import requests
from bs4 import BeautifulSoup
import webbrowser

choice = int(input('Would you like to read random article or a specific article?(1/2) '))
while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    if choice==1:
        title = soup.find(class_="firstHeading").text
    elif choice==2:
        title = input('Enter  a topic ')

    print(f"{title} \nWould you like to read the article? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        print("\n")
        continue
    else:
        print("Wrong choice!")
        break
