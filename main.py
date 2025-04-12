from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

# Predefined list of 25 jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why couldn't the leopard play hide and seek? Because he was always spotted.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why don't eggs tell jokes? They might crack up.",
    "What do you call a fish with no eyes? Fsh.",
    "Why did the math book look sad? Because it had too many problems.",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "What do you call a can opener that doesn't work? A can't opener.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the computer go to the doctor? Because it caught a virus.",
    "Why was the broom late? It swept in.",
    "Why did the chicken join a band? Because it had the drumsticks.",
    "Why don't oysters donate to charity? Because they are shellfish.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the man put his money in the blender? He wanted to make some liquid assets.",
    "Why did the cookie go to the doctor? Because it felt crumby.",
    "Why did the stadium get hot after the game? All the fans left.",
    "Why did the banker switch careers? He lost interest.",
    "Why did the cow go to outer space? To see the Milky Way!"
]

@app.get("/joke")
async def get_random_joke():
    # Select a random joke from the list
    joke = random.choice(jokes)
    return JSONResponse(content={"joke": joke})

@app.get("/")
async def index():
    return {"message": "Joke API is up!"}