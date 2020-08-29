import requests

def main():
    # cep = input("Insira um CEP com 8 algarismos (somente números): ")
    cep = "01001000"
    url = "https://viacep.com.br/ws/{}/json/".format(cep)
    res = requests.get(url)

    if (res.status_code==requests.codes.ok):
        json=res.json()
        print("O endereço do CEP {} é:".format(cep))
        print("{} - {}, {} - {}.".format(json["logradouro"], json["bairro"], json["localidade"], json["uf"]))

if __name__ == '__main__':
    main()

