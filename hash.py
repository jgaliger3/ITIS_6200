import json
import os

def hash_file(files):
    hashes = []
    for file_name in files:
        hashes.append(hash(file_name))
    print(hashes)
    data = {
        "file_path" : os.getcwd(),
        "total_files" : files,
        "hash" : hashes
    }
    return data

json_file = "C:\\Users\\Justin\\Documents\\itis_4250\\hash.json"
with open(json_file, "r") as file:
    hash_data = json.load(file)

choice = input("Select 1 to generate a new hash table, or select 2 to verify a hash.")

if choice == "1":
    print("Please enter the correct path to the directory you want analyzed.")
    dir_path = input()
    os.chdir(dir_path)
    print(os.getcwd())

    file = '.'
    file_list = [file for file in os.listdir() if os.path.isfile(file)]
    print(file_list)

    final_list = hash_file(file_list)
    output_file = os.path.join(os.getcwd(), "hash.json")
    with open(output_file, "w") as create:
        json.dump(final_list, create, indent=3)
 
elif choice == '2':
    print(hash_data)
    hash = input("Please enter the hash value: ")
    for hash in hash_data["hash"]:
        if hash == hash_data["hash"]:
            print("Your hash is valid")
        else:
            print("Your hash is invalid")

else:
    print("Help")






