# 🚀 Guía Completa: Desplegar Django Portfolio en Render

## ✅ Checklist Pre-Deployment

- [x] Código en GitHub
- [x] `render.yaml` configurado
- [x] `build.sh` con migraciones
- [x] `requirements.txt` actualizado (con whitenoise)
- [x] `settings.py` con variables de entorno
- [x] `.env.example` documentado
- [x] `staticfiles/` será creado automáticamente

---

## 📋 Paso 1: Crear Cuenta en Render

1. Ve a [https://render.com](https://render.com)
2. Registrate con email o GitHub (recomendado)
3. Completa tu perfil

---

## 🗄️ Paso 2: Crear Base de Datos PostgreSQL

1. En el dashboard, haz clic en **"New +"**
2. Selecciona **"PostgreSQL"**
3. Completa:
   - **Name**: `django-porfolio-db`
   - **Database**: `django_porfolio`
   - **User**: `admin`
   - **Region**: Elige uno cercano a tu ubicación
   - **Plan**: Free (gratuito, pero con reinicio semanal)

4. Haz clic en **"Create Database"**
5. Espera a que esté listo, luego **copia la URL de conexión** (Internal Database URL)

**Ejemplo de DATABASE_URL:**
```
postgresql://admin:your_password@dpg-xxx.render.internal:5432/django_porfolio
```

---

## 🌐 Paso 3: Crear Servicio Web

1. En el dashboard, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. Haz clic en **"Connect a repository"** y elige tu repo `django-porfolio`
   - Si no aparece, haz clic en "Connect GitHub account"
4. Completa los datos:
   - **Name**: `django-porfolio`
   - **Runtime**: `Python 3`
   - **Build Command**: `bash build.sh`
   - **Start Command**: `gunicorn django_porfolio.wsgi --log-file -`
   - **Plan**: Free (gratuito)

5. Haz clic en **"Advanced"** y luego **"Add Environment Variable"**

---

## 🔐 Paso 4: Configurar Variables de Entorno

En la sección **Environment**, agrega estas variables (verifica que coincidan con tu `.env.example`):

### 1. **SECRET_KEY** (Requerido)
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copia el resultado y pégalo en Render.

### 2. **DATABASE_URL** (Requerido)
Copia la URL de conexión de tu base de datos PostgreSQL (paso 2).

### 3. **DEBUG**
```
false
```

### 4. **ALLOWED_HOSTS**
```
your-app-name.onrender.com
```
(Render te dirá el nombre exacto cuando crees el servicio)

### 5. **CSRF_TRUSTED_ORIGINS**
```
https://your-app-name.onrender.com
```

### 6. **SECURE_SSL_REDIRECT**
```
true
```

### 7. **SESSION_COOKIE_SECURE**
```
true
```

### 8. **CSRF_COOKIE_SECURE**
```
true
```

---

## 🚀 Paso 5: Desplegar

1. Haz clic en **"Create Web Service"**
2. Render comenzará a:
   - Clonar el repositorio
   - Ejecutar `bash build.sh` (instala paquetes, migraciones, collectstatic)
   - Iniciar la aplicación con Gunicorn
3. Verifica los **Logs** para asegurar que todo salió bien

---

## 📝 Paso 6: Post-Despliegue

### Crear un superuser (administrador)

En Render, ve a tu Web Service y abre la terminal (**Shell**):

```bash
python manage.py createsuperuser
```

Completa:
- Username: `admin`
- Email: tu-email@example.com
- Password: una contraseña segura

### Acceder al admin

```
https://your-app-name.onrender.com/admin/
```

---

## 🆘 Solución de Problemas

### ❌ Error: "No such table"
**Solución:**
- Ve a los Logs del Web Service
- Verifica que `python manage.py migrate` se ejecutó sin errores
- Si no, redeploy: haz un `git push` en tu repositorio

### ❌ Error: "DEBUG must be False"
**Solución:**
- Verifica que `DEBUG=false` en las variables de entorno (sin comillas)

### ❌ Error: "static files not found" (404)
**Solución:**
- Render ejecuta automáticamente `collectstatic` en `build.sh`
- Si aún falla, redeploy manualmente

### ❌ Error: "Connection refused" con la base de datos
**Solución:**
- Verifica que `DATABASE_URL` sea correcto
- Usa la **Internal Database URL** (no la externa)
- Espera 2-3 minutos después de crear la BD

### ❌ CSRF Forbidden (403)
**Solución:**
- Verifica `CSRF_TRUSTED_ORIGINS` en variables de entorno
- Debe incluir tu dominio en Render con `https://`

---

## 📊 Monitoreo

Desde el dashboard de Render, puedes:
- Ver logs en tiempo real
- Monitorear CPU y memoria
- Redeploy si es necesario (Push → Auto-deploy)
- Ver información del servicio

---

## 🔄 Actualizar Código

Solo haz `git push` a `main`:
```bash
git add .
git commit -m "Tu mensaje"
git push origin main
```

Render auto-deployará automáticamente.

---

## 📞 Contacto y Soporte

- Docs de Render: https://render.com/docs
- Docs de Django: https://docs.djangoproject.com
- Whitenoise: https://whitenoise.readthedocs.io/

¡Tu aplicación está lista para producción! 🎉
