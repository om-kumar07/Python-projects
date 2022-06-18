import pandas as pd
import xlrd
import smtplib      #simple mail transfer protocol is imported 
import datetime
sendermail="revealhackerr@gmail.com"
recevermail="kattyshreyansh@gmail.com"
id="@time_pass"       
today=datetime.datetime.now().strftime("%m-%d")      #fetching todays date and month
df=pd.read_excel('content.xlsx')     # reading excel file through pandas and storing in variable df
def sendmail(msg,name):              #method for sending mail
    s=smtplib.SMTP('smtp.gmail.com',587)     #creating sesson on gmail.com with port no 587
    s.starttls()                           #starting tls
    s.login(sendermail,id)                #login with username and password
    msg=msg+","+name
    s.sendmail(sendermail,recevermail,msg)    #sending mail having message msg
    s.quit()                                 #closing the session
 
    print(f" mail sent to  having related with {msg} , {name}") #confermation message after sending a mail
if __name__=="__main__":  
    for index,item in df.iterrows():        #df.iterrows() fetch content in item and index no in index
        bday=item['Date'].strftime("%m-%d")    #fetching the date in excel file and storing in bday , only storing month and date
        if(bday==today):                       #if todays date is same as birthday date assigned in excel file
            sendmail(item['Message'],item['Name']) # if todays date is same as date of bday the call method sendmail  
        else:
            print(f"mail not send for {item['Name']}")       
    
