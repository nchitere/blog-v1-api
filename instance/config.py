class Config():
    DEBUG=False

class DevelopmentConfig(Config):
    """
    Enable our debug mode to True
    in development in order to auto
    restart our server on code changes
    """
    DEBUG = True

app_configuration={
    'development': DevelopmentConfig
}

AppConfig = app_configuration.get('development')

# blogs/22/comment == 400 blog does not exist
# blogs/122/comment 
# Modify post end point to add comments. default([])
{
    123: {
        "id": 123,
        "title": "recipe",
        "author": "Herbert",
        "comments": [{"id": 1, "content": "Nice post", "Author": "george"}],
    },
    122: {
        "id":122,
        "title": "recipe1",
        "author": "Chitere",
        "comments": []
    }
}