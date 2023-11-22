from configparser import ConfigParser

config = ConfigParser()

config["default"] = {
    "branch": "Santiago",
    "branch_id": 12
}

config["cordoba_1"] = {
    "branch": "Cordoba Lugones",
    "branch_id": 1
}

config["cordoba_2"] = {
    "branch": "Cordoba Rivera",
    "branch_id": 2
}

config["cordoba_3"] = {
    "branch": "Cordoba Jacinto Rios",
    "branch_id": 3
}

config["cordoba_4"] = {
    "branch": "Cordoba Ruta 9",
    "branch_id": 4
}

config["mendoza_1"] = {
    "branch": "Godoy Cruz",
    "branch_id": 6
}

config["misiones"] = {
    "branch": "Posadas",
    "branch_id": 7
}

config["tucuman_1"] = {
    "branch": "Tucuman 1",
    "branch_id": 8
}

config["tucuman_2"] = {
    "branch": "Tucuman 2",
    "branch_id": 9
}

config["chaco"] = {
    "branch": "Chaco",
    "branch_id": 10
}

config["rosario"] = {
    "branch": "Rosario",
    "branch_id": 11
}

config["san_juan"] = {
    "branch": "San Juan",
    "branch_id": 13
}

config["salta"] = {
    "branch": "Salta",
    "branch_id": 14
}

config["rafaela"] = {
    "branch": "Rafaela",
    "branch_id": 15
}

config["mendoza_dig"] = {
    "branch": "Mendoza Digital",
    "branch_id": 16
}

with open("branch_config.ini", "w") as file:
    config.write(file)