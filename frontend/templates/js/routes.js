api = {
    sources: "(( url_for('api.sources') ))",
    generate: "(( url_for('api.generate') ))",
    status: "(( url_for('api.status', task_id="") ))"
};

frontend = {
    status: "(( url_for('frontend.show_status', task_id="") ))"
};
