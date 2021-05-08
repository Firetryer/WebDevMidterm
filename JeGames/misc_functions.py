from JeGames import app
import os

def get_game_path(game_id):
    return os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], str(game_id))

def get_relative_game_path(game_id):
    return os.path.join(app.config['UPLOAD_FOLDER'], str(game_id))

def create_game_path(game_id):
    os.makedirs(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], str(game_id)), exist_ok=True)
    return get_game_path(game_id)
