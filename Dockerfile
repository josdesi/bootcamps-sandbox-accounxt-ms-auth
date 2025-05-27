FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl gnupg git && \
    curl -fsSL https://code-server.dev/install.sh | sh

RUN useradd -m coder

USER coder
WORKDIR /home/coder

# Configure Git default settings
RUN git config --global user.name "Tony Tester" && \
    git config --global user.email "testing@example.com"

# Create extensions directory and install extensions
RUN mkdir -p ~/.local/share/code-server/extensions && \
    code-server --install-extension johhansantana.ai-commit-vscode && \
    code-server --install-extension mhutchie.git-graph

COPY --chown=coder:coder ./src ./workspace
COPY --chown=coder:coder requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R coder:coder /home/coder/workspace

EXPOSE 8080

CMD ["sh", "-c", "code-server --auth password --bind-addr 0.0.0.0:8080 /home/coder/workspace"]
