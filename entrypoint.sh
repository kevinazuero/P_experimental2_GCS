#!/bin/bash
set -e

# Definir la variable de entorno para Django
export DJANGO_SETTINGS_MODULE=CRUD_Universidad.settings

echo "Entrypoint: ejecutar migraciones..."

# Ejecutar migraciones
python manage.py migrate --noinput

# Crear superuser si no existe
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print('Superuser creado')
else:
    print('Superuser ya existe')
"

# Iniciar servidor
exec python manage.py runserver 0.0.0.0:8000
