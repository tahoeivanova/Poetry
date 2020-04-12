from django.test import Client
from django.test import TestCase
from users.models import PoemsUser

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        PoemsUser.objects.create_superuser('fred', 'testing@mail.ru', 'secret')




    # проверка статуса ответа по запросу
    def test_status_main_page(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)



    def test_status_analytics_checkbox_page(self):
        response = self.client.get('/analytics/top_100_nouns_and_adjf')
        self.assertEqual(response.status_code, 200)


    # проверка статуса ответа по запросу
    def test_status_add_poem(self):
        response = self.client.get('/poems/add/')
        self.assertEqual(response.status_code, 302)
    # тестирование доступа с авторизированным доступом
    def test_status_dictionary(self): # без авторизации РЕДИРЕКТ
        response = self.client.get('/analytics/dictionary/1283/')
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

# тестирование доступа с авторизированным пользователем
# ОШИБКА 404
    def test_status_dictionary_login(self): # c авторизацией
        self.client.login(username='fred', password='secret')
        response = self.client.get('/analytics/dictionary/1283/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    # post-запрос
    # РАБОТАЕТ
    def test_status_post_poem(self):
        self.client.login(username='fred', password='secret')
        response = self.client.post('/poems/add/', {'poem_title':"Раз два три",'poem_text':'Лучше нет стиха на свете'})
        self.assertEqual(response.status_code, 200)