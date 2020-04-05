# Poetry
сейчас в качестве теста на сайте стихи Пушкина.

Сайт со стихотворениями.

Общие сведения о проекте: Сайт предназначен для чтения и анализа стихов.

Цели: совместить поэзию и IT-технологии.

Задачи:

+сделать удобным анализ творчества поэта (подсчет количества слов, количество уникальных слов, топ-100 слов, словарь стихотворения - вывод слов по частям речи);
+сделать удобным раздел для автора (чтобы автор мог добавлять свой материал);
сделать интересным ознакомление пользователя с поэзией, как-то: озвучить текст стихотворений с помощью модуля синтеза речи;
сделать инструменты-помощники для поэта (например, поиск рифм);
+-сделать генератор фразы из случайных слов стихотворений (* может быть, подключить бота).

Аудитория приложения: Люди, проявляющие интерес к поэзии.

Примерная структура: Карта сайта (что реализовано на данный момент):

- Главная страница - "Home" - название сайта, имя автора стихов;
- Стихотворения - "Poems" - выводит все стихотворения; воможен переход к анимации набора текста стиха и к словарю стиха.
- Оглавление - "Contents".
- Добавить стихотворение - "Add poem" - раздел для автора - (автор может добавить: название, текст***).
- Поэтический анализатор: - "Meta" - подсчитвает кол-во слов всего, кол-во уникальных слов, топ-100 слов  * можно попробовать cделать доступным разные параметры анализа (топ-100 по частям речи, например)
- Auth - войти.
- Register - зарегистрироваться.
- Exit - выйти.

Реализована кнопка переключения цветовых тем (светлый/темный режим)))).

Для superuser возможно добавление и удаление стиха.

***Проблема: не получается изменить одно из названий поля в форме для добавления стиха:
в форме я изменила поле "poem_title" (CharField) на "Название",
но не получается переименовать "poem_text" (models.TextField).
В форме нет типа поля TextField, есть TextInput и др... хотелось бы оставить поле как TextField.