from zipfile import ZipFile 

def file():

    try:
        with ZipFile('temp.apkg', 'r') as apkg_file:
            file = apkg_file.read('collection.anki2')
            with open('daco.csv', 'wb') as f:
                f.write(file)

    except Exception as e:
        print(e)


print(file())