FROM codercom/code-server:latest


RUN sudo apt-get update && \
    sudo apt-get install -y wget build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev \
    liblzma-dev git && \
    wget https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz && \
    tar xvf Python-3.11.8.tgz && \
    cd Python-3.11.8 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    sudo make altinstall && \
    cd .. && \
    rm -rf Python-3.11.8 Python-3.11.8.tgz

RUN sudo ln -s /usr/local/bin/pip3.11 /usr/local/bin/pip
RUN sudo ln -s /usr/local/bin/python3.11 /usr/local/bin/python

WORKDIR /home/coder/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["code-server"]
