from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from PIL import Image
import os
import sys


comicurl = sys.argv[1]
savename = sys.argv[2]


if comicurl != None or savename != None:
	
	options = FirefoxOptions()
	options.add_argument("--headless")
	webdriver = webdriver.Firefox(options=options)
	webdriver.get(comicurl)

	image_urls = webdriver.execute_script('return lstImages')
	pagenumber = 0
	os.system("mkdir "+ savename )
	os.chdir(savename)
	for url in image_urls:
		os.system('wget ' + url + ' -O page' + str(pagenumber) + '.jpg' )
		pagenumber+=1

	image_list = []

	for img in os.listdir():
		image_list.append(Image.open(r''+img))

	converted_images = []

	for image in image_list:

		converted_images.append(image.convert('RGB'))

	converted_images[0].save(r''+os.getcwd()+savename+'.pdf',save_all=True, append_images=converted_images[1:None])
	print("sucessfully created comic pdf!, saved in : " + os.getcwd())	



else:
	print('Error! \n Usage: comicscraper.py "URL" "file_name_to_save_pdf_as" ')





