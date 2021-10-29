from flask import Flask
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import yaml

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'




@app.route('/',)
def index():
    script1()
    return "hello"



def script1():
    
    #confihurations need to read from configurations.yaml file
    with open("configuration.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    
    
    #last index till GF1 was read    
    gf1LastReadIndex=cfg["gf1LastReadIndex"]
    
   
    #reading spreadsheet
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(creds)
    
    
    
    #reading data from Google form 1 
    gf1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("GF1")
    gf1Data = gf1Spreadsheet.get_all_values()
    headings= gf1Data[0]
    gf1RemainingData=gf1Data[gf1LastReadIndex:]
    print(gf1RemainingData)
    
     
    # reading data from stage 1 
    st1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("GF1-V2")
    st1Data = st1Spreadsheet.get_all_values()
    st1DataCurrentLength=len(st1Data)
    print(st1Data)
  

    #moving data from gf1 to st1 ot st2
    for entry in gf1RemainingData:

        Timestamp=entry[0]
        Name= entry[1]
        YourWhatsAppnumber=entry[2]
        Email=entry[3]
        country=entry[4]
        #read missing onces






        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 1, Timestamp) #timestamp
        print(entry)
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 2, Name) #Name 
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 3,  YourWhatsAppnumber) #whattsapp number
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 4, Email) #email
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 5, country) #country

        st1DataCurrentLength=st1DataCurrentLength+1
            

       
        
        gf1LastReadIndex=gf1LastReadIndex+1

        
        


        
    #updating last read in configuration file
                
    cfg["gf1LastReadIndex"]= gf1LastReadIndex
    


    with open('helo.yaml', 'w') as fp:
        yaml.dump(cfg, fp)

    return    
@app.route('/gf2',)
def index1():
    script2()
    return "hello"



def script2():
    
    #confihurations need to read from configurations.yaml file
    with open("configuration.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    
    
    #last index till GF1 was read    
    gf1LastReadIndex=cfg["gf1LastReadIndex"]
    
   
    #reading spreadsheet
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(creds)
    
    
    
    #reading data from Google form 1 
    gf1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("GF2")
    gf1Data = gf1Spreadsheet.get_all_values()
    headings= gf1Data[0]
    gf1RemainingData=gf1Data[gf1LastReadIndex:]
    print(gf1RemainingData)
    
     
    # reading data from stage 1 
    st1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("GF2-V2")
    st1Data = st1Spreadsheet.get_all_values()
    st1DataCurrentLength=len(st1Data)
    print(st1Data)
  

    #moving data from gf1 to st1 ot st2
    for entry in gf1RemainingData:

        Timestamp=entry[0]
        Name= entry[1]
        YourWhatsAppnumber=entry[2]
        Email=entry[3]   
        issue=entry[19]
        preferencetime=entry[21]     #read missing onces






        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 1, Timestamp) #timestamp
        print(entry)
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 2, Name) #Name 
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 3,  YourWhatsAppnumber) #whattsapp number
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 4, Email)
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 5, issue)
        st1Spreadsheet.update_cell(st1DataCurrentLength+1, 6, preferencetime) #email

        st1DataCurrentLength=st1DataCurrentLength+1
            

       
        
        gf1LastReadIndex=gf1LastReadIndex+1

        
        


        
    #updating last read in configuration file
                
    cfg["gf1LastReadIndex"]= gf1LastReadIndex


if __name__ == '__main__':
    app.run(debug=False)