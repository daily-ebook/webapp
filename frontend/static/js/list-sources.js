$.get(api.sources)
.done(function(sources) {
    var sources = new Ractive({
      el: 'ractive-list-sources',
      template: '#template-list-sources',
      data: sources
    });
});