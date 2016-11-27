var lastRecipe = JSON.parse(localStorage.getItem("lastRecipe"));

var ractiveCreateRecipe = new Ractive({
    el: "ractive-create-recipe",
    template: "#template-create-recipe",
    data: {
        recipe: {
            title: "Placeholder Title",
            sources: []
        },
        lastRecipe: lastRecipe
    }
});

$.get(api.sources)
.done(function(availableSources) {
   ractiveCreateRecipe.set("availableSources", availableSources.sources);
});

ractiveCreateRecipe.on("addSourceToRecipe", function(event){
    var availableSources = ractiveCreateRecipe.get("availableSources");
    var selectedSource = ractiveCreateRecipe.get("sourceToAdd");

    for (var i=0;i<availableSources.length;i++) {
        if (availableSources[i].name === selectedSource) {
            var recipeToAdd = jQuery.extend(true, {}, availableSources[i]); //deep copy object
            ractiveCreateRecipe.push("recipe.sources", recipeToAdd);
            return;
        }
    }

    alert("Unknown source: " + selectedSource);
});

ractiveCreateRecipe.on("selectSourceToEdit", function(event, selectedIndex){
    ractiveCreateRecipe.set("activeIndex", selectedIndex);
});

ractiveCreateRecipe.on("loadLastRecipe", function(event, selectedIndex){
    if(lastRecipe)
        ractiveCreateRecipe.set("recipe", lastRecipe);
});

ractiveCreateRecipe.on("submitGenerateRequest", function(){
    var recipe = ractiveCreateRecipe.get("recipe");

    localStorage.setItem("lastRecipe", JSON.stringify(recipe));

    $.post(api.generate, { recipe: JSON.stringify(recipe) })
    .done(function(task_id){
        window.location.href = frontend.status + task_id;
    });
});
