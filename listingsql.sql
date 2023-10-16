PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Courier;
DROP TABLE IF EXISTS Order_info;
DROP TABLE IF EXISTS Boardgame_in_circulation;
DROP TABLE IF EXISTS Owner;
DROP TABLE IF EXISTS Renter;
DROP TABLE IF EXISTS Boardgame;


CREATE TABLE Boardgame( 
"ID" INTEGER PRIMARY KEY,
"Name" VARCHAR(30),
"Status" VARCHAR(30),
"Description" VARCHAR(30),
"Middle_game_time" VARCHAR(30),
"Min_players" INTEGER,
"Max_players" INTEGER,
"Age" INTEGER,
"Rools" VARCHAR(30),
"Image" VARCHAR(30),
"Rating" FLOAT,
"Price_per_day" MONEY,
"Base_cost" MONEY,
"Complexity" FLOAT,
"Category" VARCHAR(30));


CREATE TABLE Renter(
"FIO" VARCHAR(30),
"ID" INTEGER PRIMARY KEY,
"Rating" FLOAT);

CREATE TABLE Owner(
"FIO" VARCHAR(30),
"ID" INTEGER PRIMARY KEY,
"Rating" FLOAT);

CREATE TABLE Boardgame_in_circulation(
"ID_Renter" INTEGER REFERENCES Renter("ID") ON DELETE CASCADE ON UPDATE CASCADE,
"ID_boardgame" INTEGER REFERENCES Boardgame("ID") ON DELETE CASCADE ON UPDATE CASCADE,
"ID_Owner" INTEGER REFERENCES Owner("ID")ON DELETE CASCADE ON UPDATE CASCADE,
"Status_boardgame" VARCHAR(30),
"Boardgame_state" VARCHAR(30),
PRIMARY KEY("ID_renter","ID_boardgame","ID_Owner"));

CREATE TABLE Order_info(
"ID" INTEGER PRIMARY KEY,
"Status" VARCHAR(30),
"Order_time" VARCHAR(30),
"Addres_recive" VARCHAR(30),
"Addres_send"VARCHAR(30),
"ID_renter" INTEGER, 
"ID_boardgame" INTEGER, 
"ID_owner" INTEGER,
"ID_courier" INTEGER REFERENCES Courier("ID")ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY("ID_renter", "ID_boardgame", "ID_owner") REFERENCES Boardgame_in_circulation("ID_Renter", "ID_boardgame", "ID_Owner") ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Courier(
"FIO" VARCHAR(30),
"ID" INTEGER PRIMARY KEY,
"Rating" FLOAT);

INSERT INTO Courier("FIO", "ID","Rating") VALUES 
('ГУАП',1,2.2),
('ИТМО',2,3.3);
*/
INSERT INTO Boardgame(
"ID", 
"Status",
"Name",
"Description",
"Middle_game_time",
"Min_players",
"Max_players",
"Age",
"Rools",
"Image",
"Rating",
"Price_per_day",
"Base_cost",
"Complexity",
"Category") VALUES (
    0,
    "Доступна",
    "Кулинариум",
    "«Кулинария» - вкусная и ароматная настольная игра для юных поварят!",
    "15",
    2,
    6,
    16,
    "Игроки выбирают себе фишки и ставят их на старт. Чтобы определить очередность хода каждого игрока, 
    все участники бросают кубик. Первым ходит тот, у кого выпало наибольшее количество очков. И так далее по убыванию.
    Игроки по очереди бросают кубик и передвигают свою фишку на выпавшее на нем количество ходов. Фишки идут по кругу. 
    Каждая ячейка содержит различные ингредиенты к блюдам. Побеждает тот, кто первым доберется до финиша.",
    "https://hobbygames.ru/image/cache/hobbygames_beta/data/HobbyWorld/Kulinarium/Kulinarium00-1024x1024-wm.jpg", 
    "4.85",
    50,
    500,
    "сложно",
    "Семейная"
    )
    ,
    (    
    1,
    "Доступна",
    "Колонизаторы",
    "«Колонизаторы» - экономическая и стратегическая настольная игра. 
    Вам придется распоряжаться ресурсами, тщательно обдумывать ходы 
    и тесно взаимодействовать с соперниками.",
    "10",
    2,
    6,
    18,
    "В начале игры раскладывается поле с изображением острова Катан. 
    Краями острова служит рамка, состоящая из пазлов голубого цвета. 
    Внутри выкладывают шестиугольные гексы суши.
    Затем нужно пронумеровать гексы ярлыками. 
    А положите с одного края, В – с другого. Разместите ярлыки по алфавиту или в числовом порядке. Цифры определяют игрока, получающего ресурс.",
    "https://geekgames.ru/content/images/thumbs/0005769_kolonizatory-hobbyworld.jpeg", 
    "4.30",
    50,
    500,
    "просто",
    "Стратегия"
    )
    ,
    (    
    2,
    "Доступна",
    "Dungeon and Dragons",
    "Dungeons and Dragons (D&D) — коллаборативная ролевая игра о приключениях в фэнтезийном мире. 
    Партия в D&D разворачивается под управлением гейм-мастера, который создаёт игровой мир, 
    ведёт приключение, определяет правила, направляет взаимодействие игроков по ходу сценария.",
    "10",
    2,
    6,
    18,
    "Перед началом игры каждый участник создаёт себе персонажа, заполняя лист со слабыми и сильными сторонами героя. 
    Важно также указать дополнительные детали: 
    например, как выглядит персонаж, во что он одет и что делает его уникальным. 
    Опытные игроки продумывают биографию до мельчайших подробностей.",
    "https://cdn1.ozone.ru/s3/multimedia-4/6417031852.jpg", 
    "4.98",
    50,
    500,
    "сложно",
    "Стратегия"
    )
    ,
    (    
    3,
    "Доступна",
    "Экивоки",
    "Смысл этой игры очень прост: нужно объяснять загаданные слова разными способами:
     показывать жестами
     рисовать с закрытыми глазами
     лепить из пластилина",
    "10",
    2,
    6,
    18,
    "Игра заключается в том, что один игрок объясняет загаданные на карточках слова и выражения тем или иным способом:
    жестами, рисунками, словами и т. п. 
    Другие должны за 1 минуту это слово отгадать. Бросьте кубик, возьмите карточку",
    "https://igrrai.ru/image/catalog/Ekivoki/Baza/6048499841.jpg", 
    "4.98",
    50,
    500,
    "легко",
    "Логическая"
    );

--SELECT * FROM Order_info, Boardgame WHERE Order_info.ID_boardgame = Boardgame.ID