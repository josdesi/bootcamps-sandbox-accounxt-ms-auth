FROM python:3.11-slim

# Instala code-server y utilidades necesarias
RUN apt-get update && apt-get install -y curl gnupg git && \
    curl -fsSL https://code-server.dev/install.sh | sh

# Crea usuario
RUN useradd -m coder

# Usa el usuario no root
USER coder
WORKDIR /home/coder

# Copia archivos y asegúrate de que pertenecen a 'coder'
COPY --chown=coder:coder ./src ./workspace
COPY --chown=coder:coder requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN chown -R coder:coder /home/coder/workspace

EXPOSE 8080

CMD ["sh", "-c", "code-server --auth password --bind-addr 0.0.0.0:8080 /home/coder/workspace"]
