class Movie:
    def __init__(self, dic):
        self.title = dic["Title"]
        self.plot = dic["Plot"]
        self.lang = dic["Language"]
        self.id = dic["ID"]
        self.date = dic["PublicationDate"]

