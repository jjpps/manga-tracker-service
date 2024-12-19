import pandas as pd
import os
import csv 

def criarExcel ():
    print('criando excel')
    path = './mangas.csv'
    check_file = os.path.exists(path)
    if(check_file == False):
        df = pd.DataFrame(columns=['ID','Nome','QtdCap','QtdCapLido'])
        df.to_csv(path)
        return
    else:
        return
def leExcel():
        path = './mangas.csv'   
        data = []     
        with open(path) as file_obj:       
            # Skips the heading 
            # Using next() method 
            heading = next(file_obj) 
            
            # Create reader object by passing the file  
            # object to reader method 
            reader_obj = csv.reader(file_obj) 
            
            # Iterate over each row in the csv file  
            # using reader object 
            for row in reader_obj: 
                 data.append(row)
            return data
                 


