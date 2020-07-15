from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.coronatracker.com/").text
soup = BeautifulSoup(source, "lxml")

numbers = soup.find("div", class_ = "h-16 pt-2 flex flex-auto items-center justify-center bg-red-100 text-base sm:text-lg lg:text-3xl font-bold font-sans")
print(numbers)


#<div class="h-16 pt-2 flex flex-auto items-center justify-center bg-red-100 text-base sm:text-lg lg:text-3xl font-bold font-sans"><span class="mx-2">
         # 9,393,450
        #</span></div>
