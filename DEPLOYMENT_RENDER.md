# Deployment en Render

Guía paso a paso para desplegar tu aplicación Django en Render.

## Requisitos Previos

1. Cuenta en [Render.com](https://render.com)
2. Repositorio en GitHub con tu código
3. Los archivos creados: `build.sh`, `render.yaml`, `requirements.txt`

## Pasos para Desplegar

### 1. Subir código a GitHub

```bash
git init
git add .
git commit -m "Initial commit - Django portfolio"
git branch -M main
git remote add origin https://github.com/tu-usuario/django-porfolio.git
git push -u origin main
```

### 2. Crear servicio web en Render

1. Ve a [https://dashboard.render.com](https://dashboard.render.com)
2. Haz clic en **"New +"** → **"Web Service"**
3. Selecciona **"Connect a repository"**
4. Busca y selecciona tu repositorio `django-porfolio`
5. Completa los datos:
   - **Name**: `django-porfolio`
   - **Runtime**: `Python 3`
   - **Build Command**: Ya está configurado en `render.yaml`
   - **Start Command**: Ya está configurado en `render.yaml`

### 3. Crear Base de Datos PostgreSQL

1. Ve a [https://dashboard.render.com](https://dashboard.render.com)
2. Haz clic en **"New +"** → **"PostgreSQL"**
3. Completa los datos:
   - **Name**: `django-porfolio-db`
   - **Database**: `django_porfolio`
   - **User**: `admin`
   - **Plan**: Elige uno (la opción gratuita está disponible)

### 4. Configurar Variables de Entorno

En tu servicio web, ve a **Environment**:

1. **SECRET_KEY**: Genera una nueva con:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **DATABASE_URL**: Copia del servicio PostgreSQL (en "Connections")

3. **DEBUG**: `false`

4. **ALLOWED_HOSTS**: `tu-app.onrender.com`

Ejemplo de DATABASE_URL (Render te lo proporciona):
```
postgresql://admin:password@localhost:5432/django_porfolio
```

### 5. Desplegar

1. Render detectará automáticamente `render.yaml`
2. Ejecutará `build.sh` que:
   - Instala dependencias
   - Ejecuta migraciones
   - Recopila archivos estáticos
3. Inicia la aplicación con Gunicorn

## Solución de Problemas

### Error: "No such table"
- Asegúrate que las migraciones se ejecutaron correctamente
- Verifica en **Logs** que `python manage.py migrate` se ejecutó sin errores

### Error: "DEBUG must be False"
- Asegúrate que la variable `DEBUG=false` está configurada

### Error: "static files not found"
- Ejecuta:
  ```bash
  python manage.py collectstatic --no-input
  ```

### Verificar base de datos conectada
- En **Environment**, verifica que `DATABASE_URL` esté configurado
- Mira los **Logs** para verificar la conexión

## Comandos Útiles Post-Despliegue

### Ejecutar comandos en la aplicación (SSH)

```bash
# Crear superuser
python manage.py createsuperuser

# Ejecutar migraciones manual
python manage.py migrate

# Limpiar archivos estáticos
python manage.py collectstatic --clear --no-input
```

### Acceder a logs

Ve a tu servicio en Render → **Logs** para ver en tiempo real lo que está sucediendo.

## Dominios Personalizados (Opcional)

1. Ve a tu servicio → **Settings**
2. En **Custom Domain**, agrega tu dominio (ej: miportafolio.com)
3. Sigue las instrucciones para configurar DNS

## Backup de Base de Datos

Render proporciona backups automáticos. Para descargar:

1. Ve a tu servicio PostgreSQL
2. En **Backups**, puedes ver y descargar los backups

## Próximos Pasos

- [ ] Configurar dominio personalizado
- [ ] Agregar certificado SSL (automático en Render)
- [ ] Configurar email para contactos
- [ ] Agregar analytics
- [ ] Configurar backups automáticos

¡Listo! Tu aplicación debería estar funcionando en `https://tu-app.onrender.com`
