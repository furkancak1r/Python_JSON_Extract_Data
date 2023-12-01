import json
import re
# Specify the encoding when loading the JSON data
# Specify the encoding when loading the JSON data
with open('oldexcel.json', encoding='utf-8-sig') as f:
    data = json.load(f)


# Process each service item
newData=[]
for service in data:
    # Extract the parts information from the "parts" field
    parts_raw=[]

    parts_raw = service.get ('parts', None)
    if parts_raw:
        parts_list = parts_raw.split('; ')
        parts_list = [part_raw for part_raw in parts_list if part_raw]
    else :
       
    
        part_processed = {
                    "serviceNo":service.get ('serviceNo', None),
                    "code": None,
                    "explanation":  None,
                    "quantity":None,
                    "price": None,
                    "currency": None,
                }
        newData.append(part_processed)
        continue


    parts_processed = []
    for part_raw in parts_list:
        if len(part_raw) >2:
            resultFirstData = part_raw.split('- ')[0]
            part_raw = '- '.join(part_raw.split('- ')[1:])
         
            if part_raw.endswith("EUR") or part_raw.endswith("EUR "): 
                separators = " x | = | EUR" 
                resultAll = re.split(separators, part_raw) 
                resultAll[-1] = "EUR" 
            elif part_raw.endswith("USD") or part_raw.endswith("USD "):
                separators = " x | = | USD" 
                resultAll = re.split(separators, part_raw) 
                resultAll[-1] = "USD" 
            elif part_raw.endswith("TL") or part_raw.endswith("TL "):
                separators = " x | = | TL" 
                resultAll = re.split(separators, part_raw) 
                resultAll[-1] = "TL" 
            else:
                print("hata var:",parts_list)
                break
                    
            part_processed = {
                    "serviceNo":service.get ('serviceNo', None),
                    "code": resultFirstData,
                    "explanation":  resultAll[0].strip(),
                    "quantity":resultAll[1].strip(),
                    "price": resultAll[2].strip(),
                    "currency": resultAll[3].strip(),
                }


            newData.append(part_processed)
    
       
# newData'yı JSON formatında bir dizeye dönüştürme
json_dizi = json.dumps (newData, indent=4, ensure_ascii=False)

# JSON dizisini yeni bir dosyaya yazma
with open ("newData.json", "w",encoding='utf-8-sig') as dosya:
    dosya.write (json_dizi)
