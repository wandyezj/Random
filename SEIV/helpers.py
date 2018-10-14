import os

def write_data(items, file_name):
    data = ""
    for i in items:
        data += str(i)

    #print(data)

    f = open(file_name, 'w')
    f.write(data)
    f.close()

def write_data_file(items, run_file_name, file_type):

    lookup = {
        "c":"Components",
        "m":"Mounts",
        "v":"VehicleSizes"
    }
    

    suffix = lookup[file_type]
    name = run_file_name.replace(".py", "")
    file_name = name + "." + suffix + ".txt"
    #print(file_name)
    file_path = os.path.join(".", "mod_snips", file_name)
    #print(file_path)
    write_data(items, file_path)