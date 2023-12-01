from subprocess import call

def open_py_file():
    try:
        call(["python", "tv_video.py"])
    except:
        pass
    try:
        call(["python", "videojuegos.py"])
    except:
        pass
    try:
        call(["python", "informatica.py"])
    except:
        pass
    try:
        call(["python", "smartwatch.py"])
    except:
        pass
    try:
        call(["python", "cel_tablet.py"])
    except:
        pass
    try:
        call(["python", "audio.py"])
    except:
        pass
    
open_py_file()

def merge_csv():
    call(["python", "csv/csv_joiner.py"])
    
merge_csv()