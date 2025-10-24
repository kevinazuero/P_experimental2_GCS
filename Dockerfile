# Dockerfile
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Dependencias del sistema (útiles para paquetes que compilen)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el código
COPY . /app/

# Copiar entrypoint y darle permiso
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

# CMD por defecto para desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
