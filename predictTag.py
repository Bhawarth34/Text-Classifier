categories = ['academic interests', 'arts and culture', 'automotives',
       'books and literature', 'business and finance', 'careers',
       'video gaming', 'sports', 'food and drinks', 'news and politics',
       'technology and computing', 'movies', 'home and garden', 'health',
       'style and fashion', 'healthy living', 'hobbies and interests',
       'travel', 'shopping', 'television', 'music and audio',
       'personal finance', 'family and relationships', 'pets',
       'pharmaceuticals, conditions, and symptoms', 'real estate']

def get_category(index):
    if 0 <= index < len(categories):
        return categories[index]
    else:
        return 0
