# Urbvan Development Challenge

## Correr el proyecto

Una vez que hayas clonado el repositorio y te encuentres dentro de su carpeta base, ve al directorio "employees_web_app" y corre un 

`npm install`

`npm run serve`

con esto podrás ver el front corriendo. 

Para correr el back ve al directorio "backend" y usa el comando

`pip install Flask`

`pip install -U flask-cors`

`python app.py`

dependiendo de tu configuración vas a usar pip/python o pip3/python3

## Front End

Este proyecto usa Vue con Vuetify para la parte del front end, y está compuesto principalmente de 2 pantallas y 3 modales:

- Tabla de empleados

![image](https://user-images.githubusercontent.com/37568592/138820360-7928bc99-e129-4e59-aa8d-d2be0bd7a207.png)

- Detalles de empleado

![image](https://user-images.githubusercontent.com/37568592/138820468-9f2ea8f8-e0d5-40af-ac6b-b8809e5ae0fc.png)

- Modal para agregar empleado

  ![image](https://user-images.githubusercontent.com/37568592/138820258-7d5b6fdc-b9f4-46a4-be9d-7c01ab4b286e.png)

- Modal para agregar nota

![image](https://user-images.githubusercontent.com/37568592/138820432-87600944-a3ce-46c9-8d1d-28f31698d96a.png)

- Modal para editar empleado

![image](https://user-images.githubusercontent.com/37568592/138820677-a1bc8b85-54c7-4622-8064-5f78ea071fdc.png)

## Back end

Para el back del proyecto usé python con Flask para crear las APIs:

- `http://localhost:3000/employee` method: GET
   
   Regresa a todos los empleados guardados
   
- `http://localhost:3000/employee/<employee_id>` method: GET
   
   Regresa la información del empleado solicitado
   
- `http://localhost:3000/employee/update` method: POST
   
   Actualiza la información del empleado especificado
   
- `http://localhost:3000/employee/delete/<employee_id>` method: GET
   
   Borra el empleado especificado
   
- `http://localhost:3000/employee/add` method: POST
   
   Crea un nuevo empleado
   
- `http://localhost:3000/notes/add` method: POST
   
   Crea una nueva nota
   
- `http://localhost:3000/notes` method: GET
   
   Regresa todas las notas 
   
- `http://localhost:3000/notes/<employee_id>` method: GET
   
   Regresa todas las notas del empleado especificado
   
