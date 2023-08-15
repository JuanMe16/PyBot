# PyBot
Discord bot made with Pycord.

# Libraries
Libraries used on this discord bot were mostly pycord and sqlalchemy, but you can check them all in the requirements.txt file.

# Description
This discord bot was made for showcasing my skills of learning libraries and technologies, reading documentation, and using paradigms like POO to work with the tools of the pycord libraries, making the code more mantainable, readeable, and efficient.
I liked a lot working with SQL bases as relational databases works well in SQLite, for this type of cases where i don't need a enterprise level data to save.
I prefer working with SQL and Relational DB in general, because i have way more experience, but i have worked with MongoDB and Firebase(This one specially in JS).

# How can i make the bot work?
Simply as going to the <a href='https://discord.com/developers/applications'> Discord Developer Portal </a> and creating an application and bot, take the token from the bot windows (don't give this to anybody)
later on, change the .env.example to .env and put your TOKEN on the TOKEN Enviroment Variable, after that you can put the SQLite URL where you want to store all your data.
(if you don't know how you can put a SQLite URI check this:) <a href='https://docs.sqlalchemy.org/en/20/core/engines.html#sqlite'> SQLAlchemy SQLite Docs </a>

Don't forget to install all the libraries!
(I recommend using virtual enviroments if you don't want them installed globally in your PC.)

```
pip install -r requirements.txt
```
To make it run on discord:
```
python main.py
```

And that's all, the bot should be log in discord, if you want to use the commands and such, don't forget to generate a discord invite link with all the permissions to make the bot work correctly.
(If you don't know how, you can check it in the OAuth2 window on your application on <a href='https://discord.com/developers/applications'> Discord Developer Portal </a> and click the URL Generator, i recommend you click the bot and administrator checkboxes.)

# What does the bot have?
This is an economy bot, it means it works with a economy purpose on your discord server, it's not like an separated eceonomy on each discord guild server but it's an entire discord cross economy, so it saves people data from whatever server they call the commands, as it's work with a SQLite DB, you need to insert all the items you want to sell with the /item_shop command, i can give you the SQL Sentence to create some basic items on your shop.

```sql
INSERT INTO items VALUES (1,'Apple','Food',50);
INSERT INTO items VALUES (2,'Banana','Food',50);
INSERT INTO items VALUES (3,'Phone','Misc',2500);
INSERT INTO items VALUES (4,'Cap','Misc',450);
INSERT INTO items VALUES (5,'Wood Chest','Chest',350);
```

All the command bots have descriptions of what they do, but note that in order to work with the economy collection of commands, you need to first register yourself in the bot using /register, therefore you can use /work, /deposit, /withdraw, /transfer and other available commands, to play with the bot.

# ERM (Entity Relational Model)

![image](https://i.imgur.com/rBL08lf.png)


# Trello
I used this trello to plan the bot, other ideas and have a follow-up to all the commands and tasks.
This trello is on my mother language (Spanish).

![image](https://i.imgur.com/tb14nOp.png)
