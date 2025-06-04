# Scriptum - Anuario Digital

## Documentación
- (Lista de endpoints)[./doc/endpoints.md]

## Requerimientos
Requerimientos para correr en ambiente local:
  - Conda >= 23.11.0
  - Python >= 3.10
  - Django >= 4.1.6

## Inicialización

- Crea un entorno virtual con conda tomando los requerimientos de un archivo environment.yml
```bash
conda env create -f environment.yml
```

- Si se tiene instalado y configurado un entorno virtual, activarlo:
```bash
conda activate [nombreDelEntorno]
```
- Revisar que entornos se tienen creados
```bash
conda env list
```  

- Levantar el proyecto Scriptum
```bash
python manage.py runserver
```
- Si es necesario, aplicar migraciones
```bash
python manage migrate
```
- Ingresar como administrador
```bash
http://localhost:8000/admin-login/
```

