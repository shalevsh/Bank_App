class Model{
    async getRecipesFromServer(ingredientName:string, glutenIsClikced:boolean, diaryIsClikced:boolean){
        return await $.get(`/recipes?ingredient_name=${ingredientName}&has_gluten=${glutenIsClikced}&has_diary=${diaryIsClikced}`);
    }
}