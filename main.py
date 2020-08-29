import requests

def main():
    cepRecebido=False
    while not cepRecebido:
        cep = input("Insira um CEP com 8 algarismos (somente números): ")
        if (len(str(cep))!=8):
            print("CEP inválido, insira novamente.")
        else:
            cepRecebido=True
    # cep = "01001000"
    url = "https://viacep.com.br/ws/{}/json/".format(cep)
    res = requests.get(url)

    json=res.json()
    if ("erro" in json):
        print("CEP inexistente.")
    elif (res.status_code==requests.codes.ok):
        print("O endereço do CEP {} é:".format(cep))
        print("{} - {}, {} - {}.".format(json["logradouro"], json["bairro"], json["localidade"], json["uf"]))
    else:
        print("Problema com a requisição, tente novamente.")

if __name__ == '__main__':
    main()

