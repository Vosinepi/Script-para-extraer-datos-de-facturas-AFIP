import fitz

import cv2

import pandas as pd


import pdfplumber
import os
import re
import datetime

# variables
fecha = datetime.datetime.now()


# Carpeta donde se encuentran los pdfs
carpeta_raiz = ""
carpeta_imagenes = f"/{fecha.strftime('%Y-%m-%d')}_facturas_jpg"
carpeta_excel = f"/{fecha.strftime('%Y-%m-%d')}_Excel_con_datos"

facturas_dict = {}


def read_qr_code(filename, carpeta_imagenes):
    """Read an image and read the QR code.

    Args:
        filename (string): Path to file

    Returns:
        qr (string): Value from QR code
    """
    global text
    global value

    # creamos carpeta para guardar imagenes

    # carpeta_imagenes = f"./{fecha.strftime('%Y-%m-%d')}_{carpeta_imagenes}"

    nombre_de_archivo = os.path.splitext(filename)[0]
    print(nombre_de_archivo)
    global text
    global value
    with fitz.open(filename) as pdf:
        page = pdf.load_page(0)
        pix = page.get_pixmap(dpi=300, alpha=False)

        pix.save(
            f"./{carpeta_raiz + carpeta_imagenes}/{nombre_de_archivo}.jpeg", "jpeg"
        )

    # Extract text from pdf
    pdf = pdfplumber.open(filename)
    page_pdf = pdf.pages[0]
    text = page_pdf.extract_text()

    # read qr code
    try:
        img = cv2.imread(
            rf"./{carpeta_raiz + carpeta_imagenes}/{nombre_de_archivo}.jpeg"
        )
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)

    except:
        print("No se pudo leer el código QR")


def parsear_facturas(carpeta_raiz):
    fecha = datetime.datetime.now()

    # Crear carpeta donde se guardan las imagenes

    print(carpeta_imagenes)

    try:
        os.makedirs(f"./{carpeta_raiz + carpeta_imagenes}")

    except:
        print("La carpeta de imagenes ya existe")

    # Carpeta donde se encuentran los pdfs
    for file in os.listdir():
        if file.endswith(".pdf"):
            read_qr_code(file, carpeta_imagenes)
            nombre = re.findall("Razón Social: (.+?) Fecha de Emisión", text)[0]
            punto_de_venta = re.findall("Punto de Venta: (.+?) Comp. Nro:", text)[0]
            comprobante_numero = re.findall("Comp. Nro: (.+?)\n", text)[0]
            cuit = re.findall("CUIT: (.+?) Apellido y Nombre /", text)[0]
            cae = re.findall("CAE N°: (.+?)\n", text)[0]
            facturas_dict[file] = {
                "nombre": nombre,
                "punto_de_venta": punto_de_venta,
                "comprobante_numero": comprobante_numero,
                "cuit": cuit,
                "cae": cae,
                "Enlace CAE": value,
            }

    df = pd.DataFrame.from_dict(facturas_dict, orient="index")
    print(df)

    # Carpeta donde se guardan los excel

    try:
        os.makedirs(f"./{carpeta_raiz + carpeta_excel}")

    except:
        pass

    df.to_excel(f"./{carpeta_raiz + carpeta_excel}/facturas.xlsx")
    print(carpeta_raiz + carpeta_excel)
    print("Excel creado")
    input("Presiona enter para abrir el excel...")
    print("Abriendo excel")
    os.system(f'"./{carpeta_raiz + carpeta_excel}/facturas.xlsx"')
    print("Excel abierto")
    input("Presiona enter para salir...")


if __name__ == "__main__":
    carpeta_raiz = input(
        "Ingrese el nombre de la carpeta donde quiere guardas las imagenes y el excel: "
    )
    print(carpeta_raiz)
    parsear_facturas(carpeta_raiz)
