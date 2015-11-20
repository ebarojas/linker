Welcome to Linker, job hunting made easy: a lovechild between Tinder and LinkedIn

# Initial setup of Vagrant Base

# First time cloning ->
This steps only ever needs to be done once. Once the precise64 box is installed on a system the remaining steps refer to that same box regardless of the project.

On an Apple running OS X, download and install [Xcode from the Apple App Store](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12). This is necessary to get some compilers and install Git on the host machine.

Download VirtualBox from http://www.virtualbox.org/wiki/Downloads, install the package.

Download Vagrant 2 or higher from http://downloads.vagrantup.com/, install the package.

vagrant up
vagrant ssh
cd /vagrant

sudo apt-get install build-essential
wget http://nodejs.org/dist/v0.8.16/node-v0.8.16.tar.gz
tar -xzf node-v0.8.16.tar.gz
cd node-v0.8.16/
./configure
make
sudo make install

# Update
sudo npm cache clean -f
sudo npm install -g n
sudo n stable

sudo npm install -g bower
sudo pip install django-bower

sudo apt-get update


install bower + bootstrap



