from googlesearch import search
import requests
from bs4 import BeautifulSoup

while True:
    query = input("What would you like to search: ")

    if query == "^":
        break

    links = search(query, num_results=10)

    for link in links:
        linkRequest = requests.get(link)
        if linkRequest.status_code == 200:
            doc = BeautifulSoup(linkRequest.text, "html.parser")

            paragraphs = doc.find_all("p")

            for paragraph in paragraphs:
                print(paragraph.get_text())

            goAgain = input("Good enough? (Y to stop): ")

            if goAgain == 'Y':
                break
print("program ended")
