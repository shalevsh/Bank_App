from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import requests
from Recipe import Recipe
from server_utils import *
from constants import RECIPES_URL


app = FastAPI()

app.mount("/client/build", StaticFiles(directory="client/build"), name="static")


@app.get("/")
def root():
    return FileResponse("./client/build/index.html")


@app.get("/sanity")
def sanity():
    return {
        "status": "ok"
    }


@app.get("/recipes", status_code=status.HTTP_200_OK)
def recipes_by_ingredient(ingredient_name: str, has_gluten: bool = False, has_diary: bool = False):
    try:
        query = RECIPES_URL % ingredient_name
        result = requests.get(query)
        recipes_dto = result.json().get("results")
    except HTTPException as exception:
        return exception(status_code=404, detail="the ingredient name dosent exist")

    recipes = [Recipe(recipe) for recipe in recipes_dto]
    if has_gluten:
        recipes = remove_recipes(recipes, table_name=GLUTEN)
    if has_diary:
        recipes = remove_recipes(recipes, table_name=DIARY)
    return {"recipes": recipes}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
