from subprocess import call

def open_py_file():
    try:
        call(["python", "hiper_tv_video.py"])
    except:
        pass
    try:
        call(["python", "hiper_videojuegos.py"])
    except:
        pass
    try:
        call(["python", "hiper_informatica.py"])
    except:
        pass
    try:
        call(["python", "hiper_smartwatch.py"])
    except:
        pass
    try:
        call(["python", "cel_tablet.py"])
    except:
        pass
    try:
        call(["python", "hiper_audio.py"])
    except:
        pass
    
open_py_file()

def merge_csv():
    call(["python", "csv_joiner.py"])
    
merge_csv()