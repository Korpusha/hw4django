from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Author(models.Model):
    def __str__(self):
        return self.name_author

    name_author = models.CharField(max_length=120)


class Book(models.Model):
    def __str__(self):
        return self.name_book

    name_book = models.CharField(max_length=120)
    year_of_public = models.DateField(null=True)
    available = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)


class User(models.Model):
    def __str__(self):
        return self.name_user

    name_user = models.CharField(max_length=120)
    books_available = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='available_books', null=True,
                                        limit_choices_to={'available': True})


class LikeOrDislike(models.Model):
    class Meta:
        abstract = True

    do_you_like_it = models.BooleanField(verbose_name="Do you like it?", null=True)


class BlogUser(models.Model):
    blog_user_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, default=0)
    password = models.CharField(max_length=120, default=0)

    def __str__(self):
        return self.blog_user_name

    class Meta:
        ordering = ['-blog_user_name']


class Blog(LikeOrDislike):
    article_name = models.CharField(max_length=120)
    article_body = models.TextField(default=0)
    date_of_publicity = models.DateField(null=True)
    blog_user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='blogs', null=True)

    def __str__(self):
        return self.article_name

    class Meta:
        ordering = ['-date_of_publicity']


class Comment(LikeOrDislike):
    comment = models.TextField()
    blog_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.comment

    def save(self, **kwargs):
        if not self.id:
            for i in str(self.comment).split():
                if i == 'Start':
                    self.comment += ' (*)'
                    break

                elif i == 'Middle':
                    self.comment = '(*) ' + str(self.comment) + ' (*)'
                    break

                elif i == 'Finish':
                    self.comment = '(*) ' + str(self.comment)
                    break

            self.created_at = datetime.now() - relativedelta(years=1)
        super().save(**kwargs)
