# RUNBOOK - CookiesLab Web

## 1. Crear carpeta limpia

Recomendado:

```cmd
cd /d C:\x
mkdir CookiesLab-Web
```

Copia el contenido de este starter directo dentro de `C:\x\CookiesLab-Web`, para que `manage.py` quede así:

```text
C:\x\CookiesLab-Web\manage.py
```

Evita dejarlo como muñeca rusa tipo:

```text
C:\x\CookiesLab-Web\CookiesLab-Web-Starter\CookiesLab-Web-Starter
```

## 2. Crear entorno virtual

```cmd
cd /d C:\x\CookiesLab-Web
py -m venv .venv
.venv\Scripts\activate
```

## 3. Instalar dependencias

```cmd
pip install -r requirements.txt
```

Si `mysqlclient` falla en Windows, usar temporalmente:

```cmd
pip install pymysql
```

Y pedirle a Claude que adapte `config/settings.py` para PyMySQL. Lo ideal es `mysqlclient`, pero PyMySQL salva vidas cuando Windows se pone payaso.

## 4. Crear base de datos

En Navicat o consola MySQL:

```sql
CREATE DATABASE cookieslab_web CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 5. Configurar variables

```cmd
copy .env.example .env
```

Editar `.env`:

```env
DB_NAME=cookieslab_web
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
```

Si XAMPP está en 3307:

```env
DB_PORT=3307
```

## 6. Migrar

```cmd
python manage.py makemigrations
python manage.py migrate
```

Si alguna app no crea tabla:

```cmd
python manage.py migrate --run-syncdb
```

## 7. Crear admin

```cmd
python manage.py createsuperuser
```

## 8. Datos demo

```cmd
python manage.py seed_demo
```

## 9. Correr servidor

```cmd
python manage.py runserver
```

## 10. Pendientes de producción

- Configurar dominio.
- Usar hosting con soporte Python/Django.
- Pasar `DEBUG=False`.
- Servir estáticos con WhiteNoise o servidor real.
- Configurar media files correctamente.
- Respaldos de MySQL.
- No meter pagos en fase 1.
