# One-Click-Market v0.1.0

## Descripción
One-Click-Market es un proyecto que simplifica el proceso de mercado en línea, con una arquitectura dividida entre el frontend y el backend. El frontend está construido con Next.js, mientras que el backend utiliza Django Rest Framework. La base de datos utilizada es PostgreSQL. Todo el proyecto está dockerizado para facilitar la implementación y la gestión del entorno.

## Requisitos
Asegúrate de tener instalados los siguientes requisitos antes de ejecutar el proyecto:

- Docker
- Docker Compose

## Instrucciones de Instalación y Ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/one-click-market.git
```

2. Copia el archivo de configuración de ejemplo y ajústalo según tus necesidades:
```bash 
cp .env.template .env
```

3. Construye y levanta los contenedores Docker
```bash
docker-compose -f docker-compose.yml -f docker-compose-develop.yml build
docker-compose -f docker-compose.yml -f docker-compose-develop.yml up -d
```

4. Para acceder al frontend desde el navegador:
```
http://localhost:3000
```

5. Para acceder al admin del backend
```
http://localhost/admin
```

6. Para realizar peticiones mediante api al backend
```
http://localhost/api/
```

7. Para detener el proyecto 
```bash
docker-compose -f docker-compose.yml -f docker-compose-develop.yml down
```

## Estructura del Proyecto
**frontend/**: Contiene el código fuente del frontend construido con Next.js.

**backend/**: Contiene el código fuente del backend construido con Django Rest Framework.

**docker/**: Contiene las configuraciones de cada contenedor

**docker-compose.yml**: Archivo de configuración de Docker Compose para produccion.

**docker-compose-develop.yml**: Archivo de configuración de Docker Compose para development.

**.env**: Archivo de variables de entorno para la configuración.

## Problemas y Soporte

Si encuentras algún problema o necesitas soporte, por favor crea un issue en el repositorio de GitHub.


