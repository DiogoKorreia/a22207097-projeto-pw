import zipfile

zip_path = '/home/a22207097/project/meteo/static/meteo/icons_ipma_weather.zip'

extract_path = '/home/a22207097/project/meteo/static/meteo/'


with zipfile.ZipFile(zip_path, 'r') as zip_ref:

    zip_ref.extractall(extract_path)

print("Sucesso!")
