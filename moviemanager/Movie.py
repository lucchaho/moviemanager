class Movie:
    def __init__(self, dic):
        if 'Title' in dic.keys():
            self.title = dic["Title"]
        else:
            self.title = ""
        if 'Plot' in dic.keys():
            self.plot = dic["Plot"]
        else:
            self.plot = ""
        if 'Language' in dic.keys():
            self.lang = dic["Language"]
        else:
            self.lang = ""
        if 'ID' in dic.keys():
            self.id = dic["ID"]
        else:
            self.id = ""
        if 'PublicationDate' in dic.keys():
            self.date = dic["PublicationDate"]
        else:
            self.date = ""

