"""En este archivo se debe importar el archivo:
- ./controller.py
- ../util.py as util
- ../data/database.py as database
- ../tests/test_config.py as test_config
- ../tests/load_tests/ddos_simulation.py as ddos_simulation
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.controller.ejercicio_03
"""

import sys
sys.path.append("C:/Users/Escritorio/Documents/GitRepo/Soporte/practica-soporte/practico_02/source")
sys.path.append("C:/Users/Escritorio/Documents/GitRepo/Soporte/practica-soporte/practico_02")

import controller
import util
from data import database
import config.test_config as test_config
from config.ci_cd import deploy_travis
import main

# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert controller.name == "controller"
assert test_config.name == "test_config"
assert deploy_travis.name == "deploy_travis"
# NO MODIFICAR - FIN

# Este es el último ejercicio del TP2
