import json
read_dataset = 'Conectividad_Internet.json'
write_dataset = 'Conectividad_Internet_proc.json'
def check_connect(line_proc):
    types=['ADSL','CABLEMODEM','DIALUP','FIBRAOPTICA','SATELITAL',
            'WIRELESS','TELEFONIAFIJA','3G','4G']
    if all(line_proc[key] == '--' for key in types):
        HasConnect = 'NO'
    else:
        HasConnect = 'SI'
    return HasConnect
with open(read_dataset, mode = 'r', encoding = 'utf-8') as read_file:
    write_file = open(write_dataset, mode = 'w', encoding = 'utf-8')
    data = json.load(read_file)
    print(type(data))
    for record in data:
        record['posee_conectividad'] = check_connect(record)
json.dump(data, write_file, indent=4)
write_file.close()
