import json

def abrirJSON():
    dicFinal = []
    try:
        with open("./data/ListaGastos.json", "r") as openFIle:
            dicFinal = json.load(openFIle)
    except FileNotFoundError:
        dicFinal = []
    return dicFinal

def guardarJSON(dic):
    with open("./data/ListaGastos.json", "w") as outFile:
        json.dump(dic, outFile, indent=4)

def cargarLogs():
    dicFinal = []
    try:
        with open("./data/logs.json", 'r') as openFile:
            dicFinal = json.load(openFile)
    except FileNotFoundError:
        dicFinal = []
    return dicFinal

def logsJSON(dic):
    dicTemporal = cargarLogs()
    dicTemporal.append(dic)
    with open("./data/logs.json", 'w') as outFile:
        json.dump(dicTemporal, outFile, indent=4)