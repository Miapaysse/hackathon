import google.generativeai as genai

def listar_modelos():
    api_key = "AIzaSyB1EBXeDpuhSZ5a4oX1THmVW3aJmNdZGAM"
    genai.configure(api_key=api_key)
    modelos = genai.list_models()
    print("Modelos disponibles:")
    for m in modelos:
        print(m)

