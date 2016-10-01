var ractiveCreateRecipe = new Ractive({
    el: "ractive-create-recipe",
    template: "#template-create-recipe",
    data: { 
        recipe: {
            sources: []
        } 
    }
});

$.get(api.sources)
.done(function(availableSources) {
   ractiveCreateRecipe.set("availableSources", availableSources);
});

ractiveCreateRecipe.on("addSourceToRecipe", function(event){
    var availableSources = ractiveCreateRecipe.get("availableSources").sources;
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

ractiveCreateRecipe.on("submitGenerateRequest", function(){
    var recipe = ractiveCreateRecipe.get("recipe");

    $.post(api.generate, { recipe: JSON.stringify(recipe) })
    .done(function(task_details){
        console.log(task_details);
    });
});
