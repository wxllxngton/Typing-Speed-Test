import random

class TextGenerator:
    def __init__(self):
        self.articles = ['Apartments simplicity or understood do it we. Song such eyes had and off. Removed winding ask explain delight out few behaved lasting.', 'Up branch to easily missed by do. Admiration considered acceptance too led one melancholy expression.']

    def random_article(self):
        random_article_choice = random.choice(self.articles)
        return random_article_choice



