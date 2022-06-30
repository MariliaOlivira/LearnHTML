from joblib import Parallel, delayed
def get_atrs(informados):
    return " ".join(f'{k.split("_")[-1]}="{v}"'
        for k, v in informados.items())

def criar_blocos(texto, *args, classe="succcess", inline = False):
    tag = "span" if inline else "div"
    html = texto if not callable(texto) else texto(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def criar_lista(*itens):
    lista = ''.join((f'\n\t<li>{item}</li>' for item in itens))
    return f'<ul>{lista}\n</ul>'

def sei():
    nome = input()
    print(nome)

if __name__ == '__main__':
    print(criar_lista("happy"))