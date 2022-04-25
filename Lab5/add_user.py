#!/usr/bin/python3

# Maxwell Fusco
# April 25th, 2020

from os import system

system('clear')

def read_csv(filename):
    first = True
    users = {}
    with open(filename, 'r') as csv:
        for line in csv:
            if first:
                first = False
                continue
            line = line.strip()
            if line.endswith(','):
                line = line[:-1]
            line = line.split(',')
            if len(line) != 7:
                print(f'UserID {line[0]} was not added due to incorrect amount of fields')
                continue
            if any(item == '' for item in line):
                print(f'UserID {line[0]} was not added due to empty fields')
                continue
            users[line[0]] = {}
            users[line[0]]['LastName'] = line[1]
            users[line[0]]['FirstName'] = line[2]
            users[line[0]]['Office'] = line[3]
            users[line[0]]['Phone'] = line[4]
            users[line[0]]['Department'] = line[5]
            users[line[0]]['Group'] = line[6]
    return users

def check_group(group):
    with open('/etc/group') as file:
        for line in file:
            line = line.strip().split(':')[0]
            if group == line:
                return True
        return False

def create_group(group):
    system(f'groupadd {group}')
    system(f'mkdir /home/{group}')

def user_id_exists(username):
    with open('/etc/passwd') as file:
        for line in file:
            line = line.strip().split(':')[0]
            if line == username:
                return True
        return False

def create_user_id(first, last):
    user_id = first[0] + last
    iterator = 1
    if user_id_exists(user_id):
        while True:
            if user_id_exists(f'{user_id}{iterator}'):
                iterator += 1
            else:
                break
        return f'{user_id}{iterator}'
    return user_id

def main():
    pass

if __name__ == '__main__':
    main()