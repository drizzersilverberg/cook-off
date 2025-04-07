opponents = {
    'yukum' : {
        'name'              : 'Yu Kum',
        'order'             : 1,
        'possible_dishes'   : [1,2,3,4,5,6,7],
        'fixed_dishes'      : {
            'starter'   : 'tomato_soup',
            'main'      : None,
            'dessert'   : None,
        }
    },

    'goetsu' : {
        'name'              : 'Goetsu',
        'order'             : 2,
        'possible_dishes'   : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        'fixed_dishes'      : {
            'starter'   : None,
            'main'      : 'buttered_clams',
            'dessert'   : None,
        }
    },
}

recipes = {
    'rolled_omelet' : {'name' : 'Rolled Omelet',    'order' : 1},
    'tomato_soup'   : {'name' : 'Tomato Soup',      'order' : 2},
    'ohitashi'      : {'name' : 'Ohitashi',         'order' : 3},
}

seasonings = {
    'salt'  : {'name': 'Salt'},
    'sugar' : {'name': 'Sugar'},
}

dishes = {
    'rolled_omelet' : {'name': 'Rolled Omelet', 'recipe_id' : 'rolled_omelet', 'course' : 'main', 'seasoning' : None,       'scoring': {'normal': 2, 'sweet': 2, 'spicy': 2, 'meat': 2, 'fish': 2, 'vegetables': 2, 'japanese': 2, 'western' : 2, 'chinese': 3, 'everything': 5}},
    'sweet_omelet'  : {'name': 'Sweet Omelet',  'recipe_id' : 'rolled_omelet', 'course' : 'main', 'seasoning' : 'sugar',    'scoring': {'normal': 2, 'sweet': 4, 'spicy': 1, 'meat': 2, 'fish': 2, 'vegetables': 2, 'japanese': 2, 'western' : 4, 'chinese': 2, 'everything': 5}},
}

judges = {
    'flik'      : {'name': 'Flik',          'food_preference': 'normal',            'intro': 'Sir Flik is a man with good common sense. We can expect fair judging from him.'},
    'viktor'    : {'name': 'Viktor',        'food_preference': 'everything',        'intro': 'With an appetite like a bear, he\'ll eat anything and love it. It\'s Viktor!!!'},
    'viki'      : {'name': 'Viki',          'food_preference': 'uncommon',          'intro': 'Is her tongue as confused as her brain? It\'s Viki!!!'},
    'sheena'    : {'name': 'Sheena',        'food_preference': 'nothing',           'intro': 'This pampered poodle from the Toran Republic is hard to please! It\'s Sheena!!!'},
}