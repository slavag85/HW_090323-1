# Git command 
+ __git --version__ -Проверяет номер версии Git-а.
+ __git config --global user.name__ - Показывает имя пользователя.
> Для ввода имени Нужно поставить двойные кавычки с двух сторон.
+ __git config --glomal user.email__ - Показывает эл.почту пользователя.
> Для ввода эл.почты нужно поставить двойные кавычки с двух сторон.
+ __git init__ - Создание репазитория.
+ __git add__ - Команда позволяющая Git-у понять что вы хотите внести измениние в канкретный файл.
+ __git commit__ -Создает сохранение того или иного изменения в проэкт. 
> **git commit** сохраняется в иистории и остается до тех пор пока его не удолят.
+ __git status__ - Показывает текещий статус сохранения версии. 
+ __git branch__ - Выводит список веток. 
+ __git branch *branch_name*__- Создает ветку с название. 
+ __git checkout__ - Вывод какого-либо изменения или ветки. 
> Для вывода версии нежно написать 4-6 первых симдолов.
>> Для выводв ветки ввести ее название.
+ __git merge__  - Производит слияние двух веток. 
* __git branch -d *branch_name*__ - Удаляет ветку 


# GitHub
- git clone (https. rep)- Клонировать репозиторий 
- git pull - Взять актуальные изменения с GITHUB 
- git push - Отправить в удаленный репозиторий 

## Как делаем __pull request__ ?
1. Делаем __fork__ репозитория  другово аккаунта 
2. делаем __git clone (https.progect)__ - копирует в наш личный репозиторий 
3. Cоздаем __branch__ и __РОБОТАЕМ ТОЛЬКО В НЕЙ !!!__
4. Днлаем __commit__ 
5. Отправляем на свой аккаунт (git push) 
    > Может ругаться, и предложит подсказку 
6.  *Github.com*  предлогаем __pull request__



### Экспортирование уже существующего репозиторая на Github
    git remote add origin (https_github_rep)
    git branch -M main 
    git push -u origin main




# Markdown 

## Titles

## Text selection 
Синтаксис выделение текста:
**Жирный**  -обрамление двумя звездочками 

__Жтрный__  - обрамление двумя нижнеми подчеркиваниями

*Курсив*  - обрамление одной звездочкой 

_Курсив_  - обрамление одним нижним подчеркиванием 

~~Зачеркнутый~~  - обрамление двумя тильдами 

>*ИХ МОЖНО СОВМЕЩАТЬ



## Lists 
#### Для создания ненумерованного списка в начале следует добавить (+),(-) или (*).
Например;
* one 
- two
+ three 
#### Для cоздания нумерованного списка в начале строки используется цифра с точкой (1.)
Например:
1. one 
2. two
3. three
 
## Images 
>Добавление фотоизибражения из локольной папки

\!\[Error_text]\(image.name)
![no_rover](Curiosity.png)
>Добавление изибражения по ссылке из интернета 

\!\[10_years_of_mision]\(image.https)
![10_years_of_mision](https://mars.nasa.gov/system/resources/detail_files/26910_Curiosity_Poster-web.jpg) 

>Добавление ссылки

\[Mars_images]\(site.https)
## [Mars_images](https://mars.nasa.gov/msl/multimedia/images/?page=0&per_page=25&order=pub_date+desc&search=&category=51%3A176&fancybox=true&url_suffix=%3Fsite%3Dmsl)


>## Эксперемент с .gif

![Rick&Morty.gif](https://media.tenor.com/6Tc-POkXDgYAAAAC/epic-rick-and-morty.gifh)
 
## Tables
work in proсess
## Chek-box 
work in proсess
