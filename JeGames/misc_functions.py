from JeGames import app, db
from JeGames.models import WebsiteSetting
import os
from math import ceil

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

class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num
