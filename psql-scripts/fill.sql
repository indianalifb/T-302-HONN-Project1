INSERT INTO Player( 
    username,
    HighScore
)
VALUES 
('Steven', 0);

INSERT INTO Player(
     username,
     HighScore
) 
VALUES 
('George', 0); 

 INSERT INTO PLAYER(
     username,
     HighScore 
 )
VALUES
('420-blazemaster69', 1080);

INSERT INTO PLAYER( 
     username,
     HighScore
)
VALUES
 ('MagniDolphinsCry10', 190);

INSERT INTO PLAYER( 
     username,
    HighScore
)
VALUES
('GNRz', 300);

INSERT INTO PLAYER(
    username,
    HighScore
)
VALUES
('StickyMcJew', 3000);

INSERT INTO PLAYER(
    username,
    HighScore
)
VALUES
('KarmelCoolJew', 2432);


INSERT INTO FRIENDS (
    adder_id,
    reciever_id
)
VALUES
((SELECT USER_ID FROM PLAYER WHERE USERNAME = 'Steven'),
(SELECT USER_ID FROM PLAYER WHERE USERNAME = 'George'));
