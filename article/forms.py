from article.models import Article,Comment
from django import forms

class ArticleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body',  'thumbnail', 'pub_date')

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('name', 'body')
