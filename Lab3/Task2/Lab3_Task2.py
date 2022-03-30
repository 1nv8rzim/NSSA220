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

def find_conflicts(hash_new, hash_original):
    conflicts = {}
    
    for command, original in hash_original.items():
        if original != (new := hash_new[command]):
            conflicts[command] = {'original': original, 'new':new}
    
    return conflicts
    

def print_conflicts(conflicts):
    for command, hashes in conflicts.items():
        print(f'{command}: MD5 original={hashes["original"]}, MD5 new={hashes["new"]}')

def main():
    try:
        new_file, original_file = argv[1:]
    except:
        new_file, original_file = 'md5_new.txt', 'md5_original.txt'
    
    hash_new, hash_original = read_data(new_file, original_file)
    
    conflicts = find_conflicts(hash_new, hash_original)
    
    print_conflicts(conflicts)
    

if __name__ == '__main__':
    main()