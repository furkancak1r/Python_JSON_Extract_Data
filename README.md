# Python_JSON_Extract_Data
 
This application allows you to filter Excel files converted to JSON format according to certain criteria.

## How to use

- Run `app.py` file to run the application.
- Enter the path of the JSON file you want to convert. The JSON file must contain data named `parts`.
- Filtering criteria are: `"-"`, `"x"`, `"="`, `"TL"`, `"USD"`, `"EUR"`.
- Saves filtered JSON file.
- Use an online JSON to Excel converter to convert the JSON file back to Excel format.

## Notes

- When converting the Excel file to JSON format, the `/` character may be converted to `\/` in some places. Therefore, before running `app.py`, replace all `\/` characters in the JSON file with `/` character.
- This application is written in Python 3.12. The libraries required to run it are: `json`, `re`.

# Python_JSON_Extract_Data
 
Bu uygulama, Excel dosyalarının JSON formatına dönüştürmüş halini belirli kriterlere göre filtrelemenize olanak tanır.

## Nasıl kullanılır

- Uygulamayı çalıştırmak için `app.py` dosyasını çalıştırın.
- Dönüştürmek istediğiniz JSON dosyasının path'ini girin. JSON dosyası `parts` adında bir veri içermelidir.
- Filtreleme kriterleri şunlardır: `"-"`, `"x"`, `"="`, `"TL"`, `"USD"`, `"EUR"`.
- Filtrelenmiş JSON dosyasını kaydeder.
- JSON dosyasını Excel formatına geri dönüştürmek için bir online JSON to Excel converter kullanın.

## Notlar

- Excel dosyasını JSON formatına dönüştürürken, bazı yerlerde `/` karakteri `\/` şeklinde dönüştürülebilir. Bu nedenle, `app.py` dosyasını çalıştırmadan önce, JSON dosyasındaki tüm `\/` karakterlerini `/` karakteri ile değiştirin.
- Bu uygulama Python 3.12 sürümü ile yazılmıştır. Çalıştırmak için gerekli kütüphaneler şunlardır: `json`, `re`.
