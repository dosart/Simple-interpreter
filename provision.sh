#!/usr/bin/env bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

echo "Installing python 3.9.0."
cd /opt
sudo wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz

sudo tar xzf Python-3.9.0.tgz
cd Python-3.9.0
sudo ./configure --enable-optimizations
sudo make altinstall
python3.9 --version
cd /vagrant

echo "Installing curl."
sudo apt install -y curl
curl -V

echo "Installing poetry."
curl -sSL https://install.python-poetry.org | python3 -

echo "Adding poetry to PATH."
echo >> ~/.bashrc
echp 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
poetry --version

echo "Automatically cd to /vagrant folder when vagrant ssh."
echo >> ~/.bashrc
echo "# automatically cd to /vagrant folder when vagrant ssh" >> ~/.bashrc
echo "cd /vagrant" >> ~/.bashrc

echo "Installing project dependencies."
poetry install
