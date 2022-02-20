#!/bin/bash

letter_writer () {
    # $1 = username
    # $2 = first_name
    # $3 = department
    # $4 = title
    
    file=/home/$1/Documents
    
    echo "Dear ${2}," > $file
    echo "" > $file
    echo "Welcome to Initech Corperation"
}

read -p "Username: " username
read -p "Full Name: " first_name last_name
read -p "Department: " department
read -p "Job Title: " title

useradd -m $username



echo "User ${username} added!"

read -p "Would you like to add another user? (y/n): " response

if [ $response == 'y' ]; then
    ./Lab2_Task1.sh
fi
