from os.path import exists

def lerDados(id=1, count=0):
    path = "Accenture-Grupo-Ada\\code\\src\\data\\"
    caminho = f"{path}clients-{id:03d}.csv"
    file = open(caminho,'r')
    while True:
        count +=1
        line = file.readline()
        if not line:
            break
        print("Line {}: {}".format(count, line.strip()))
    file.close

    if exists(caminho):
        lerDados(id+1,count)

lerDados()