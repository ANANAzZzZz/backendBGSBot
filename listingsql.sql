PRAGMA foreign_keys = ON;

/*
DROP TABLE IF EXISTS Courier;
DROP TABLE IF EXISTS Order_info;
DROP TABLE IF EXISTS Boardgame_in_circulation;
DROP TABLE IF EXISTS Owner;
DROP TABLE IF EXISTS Renter;
*/
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

/*
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
    "семейная",
    "15",
    2,
    6,
    16,
    "кулинарная игра для семьи",
    "https://hobbygames.ru/image/cache/hobbygames_beta/data/HobbyWorld/Kulinarium/Kulinarium00-1024x1024-wm.jpg", 
    "4.85",
    50,
    500,
    "сложно",
    "стратегия"
    )
    ,
    (    
    1,
    "Доступна",
    "Колонизаторы",
    "Стратегия",
    "10",
    2,
    6,
    18,
    "Создание послений,городов,армий.",
    "https://geekgames.ru/content/images/thumbs/0005769_kolonizatory-hobbyworld.jpeg", 
    "4.30",
    50,
    500,
    "просто",
    "стратегия"
    )
    ,
    (    
    2,
    "Доступна",
    "Dungeon and Dragons",
    "Стратегия",
    "10",
    2,
    6,
    18,
    "D&D — это культовая настольная ролевая игра. Игроки творят общую фэнтезийную историю с абсолютно неожиданным для всех финалом. ... За десятилетия широко известная игра Dungeons & Dragons стала чем-то большим – явлением культуры.",
    "https://cdn1.ozone.ru/s3/multimedia-4/6417031852.jpg", 
    "4.98",
    50,
    500,
    "сложно",
    "стратегия"
    )
    ,
    (    
    3,
    "Доступна",
    "Экивоки",
    "Стратегия",
    "10",
    2,
    6,
    18,
    "Избегание прямых ответов на вопросы неопределенностями, широкими понятиями, модификаторами и квалификаторами. Эквивокация - это самый интересный и творческий вид лжи, речевые признаки и невербальные маркеры которой отличаются наибольшим разнообразием",
    "https://igrrai.ru/image/catalog/Ekivoki/Baza/6048499841.jpg", 
    "4.98",
    50,
    500,
    "сложно",
    "Семейная"
    );

SELECT * FROM Order_info, Boardgame WHERE Order_info.ID_boardgame = Boardgame.ID