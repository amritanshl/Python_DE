import os
import csv
import datetime
import schedule
import time

# fileExist = os.path.exists("Input/")
# if(fileExist):
#     with open("Input/products.csv", mode="r") as file:
#         csvdict = csv.DictReader(file)
#         for s in csvdict:
#            print(s)
# filecontent = pandas.read_csv('https://raw.githubusercontent.com/MicrosoftLearning/dp-203-azure-data-engineer/master/Allfiles/labs/01/adventureworks/products.csv')
# print(filecontent)

companies = ['EY', 'Delloite', 'KPMG', 'Microsoft','Accenture']

def job():
    mode = 0o666
    for x in companies:
        year_f = str(datetime.datetime.now().year)
        month_f= str(datetime.datetime.now().month)
        day_f= str(datetime.datetime.now().day)
        hour_f= str(datetime.datetime.now().hour)
        min_f= str(datetime.datetime.now().minute)
        sec_f= str(datetime.datetime.now().second)

        file_name = x+"_"+year_f +month_f+day_f+hour_f+min_f+sec_f+".csv"   
        #print(file_name) 
        #print(os.getcwd())
        OutputPath = os.path.join(os.getcwd(),"Output")
        if(not os.path.exists(os.path.join(os.getcwd(),"Output"))):
            
            os.mkdir(OutputPath)
        year_path = os.path.join(OutputPath,year_f)
        if (os.path.exists(year_path)):
            pass
        else:
            os.mkdir(year_path)
        month_path = os.path.join(year_path,month_f)
        if (os.path.exists(os.path.join(year_path,month_f))):
            pass
        else:
            
            os.mkdir(month_path)

        day_path = os.path.join(month_path,day_f)
        if (os.path.exists(os.path.join(month_path,day_f))):
            pass
        else:
            
            os.mkdir(day_path)
        
        hourt_path = os.path.join(month_path,hour_f)
        if (os.path.exists(hourt_path)):
            pass
        else:
            
            os.mkdir(hourt_path)
        
        min_path = os.path.join(hourt_path,min_f)
        if (os.path.exists(min_path)):
            pass
        else:
            
            os.mkdir(min_path)

        sec_path = os.path.join(min_path,sec_f)
        if (os.path.exists(sec_path)):
            pass
        else:
            
            os.mkdir(sec_path)
   

schedule.every().second.do(job)

while 1:
    schedule.run_pending()
    time.sleep(2)

