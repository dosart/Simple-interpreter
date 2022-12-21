 #!/usr/bin/env bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

echo "Loading terminal prompt formatting from .bash_prompt."
echo >> ~/.bashrc
echo "# load terminal prompt formatting from .bash_prompt" >> ~/.bashrc
echo "source ~/.bash_prompt" >> ~/.bashrc
sudo ln -s /vagrant/.bash_prompt ~/.bash_prompt

echo "Installing curl."
sudo apt install -y curl

echo "Installing poetry."
curl -sSL https://install.python-poetry.org | python3 -

echo "Adding poetry to PATH."
export PATH="/home/vagrant/.local/bin:$PATH"
echo >> ~/.bashrc
echo 'export PATH="/home/vagrant/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

echo "Installing pip."
sudo apt-get -y install python3-pip

echo "Installing pre-commit."
pip install --user pre-commit
cd /vagrant
pre-commit install

echo "Installing project dependencies and activating the virtual environment."
poetry config virtualenvs.in-project true
poetry env use python3.8
poetry install
poetry shell
