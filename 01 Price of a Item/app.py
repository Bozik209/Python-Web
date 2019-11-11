import requests  # $ pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# pull out info from https use requests and BeautifulSoup libary
# get the price of the item 
request = requests.get("https://www.johnlewis.com/electricals/www.johnlewis.com/beats-solo-pro-wireless-bluetooth-on-ear-headphones-with-active-noise-cancelling-mic-remote/p4789503?intcmp=bc_20191030_beatssolopro_cp_ele_")
content = request.content 
soup = BeautifulSoup(content , "html.parser")
element = soup.find("p",{"class":"price price--large"})  # <p class="price price--large">£269.95 </p>

price_without_symbol = element.text.strip() # £269.95
clean_price = price_without_symbol[1:]      #  269.95
price=float(clean_price)

if price<500:
    print("You can buy the item \nThe price is {}".format(element.text.strip()))
else:
    print("Too expensive")


# another way to pull info
# in this case is the amount of view in youtube 
url = 'https://www.youtube.com/watch?v=auLmekEsaak'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
print("\n\n"+ soup.select_one('meta[itemprop="interactionCount"][content]')['content'] + " view")
