
--data creation
DROP TABLE IF EXISTS User;
CREATE TABLE User (
    id VARCHAR(255) PRIMARY KEY,
    region VARCHAR(255) NOT NULL,
    dlcOwned INTEGER NOT NULL,
    acctStatus VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS Bungie;
CREATE TABLE Bungie (
    id VARCHAR(255) PRIMARY KEY,
    vendor VARCHAR(255) NOT NULL,
    season VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS GameActivities;
CREATE TABLE GameActivities (
    activityName VARCHAR(255) PRIMARY KEY,
    activityType VARCHAR(255) NOT NULL,
    dlc VARCHAR(255) NOT NULL,
    season VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS DLC;
CREATE TABLE DLC (
    season VARCHAR(255) PRIMARY KEY,
    seasonpass BOOLEAN NOT NULL,
    subclass BOOLEAN NOT NULL,
    orderReleased INTEGER NOT NULL,
    campaign VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS Armor;
CREATE TABLE Armor (
    name VARCHAR(255) PRIMARY KEY,
    class VARCHAR(255) NOT NULL,
    subclass VARCHAR(255) NOT NULL,
    season VARCHAR(255) NOT NULL,
    ornament BOOLEAN NOT NULL,
    slot VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS Character;
CREATE TABLE Character (
    id VARCHAR(255) PRIMARY KEY,
    class VARCHAR(255) NOT NULL,
    subclass VARCHAR(255) NOT NULL,
    userID VARCHAR(255) NOT NULL
);

--dummy data
INSERT INTO User VALUES('Sean#1111', 'North America', '3', 'Clear');
INSERT INTO User VALUES('Peter#1112', 'North America', '6', 'Clear');
INSERT INTO User VALUES('Hacker#0000', 'Australia', '2', 'Banned');
INSERT INTO User VALUES('Player#0001', 'South America', '4', 'Clear');

INSERT INTO Bungie VALUES('Dev1', 'Eris', 'Shadowkeep');
INSERT INTO Bungie VALUES('Dev2', 'N/A', 'Shadowkeep');
INSERT INTO Bungie VALUES('Dev3', 'Variks', 'Beyond Light');

INSERT INTO GameActivities VALUES('The Scarlet Keep', 'Strike', 'Shadowkeep', 'Season of the Undying');
INSERT INTO GameActivities VALUES('The Glassway', 'Strike', 'Beyond Light', 'Season of the Hunt');
INSERT INTO GameActivities VALUES('Splicer Lost Sectors', 'Lost Sector', 'Beyond Light', 'Season of the Splicer');
INSERT INTO GameActivities VALUES('Lost Lost Sectors', 'Lost Sector', 'Beyond Light', 'Season of the Lost');
INSERT INTO GameActivities VALUES('Hunt Lost Sectors', 'Lost Sector', 'Beyond Light', 'Season of the Hunt');
INSERT INTO GameActivities VALUES('Fragment', 'PVP Map', 'Shadowkeep', 'Season of the Undying');

INSERT INTO DLC VALUES ('Season of the Outlaw', 'False', 'True', '4', 'Forsaken');	 
INSERT INTO DLC VALUES ('Season of the Hunt', 'True', 'True', '6', 'Beyond Light');
INSERT INTO DLC VALUES ('Season of the Splicer', 'True', 'True', '6', 'Beyond Light');
INSERT INTO DLC VALUES ('Season of the Lost', 'True', 'True', '6', 'Beyond Light');
INSERT INTO DLC VALUES ('Season of the Red War', 'False', 'True', '1', 'Base Game');
INSERT INTO DLC VALUES ('Season of the Curse of Osiris', 'False', 'False', '2', 'Curse of Osiris');
INSERT INTO DLC VALUES ('Season of the Undying', 'True', 'True', '5', 'Shadowkeep');
INSERT INTO DLC VALUES ('Season of the Warmind', 'False', 'False', '3', 'Warmind');

INSERT INTO Character VALUES ('Exo1', 'Warlock', 'Void', 'Sean#1111');
INSERT INTO Character VALUES ('Human1', 'Hunter', 'Solar', 'Sean#1111');
INSERT INTO Character VALUES ('Exo2', 'Hunter', 'Stasis', 'Peter#1112');
INSERT INTO Character VALUES ('Awoken1', 'Titan', 'Arc', 'Hacker#0000');

INSERT INTO Armor VALUES('Sunbracers', 'Warlock', 'Solar', 'Season of the Red War', 'True', 'Arms');
INSERT INTO Armor VALUES('Omnioculus', 'Hunter', 'Void', 'Season of the Hunt', 'False', 'Torso');
INSERT INTO Armor VALUES('Helm of Saint 14', 'Titan', 'Void', 'Season of the Curse of Osiris', 'True', 'Helmet');
INSERT INTO Armor VALUES('One-Eyed Mask', 'Titan', 'Neutral', 'Season of the Outlaw', 'True', 'Helmet');
INSERT INTO Armor VALUES('Star-Eater Scales', 'Hunter', 'Neutral', 'Season of the Splicer', 'False', 'Legs');
INSERT INTO Armor VALUES('Phoenix Protocol', 'Warlock', 'Solar', 'Season of the Outlaw', 'True', 'Torso');
INSERT INTO Armor VALUES('No Backup Plans', 'Titan', 'Void', 'Season of the Lost', 'False', 'Arms');
INSERT INTO Armor VALUES('Armamentarium', 'Titan', 'Neutral', 'Season of the Warmind', 'True', 'Torso');

--queries
--1
.print '1--'
.headers on
SELECT count(User.id)
FROM User
WHERE User.region = 'North America'
;
.print ''

--2
.print '2--'
.headers on
SELECT Armor.name
FROM Armor
WHERE Armor.slot = 'Legs'
;
.print ''

--3
.print '3--'
.headers on
SELECT User.id
FROM User
WHERE User.acctStatus = 'Banned'
;
.print ''

--4
.print '4--'
.headers on
SELECT User.id, count(Character.id)
FROM User, Character
WHERE User.id = Character.userID
GROUP BY User.id
HAVING count(Character.id) > 1
;
.print ''

--5
.print '5--'
.headers on
SELECT DISTINCT Armor.name, DLC.campaign
FROM Armor, DLC
WHERE Armor.season = DLC.season
GROUP BY Armor.name
ORDER BY DLC.orderReleased
;
.print ''

--6
.print '6--'
.headers on 
SELECT Armor.name, GameActivities.activityName
FROM Armor, GameActivities, DLC
WHERE Armor.season = GameActivities.season
and GameActivities.DLC = DLC.campaign
and GameActivities.activityType = 'Lost Sector'
GROUP BY Armor.name
ORDER BY DLC.orderReleased
;
.print ''

--7
.print '7--'
.headers on
SELECT DISTINCT User.id, DLC.campaign 
FROM User, DLC
WHERE User.dlcOwned = DLC.orderReleased
;
.print ''


--8
.print '8--'
.headers on 
SELECT DISTINCT Character.id, Armor.name
FROM Character, Armor
WHERE Armor.class = Character.class
;
.print ''

--9
.print '9--'
.headers on
SELECT count(*)
FROM Armor
WHERE Armor.class = 'Warlock'
;
.print ''

--10
.print '10--'
.headers on
SELECT DISTINCT Armor.subclass, count(*)
FROM Armor
GROUP BY Armor.subclass
;
.print ''

--17
.print '17--'
.headers on
SELECT DISTINCT Character.id, Armor.name
FROM Character, Armor, User, DLC
WHERE Armor.class = Character.class
and User.id = Character.userID
and User.dlcOwned >= DLC.orderReleased
and Armor.season = DLC.season
;
.print ''

--18
.print '18--'
.headers on
SELECT Bungie.id, GameActivities.activityName
FROM Bungie, DLC, GameActivities
WHERE DLC.campaign = Bungie.season
and DLC.campaign = GameActivities.dlc
and DLC.season = 'Season of the Lost'
;
.print ''

--19
.print '19--'
.headers on
SELECT DISTINCT User.id, DLC.campaign
FROM User, DLC
WHERE User.dlcOwned = DLC.orderReleased
;
.print ''

--20
.headers on
SELECT Armor.name, Armor.slot
FROM Armor
WHERE Armor.subclass = 'Void' 
;
.print ''

--11
.print '11--'
.headers on
UPDATE Character
SET class = 'Titan'
WHERE Character.id = 'Exo2'
;
.print ''

--12
.print '12--'
.headers on
UPDATE Bungie
SET vendor = 'Drifter', season = 'Forsaken'
WHERE Bungie.id = 'Dev2'
;
.print ''

--13
.print '13--'
.headers on 
UPDATE Armor
SET ornament = 'True'
WHERE Armor.name = 'Omnioculus'
;
.print ''

--14
.print '14--'
.headers on
UPDATE User
SET acctStatus = 'Banned'
WHERE User.id = 'Player#0001'
;
.print ''

--15
.print '15--'
.headers on 
DELETE FROM Character
WHERE userID in 
    (SELECT User.id
    FROM User
    WHERE User.acctStatus = 'Banned')
;
.print ''

--16
.print '16--'
.headers on 
DELETE FROM Armor
WHERE Armor.season = 'Season of the Red War'
;
.print ''