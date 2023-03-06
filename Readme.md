## Iber Ismael Piovani

# Pequeño Script para extraer informacion de las facturas generadas por AFIP.

## Objetivo

Extraer Nombre, CUIT, CAE y enlace a CAE para facilitar la generacion del comprobante CAE y el almacenamiento de los datos en una tabla de excel.

## Requerimientos

- Python 3.8

- [Pandas](https://pandas.pydata.org/docs/)
- [pdfplumber](https://pypi.org/project/pdfplumber/0.1.2/)
- [PyMuPDF](https://pypi.org/project/PyMuPDF/)
- [opencv-python](https://pypi.org/project/opencv-python/)

## Uso

- Clonar el repositorio

```
git clone
```

- Crear un entorno virtual

```
python -m venv venv
```

- Activar el entorno virtual

```
venv\Scripts\activate
```

- Instalar las dependencias

```
pip install -r requirements.txt
```

- cargar las credenciales de la base de datos en el archivo `cfg.py`
- correr descarga.py para descargar el archivo XLS

```
python escaneo_facturas.py
```

```

- correr escaneo_facturas.py para escanear las facturas de la carpeta y obtener los datos.
```

## Resultados

- Una carpeta con el nombre elegido donde se crearan dos carpetas, una con el jpeg de facturas escaneadas y otra con los archivos .xls
- Se generan los enlaces para el certificado CAE

## Posibles mejoras

- generacion certificado cuit
- Ordenar las factuaras segun la eleccion para facilitar orden de impresion
- Creacion de DDBB para almacenar la informacion
- Creacion de un GUI para facilitar el uso.

## Contacto

- [Linkedin](https://www.linkedin.com/in/iber-ismael-piovani-8b35bbba/)
- [Twitter](https://twitter.com/laimas)
- [Github](https://github.com/Vosinepi)
