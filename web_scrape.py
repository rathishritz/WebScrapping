
import requests
from lxml import html
import csv


main_url='https://www.infoplease.com'
page_content=requests.get('https://www.infoplease.com/homework-help/history/collected-state-union-addresses-us-presidents')
cont=page_content.content
tree=html.fromstring(cont)
home_link=tree.xpath('//span[@class="article"]/a/text()')
href=tree.xpath('//span[@class="article"]/a/@href')
Pres=[]
DateOfSpeech=[]
Link=[]
FilePath=[]
Speech=[]
name=None
year=None

#This is to split name and speech year separately and store it in list
for l in home_link:

    name=l.split(" (",1)
    Pres.append(name[0])
    year=name[1]
    year=year[:-1]
    DateOfSpeech.append(year)
    
print(len(href))
print(len(Pres))
print(len(DateOfSpeech))

#Below code is to fetch the string from href tag and store text in a list
flag=1
for v in href:
    speech_url=main_url+v
    flag=flag+1
    content_req=requests.get(speech_url).content
    cont_tree=html.fromstring(content_req)
    cont_path=cont_tree.xpath('//div[@class="article"]/p/text()')
    flag+=1
    f_speech=""
    for val in cont_path:
        f_speech=f_speech+val
        

    Speech.append(f_speech)
txt_path="C:\\Users\\rathi\\OneDrive\\Documents\\Master's\\CIS 612 Big data\\Lab1\\InfoUnionAddress_"

path_count=1
#This is to create text files and write the content into the file 
for jk in Speech:
    tex_path=txt_path+str(path_count)+".txt"
    FilePath.append(tex_path)
    text_file=open(tex_path,"w")
    text_file.write(jk)
    text_file.close()
    path_count+=1
    

#Below code is to write the data into the csv file
csvFile=open('big_data.csv','w',newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(['Pres','DateOfSpeech','Link','Text of Address','Speech'])
    for pres_name,year,speech_link,loc_path,pres_speech in zip(Pres,DateOfSpeech,href,FilePath,Speech):
        speech_link=main_url+speech_link
        writer.writerow([pres_name,year,speech_link,loc_path,pres_speech])
        
finally:
    csvFile.close()


