import requests

token = '3cf905b0529372f4e0c69dee9de925ca'

response = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type': 'application/json'}, json = {
    "trainer_token": token,
    "email": "wayisoj656@orgria.com",
    "password": "Iloveqa1"})

print(response.text)

response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-Type': 'application/json'}, json = {
    "trainer_token": token
})
print(response_confirm.text)

create_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
    json = {
    "name": "Водяной",
    "photo": "https://dolnikov.ru/pokemons/albums/116.png"
})
print(create_pokemon.text)

add_pokemon = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
    json = {
    "pokemon_id": "6179"
})
print(add_pokemon.text)