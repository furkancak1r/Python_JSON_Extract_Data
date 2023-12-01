import json

# JSON dosyasını belirtilen kodlamayla yükle
with open('C:\\Users\\furkan.cakir\\Desktop\\FurkanPRS\\Kodlar\\SSH\\Python_JSON_Extract_Data\\jsonlar\\oldexcel.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Yeni veri listesini oluştur
newData = []

# Her bir servis öğesini işle
for service in data:
    # "problems" alanından sorun bilgilerini çıkar
    problems = service.get('problems', None)

    # Eğer "problems" alanı boş değilse, ":" karakterinden önceki kısmı al ve newData'ya ekle
    if problems:
        problem_info = problems.split(":", 1)[0].strip()
        newData.append({"problem_info": problem_info})
    else:
        # Eğer "problems" alanı boşsa, newData'ya null ekle
        newData.append({"problem_info": None})

# Yeni veriyi JSON formatlı bir dizeye çevir
json_dizi = json.dumps(newData, indent=4, ensure_ascii=False)

# JSON dizesini yeni bir dosyaya yaz
with open("C:\\Users\\furkan.cakir\\Desktop\\FurkanPRS\\Kodlar\\SSH\\Python_JSON_Extract_Data\\jsonlar\\newData.json", "w", encoding='utf-8-sig') as dosya:
    dosya.write(json_dizi)
