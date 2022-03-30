from sys import argv
def read_data(new_file, original_file):
    hash_new, hash_original = {}, {}
    with open(new_file, 'r') as new, open(original_file, 'r') as original:
        for line in new:
            command, hash = line.strip().split()
            hash_new[command] = hash
        for line in original:
            command, hash = line.strip().split()
            hash_original[command] = hash
    return hash_new, hash_original

def main():
    try:
        new_file, original_file = argv[1:]
    except:
        new_file, original_file = 'md5_new.txt', 'md5_original.txt'
    
    hash_new, hash_original = read_data(new_file, original_file)
    
    for command, hash in hash_new.items():
        print(command, hash)
    for command, hash in hash_original.items():
        print(command, hash)
    

if __name__ == '__main__':
    main()