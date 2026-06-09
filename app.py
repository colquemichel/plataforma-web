from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# =====================================
# INICIO
# =====================================

@app.route("/")
def inicio():
    return render_template("index.html")


# =====================================
# MANUALES
# =====================================

@app.route("/manuales")
def manuales():
    return render_template("manuales.html")


# =====================================
# DOCUMENTACION
# =====================================

@app.route("/documentacion")
def documentacion():
    return render_template("documentacion.html")


# =====================================
# HERRAMIENTAS
# =====================================

@app.route("/herramientas")
def herramientas():
    return render_template("herramientas.html")


def cargar_excel(nombre_archivo, titulo):

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    ruta_excel = os.path.join(
        BASE_DIR,
        "datos",
        nombre_archivo
    )

    df = pd.read_excel(ruta_excel)

    return render_template(
        "herramienta_tabla.html",
        titulo=titulo,
        herramientas=df.values.tolist()
    )


@app.route("/herramientas/montaje")
def montaje():
    return cargar_excel(
        "montaje.xlsx",
        "MONTAJE"
    )


@app.route("/herramientas/sujecion")
def sujecion():
    return cargar_excel(
        "sujecion.xlsx",
        "SUJECIÓN"
    )


@app.route("/herramientas/medicion")
def medicion():
    return cargar_excel(
        "medicion.xlsx",
        "MEDICIÓN"
    )


@app.route("/herramientas/corte")
def corte():
    return cargar_excel(
        "corte.xlsx",
        "CORTE"
    )


@app.route("/herramientas/golpe")
def golpe():
    return cargar_excel(
        "golpe.xlsx",
        "GOLPE"
    )


# =====================================
# MAQUINAS
# =====================================

@app.route("/maquinas")
def maquinas():
    return render_template("maquinas.html")

@app.route("/maquinas/amoladora")
def amoladora():
    return render_template(
        "maquina_info.html",
        titulo="AMOLADORA",
        carpeta="https://drive.google.com/drive/folders/1NfQG2XVgoO4naapQrdxT5Guj_EjsLASa?usp=drive_link"
    )


@app.route("/maquinas/esmeril")
def esmeril():
    return render_template(
        "maquina_info.html",
        titulo="ESMERIL",
        carpeta="https://drive.google.com/drive/folders/1xFnqMLt7SGUF8sE5rpbertZ19lB4TOoO?usp=drive_link"
    )


@app.route("/maquinas/prensa")
def prensa():
    return render_template(
        "maquina_info.html",
        titulo="PRENSA",
        carpeta="https://drive.google.com/drive/folders/19XiV7fNsFTaqXHoelpF8AJCVe68D4S_b?usp=drive_link"
    )


@app.route("/maquinas/oxiacetileno")
def oxiacetileno():
    return render_template(
        "maquina_info.html",
        titulo="SOLDADURA OXIACETILENO",
        carpeta="https://drive.google.com/drive/folders/1H7nzxgBz3oRgCfDLcol1ugDNqs_GQozI?usp=drive_link"
    )


@app.route("/maquinas/arco")
def arco():
    return render_template(
        "maquina_info.html",
        titulo="SOLDADURA POR ARCO ELÉCTRICO",
        carpeta="https://drive.google.com/drive/folders/1zbxJo1pDWl4FrAOsQlpRkrf_ipYNrDC-?usp=drive_link"
    )


@app.route("/maquinas/taladro")
def taladro():
    return render_template(
        "maquina_info.html",
        titulo="TALADRO",
        carpeta="https://drive.google.com/drive/folders/1UgJ18ehT0LoVL43WBCU9cD5RDdHHIFHd?usp=drive_link"
    )


@app.route("/maquinas/tecle")
def tecle():
    return render_template(
        "maquina_info.html",
        titulo="TECLE",
        carpeta="https://drive.google.com/drive/folders/1Fm8yUMKOO8MYacON7LKs91D-qOLhiK6t?usp=drive_link"
    )


@app.route("/maquinas/torno")
def torno():
    return render_template(
        "maquina_info.html",
        titulo="TORNO",
        carpeta="https://drive.google.com/drive/folders/1eR9NQU0stIvr21MFzDIybNYDcnSSArNk?usp=sharing"
    )
# =====================================
# QR
# =====================================

@app.route("/qr")
def qr():
    return render_template("qr.html")


# =====================================
# SERVIDOR
# =====================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )