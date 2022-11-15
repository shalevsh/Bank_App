"use strict";
const model = new Model();
const view = new View();
$("#search-button").on("click", function () {
    const ingredientName = $("#content").val();
    const glutenIsClikced = $("#gluten-cb").is(":checked");
    const diaryIsClikced = $("#diary-cb").is(":checked");
    model.getRecipesFromServer(ingredientName, glutenIsClikced, diaryIsClikced).then((result) => {
        view.render(result);
    });
});
