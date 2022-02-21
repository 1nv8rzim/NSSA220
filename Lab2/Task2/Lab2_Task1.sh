#!/bin/bash

letter_writer () {
    # $1 = username
    # $2 = first_name
    # $3 = department
    # $4 = title
    
    file=/home/$1/Documents/welcome.txt
    
    echo "Dear ${2}," > $file
    echo "" >> $file
    echo "Welcome to Initech Corporation! We're so happy to have you in the ${3} Department as a ${4}. Please don't forget to complete your TPS Reports in a timely manner." >> $file
    echo "" >> $file
    echo "Sincerely," >> $file
    echo "Bill Lumbergh" >> $file
}

permission_editor () {
    # $1 = username
    # $2 = home_dir

    chmod -R $1:$1 $2
    
    chmod 444 "${home_dir}/Documents/welcome.txt"
}

file_system_writer () {
    # $1 = username
    # $2 = first_name
    # $3 = department
    # $4 = title
    
    home_dir=/home/$1/
    
    mkdir "${home_dir}Documents"
    mkdir "${home_dir}Desktop"
    mkdir "${home_dir}Pictures"
    mkdir "${home_dir}Downloads"
    
    letter_writer $1 $2 $3 $4
    cp ./ackbar.png "${home_dir}/Pictures/ackbar.png"
    
    permissions_editor $1 $home_dir
}

read -p "Username: " username
read -p "Full Name: " first_name last_name
read -p "Department: " department
read -p "Job Title: " title

useradd -m $username
file_system_writer $username $first_name $department $title



echo "User ${username} added!"

read -p "Would you like to add another user? (y/n): " response

if [ $response == 'y' ]; then
    ./Lab2_Task1.sh
fi
