#!/bin/bash
clear
echo -e "                \e[91mInstalling \e[91mRed\e[0mDDoS Tool,"
echo -e "                Please Wait..."
apt-get -y install python-pip > /dev/null 2>&1
apt-get -y install python3-pip > /dev/null 2>&1
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip install tqdm > /dev/null 2>&1
pip install pyfiglet==0.7 > /dev/null 2>&1
clear
echo -e "\e[92m[*]\e[0m \e[91mRed\e[0mDDoS Tool is installed. To run \e[91mR\e[0mDDoS type '\e[1;4mpython3 RDDoS_Tool.py\e[0m' "
