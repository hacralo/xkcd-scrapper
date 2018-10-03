import os
import requests
from bs4 import BeautifulSoup
import time


# make a directory comics to store images
if not os.path.exists('comics'):
	os.makedirs('comics')
os.chdir('comics')

counter = 1
res =requests.get("https://xkcd.com/"+str(counter))

while res.status_code ==200:
	time.sleep(5) 
	soup = BeautifulSoup(res.text,'html.parser')
	img_tag = soup.findAll('img')[1]
	try:
		url = img_tag['src']
		f_url = "https:" + url
		img_name = img_tag['alt']
		response = requests.get(f_url)
		if response.status_code == 200:
			with open(img_name + '.jpg', 'wb') as f:
				f.write(requests.get(f_url).content)
				f.close()
				print("downloaded the comic: " + img_name)
	except:
		pass
	counter += 1
	res =requests.get("https://xkcd.com/"+str(counter))