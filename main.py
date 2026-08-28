import requests
apiKey = "e5300e600b03422da477ab367e8819dd"
response = requests.get(
    'https://api.spoonacular.com/recipes/findByIngredients',
    params={"ingredients": "chicken, rice, tomato", "apiKey": apiKey })
print(response.status_code)
print(response.json())

