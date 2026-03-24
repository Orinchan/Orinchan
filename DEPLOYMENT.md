# 🚀 Guía de Despliegue - Django Portafolio

## Preparación Local

Antes de desplegar, asegúrate de que todo funcione localmente:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

## Opción 1: Render.com (Recomendado - GRATIS)

**Ventajas:** Fácil, gratis, sin tarjeta de crédito

### Pasos:

1. **Crea una cuenta en [render.com](https://render.com)**

2. **Sube tu código a GitHub** (opcional, pero recomendado):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   # Luego sube a GitHub
   ```

3. **Desde Render Dashboard:**
   - Click en "New Web Service"
   - Conecta tu repositorio GitHub
   - Configura:
     - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command:** `gunicorn django_porfolio.wsgi:application`
     - **Environment:** Python 3.10
   - Espera a que despliegue (~2-3 minutos)

4. **URL de tu sitio** aparecerá como: `https://tu-app.onrender.com`

---

## Opción 2: Railway.app (GRATIS con créditos)

1. **Crea cuenta en [railway.app](https://railway.app)**
2. **Conecta tu repositorio GitHub**
3. **Railway detectará automáticamente Django**
4. Configura variables de entorno si es necesario

---

## Opción 3: PythonAnywhere (Fácil para principiantes)

1. Crea cuenta en [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sube tu código
3. Configura un web app Django
4. Actualiza los archivos de configuración web

---

## Checklist de Despliegue

✅ `requirements.txt` actualizado  
✅ `.gitignore` creado  
✅ `Procfile` presente  
✅ `DEBUG = False` en producción (automático en Render)  
✅ `ALLOWED_HOSTS` configurado  
✅ `STATIC_ROOT` configurado  
✅ Base de datos migrada  
✅ Código en Git (GitHub)  

---

## Variables de Entorno Importantes

Render y Railway pueden automáticamente generar:
- `SECRET_KEY` - Se genera automáticamente
- `DEBUG` - Set to `false` en producción

---

## Solución de Problemas

### "ModuleNotFoundError"
```bash
# Asegúrate que requirements.txt está actualizado:
pip freeze > requirements.txt
```

### Imágenes no cargan
- Las imágenes se guardan en `media/`
- En producción, considera usar un servicio como AWS S3 o Cloudinary

### Errores de base de datos
```bash
# Run migrations en servidor:
python manage.py migrate
```

---

## Siguientes Pasos

1. Dominio personalizado (compra en GoDaddy, Namecheap)
2. Email personalizado
3. Agregar más funcionalidades
4. Mejorar SEO

¡Éxito en el despliegue! 🎉
