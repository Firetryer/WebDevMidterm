## game (Implemented)
- id
- title
- description
- discount
- price
- developer
- publisher
- status
- tags
- rating
- platform
- features
- other details
- minOS
- minProcessor
- minMemory
- minStorage
- minGraphics
- maxOS
- maxProcessor
- maxMemory
- maxStorage
- maxGraphics
- languages

## tags (Implemented)
- id
- tag_title
- tags (relationship)


## game_tag (implemented)
- tag_id
- game_id


## user_table (implemented)
- id
- username
- email
- password
- register_date
- admin
- owned_games (relationship)

## owned_games (implemented)
- user_id
- game_id

## review
- id
- game_id
- user_id
- review_title
- review_text
- rating
- date_published


## cart

## cart_item