# bootcamps-sandbox-accounxt-ms-auth



Este sandbox lo puedo usar para practicar
- Clean arquitectre refactoring
- Unit testing
- Integration testing
- E2E testing
- CI/CD


docker build -t vscode-python311-fastapi-xbf .

docker run -it --rm -p 8080:8080 -e PASSWORD=a1b2c3 vscode-python311-fastapi-xbf


docker run -d \
  --name vscode-python311-fastapi-xbf \
  -p 8082:8080 \
  -v "$HOME/.config/code-server:/home/coder/.config/code-server" \
  -v "$PWD:/home/coder/project" \
  -e PASSWORD="a1b2c3" \
  vscode-python311-fastapi-xbf