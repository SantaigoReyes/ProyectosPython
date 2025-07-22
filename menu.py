import os 
import shutil
#carpeta = input("Ingresa la ruta de la carpeta a organizar: ").strip()

archivos = os.listdir(carpeta)
print(archivos)

tiposArchivos={
    "Imagenes": [".png",".jpg",".jpeg"],
    "Words" : [".doc",".docx"],
    "Excels" : [".xlsx"],
    "Documentos" : [".pdf", ".txt"],
    "Videos": [".mp4" , ".avi"],
    "Musica" : [".mp3", ".wav"],
    "Compresos" : [".zip" , ".rar"],
}
for archivo in archivos:
    nombre,ext=os.path.splitext(archivo)
    for categoria, extensiones in tiposArchivos.items():
        if ext.lower() in extensiones:
            nueva_ruta = os.path.join(carpeta,categoria)
            if not os.path.exists(nueva_ruta):
                os.mkdir(nueva_ruta)
            origen = os.path.join(carpeta,archivo)
            destino = os.path.join(nueva_ruta,archivo)
            shutil.move(origen, destino)
            print(f"Movido: {archivo}->{categoria}")
            break