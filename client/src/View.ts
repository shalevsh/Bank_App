class View{
    render(result:any){
        $("#posts-container").empty();
        const source = $("#posts-template").html();
        const templatePosts = Handlebars.compile(source);
        $("#posts-container").append(templatePosts(result));
    }
}
