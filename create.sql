DROP TABLE IF EXISTS Losers;

CREATE TABLE [Losers] (
[loser_id] varchar(5) PRIMARY KEY,
[name] TEXT NOT NULL,
[twitter_handle] TEXT NOT NULL,
[occupation] TEXT NOT NULL
);

PRAGMA foreign_keys = off;

DROP TABLE IF EXISTS Insults;

PRAGMA foreign_keys = on;

CREATE TABLE [Insults] (
[insult_id] varchar(7) PRIMARY KEY,
[tweet] TEXT NOT NULL,
[date] DATE NOT NULL,
[insult] TEXT NOT NULL,
[loser_id] INTEGER NOT NULL,
FOREIGN KEY(loser_id) REFERENCES Losers(loser_id)
);