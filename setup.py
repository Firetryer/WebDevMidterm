from setuptools import setup

setup(
        name='JeGames',
        packages=['JeGames'],
        version='0.1',
        include_package_data=True,
        description="JeGames online video game store. A Project for advanced web development",
        zip_safe=False,
        install_requires=[
            'flask',
            'Flask-WTF',
            'WTforms',
            'flask-login',
            'flask_sqlalchemy',
            'flask_bcrypt',
            'gunicorn',
            'pymysql',
            'psycopg2',
            'Flask-Migrate'
            ]
        )
