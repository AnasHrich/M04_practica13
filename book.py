
class book:
            def __init__(self, AuthorName, BookName, PublicationDate, Pages, Ranking, Weight):
                self.AuthorName = AuthorName
                self.BookName = BookName
                self.PublicationDate = PublicationDate
                self.RankingPages = Pages
                self.Ranking = Ranking

            def get_name(self):
                return self.AuthorName

            def set_name(self, AuthorName):
                self.AuthorName = AuthorName

            def get_BookName(self):
                return self.BookName

            def set_BookName(self, BookName):
                self.BookName = BookName

            def get_PublicationDate(self):
                return self.PublicationDate

            def set_PublicationDate(self, PublicationDate):
                self.PublicationDate = PublicationDate

            def get_Pages(self):
                return self.Pages

            def set_Pages(self, Pages):
                self.Pages = Pages

            def get_Ranking(self):
                return self.Ranking

            def set_Ranking(self, ranking):
                self.Ranking = Ranking
            def get_AuthorName(self):
                return self.AuthorName

            def set_AuthorName(self, AuthorName):
                self.AuthorName = AuthorName

            def information(self):
                print("AuthorName: ", self.AuthorName)
                print("BookName: ", self.BookName)
                print("PublicationDate: ", self.PublicationDate)
                print("Pages: ", self.Pages)
                print("Ranking: ", self.Ranking)
                print("Weight: ", self.Weight)