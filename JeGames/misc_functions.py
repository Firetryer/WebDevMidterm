from JeGames import app, db
from JeGames.models import WebsiteSetting
import os

def get_game_path(game_id):
    return os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], str(game_id))

def get_relative_game_path(game_id):
    return os.path.join(app.config['UPLOAD_FOLDER'], str(game_id))

def create_game_path(game_id):
    os.makedirs(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], str(game_id)), exist_ok=True)
    return get_game_path(game_id)

def setup_website_settings():
    feature_1 = WebsiteSetting(setting_name="feature1", setting_value=None, setting_group = "featured_games")
    feature_2 = WebsiteSetting(setting_name="feature2", setting_value=None, setting_group = "featured_games")
    feature_3 = WebsiteSetting(setting_name="feature3", setting_value=None, setting_group = "featured_games")
    feature_4 = WebsiteSetting(setting_name="feature4", setting_value=None, setting_group = "featured_games")
    feature_5 = WebsiteSetting(setting_name="feature5", setting_value=None, setting_group = "featured_games")
    db.session.add(feature_1)
    db.session.add(feature_2)
    db.session.add(feature_3)
    db.session.add(feature_4)
    db.session.add(feature_5)
    db.session.commit()