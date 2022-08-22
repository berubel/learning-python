import requests

def return_cep_data(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    # print(response.text)
    print(response.json())
    cep_data = response.json()
    print(cep_data['logradouro'])
    print(cep_data['complemento'])
    return cep_data

def return_pokemon_data(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    pokemon_data = response.json()
    return pokemon_data

def return_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    return_cep_data('22041001')
    pokemon_data = return_pokemon_data('pikachu')
    print(pokemon_data['sprites']['front_female'])
    #response = return_response('https://globallabs.academy/')
    #print(response)
