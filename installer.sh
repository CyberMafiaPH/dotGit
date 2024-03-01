#!/bin/bash
clear
echo "1.Linux Desktop"
echo "2.Termux Android"
echo ""
read -p "Choose environment: " environ
if [ -z $environ ]
then
    echo "Invalid input"
    exit 0
elif [ $environ -ge 3 ]
then
    echo "Invalid environment!"
    exit 1
elif [ $environ -eq 1 ]
then 
    sudo apt install wget 
    echo "[*] Done!"
    exit 1
    python3 main.py
elif [ $environ -eq 2 ]
then
    pkg install wget
    echo "[*] Done!"
    exit 2
    python3 main.py
fi