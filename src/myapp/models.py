from .mongodb import BaseModel


class Book(BaseModel):
    collection_name = "books"

    def __init__(
        self,
        title=None,
        author=None,
        published_date=None,
        genre=None,
        price=None,
        year=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.price = price
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}"
