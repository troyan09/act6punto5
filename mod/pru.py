import json
read_dataset = 'mod/Conectividad_Internet.json'
write_dataset = 'mod/Conectividad_Internet_proc.json'
def check_connect(line_proc):
    #types=['ADSL','CABLEMODEM','DIALUP','FIBRAOPTICA','SATELITAL',
            #'WIRELESS','TELEFONIAFIJA','3G','4G']
    if (line_proc['FIBRAOPTICA'] == '--'):
        HasConnect = 'NO'
    else:
        HasConnect = 'SI'
    return HasConnect

try:
    with open(read_dataset, mode = 'r', encoding = 'utf-8') as read_file:
        write_file = open(write_dataset, mode = 'w', encoding = 'utf-8')
        data = json.load(read_file)
        for record in data:
            record['posee_conectividad'] = check_connect(record)
    json.dump(data, write_file, indent=4)
    write_file.close()
except FileNotFoundError:#Este exceept nos permite mansejar errores solo  del tipo relacionado con archivos en general
    print(f"Error: el archivo que intenta leer no existe")
except json.JSONDecodeError:#En la teoria se indica que para el manejo de errores espesificos del formato json se utulize JSONDecodeError como un error generico :D
    print(f"Este archivo no contiene un json valido")
else:
    print("No se levanto la excepsion")


