from django.test import TestCase
from article.models import Article, get_upload_file_name
from django.utils import timezone
from time import time
from django.urls import reverse

class ArticleTest(TestCase):
    def create_article (self , title="test article", body="blah blah"):
        return Article.objects.create(title=title,body =body,
                                      pub_date=timezone.now(),
                                      likes =0)
    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__str__(), a.title)

    def test_get_upload_file_name(self):
        filename = "bakari.txt"
        path="uploaded_files/%s_%s"%(str(time()).replace('.','_'), filename)

        created_path = get_upload_file_name(self, filename)
        self.assertNotEqual(path, created_path)

    def test_articles_list_view(self):
       a = self.create_article()
       url = reverse('index')
       resp = self.client.get(url)

       self.assertEqual(resp.status_code, 200)
       content = resp.content.decode(resp.charset)
       self.assertIn(a.title, content)

    def test_article_detail_view(self):
       a = self.create_article()
       url = reverse('index1', args=[a.id])
       resp = self.client.get(url)

       self.assertEqual(reverse('index1', args=[a.id]),a.get_absolute_url())
       self.assertEqual(resp.status_code, 200)
       content = resp.content.decode(resp.charset)
       self.assertIn(a.title, content)




# Create your tests here.
