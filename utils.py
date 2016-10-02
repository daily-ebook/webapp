import uuid

def generate_response_from_task(task):
    response = {}
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': task.info.get('status', '')
        }
    else: # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info),    # this is the exception raised
        }
    return response

def clean_recipe(recipe):
    recipe.filename = "book." + str(uuid.uuid4())
    recipe.outfolder = "./books/"
    recipe.tmp_dir = "/tmp/daily-ebook/"

    return recipe