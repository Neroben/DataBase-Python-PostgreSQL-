INSERT INTO sponsor (name)
VALUES ('CocaCola'),
       ('Lucy'),
       ('Большой палец'),
       ('АВГДЕБС');

INSERT INTO match (playdata, count1, club_id1, count2, club_id2, sold)
values (TIMESTAMP '1999-05-22 10:00:00', 2, 3, 1, 7, 200);

INSERT INTO match (playdata, count1, club_id1, count2, club_id2, sold)
values (TIMESTAMP '1999-05-22 10:00:00', 2, 3, 3, 4, 125),
       (TIMESTAMP '1999-05-23 10:00:00', 3, 3, 2, 4, 150),
       (TIMESTAMP '1999-05-24 10:00:00', 2, 3, 2, 4, 250),
       (TIMESTAMP '1999-05-25 10:00:00', 1, 3, 1, 4, 300),
       (TIMESTAMP '1999-05-26 10:00:00', 0, 3, 0, 4, 345);

INSERT INTo club (name, rating, confederacy_id)
values ('Папки', 20, 1);

ALTER TABLE club ADD COLUMN sponsor_id int references sponsor(sponsor_id) on delete no action on update cascade;

UPDATE club SET sponsor_id = 1 where club_id = 1;
UPDATE club SET sponsor_id = 2 where club_id = 2;
UPDATE club SET sponsor_id = 3 where club_id = 3;
UPDATE club SET sponsor_id = 4 where club_id = 4;
UPDATE club SET sponsor_id = 1 where club_id = 5;
UPDATE club SET sponsor_id = 2 where club_id = 6;
UPDATE club SET sponsor_id = 3 where club_id = 7;

SELECT DISTINCT SP.name
from sponsor SP, (  SELECT DISTINCT CL.club_id, CL.sponsor_id
                    FROM club CL, confederacy CO, ( SELECT CL.club_id, count(MC)
                                                    FROM club CL, ( SELECT CL.club_id, MC.playdata
                                                                    FROM match MC, club CL
                                                                    WHERE CL.club_id = MC.club_id1 or CL.club_id = MC.club_id2) MC
                                                    where CL.club_id = MC.club_id
                                                    group by CL.club_id) MC2
                    where Cl.rating > 10 and CL.confederacy_id = 1 and MC2.club_id = CL.club_id and MC2.count < 5) CL2
where SP.name LIKE('%Б%') and SP.sponsor_id = CL2.sponsor_id;

SELECT DISTINCT CL.club_id, Cl.name, MC2.count, CL.confederacy_id
FROM club CL, confederacy CO, (SELECT CL.club_id, count(MC)
FROM club CL, ( SELECT CL.club_id, MC.playdata
                FROM match MC, club CL
                WHERE CL.club_id = MC.club_id1 or CL.club_id = MC.club_id2) MC
                where CL.club_id = MC.club_id
                group by CL.club_id) MC2
where Cl.rating > 10 and CL.confederacy_id = 1 and MC2.club_id = CL.club_id and MC2.count < 5 ;

SELECT CL.club_id, CL.name, count(MC)
FROM club CL, ( SELECT CL.club_id, MC.playdata
                FROM match MC, club CL
                WHERE CL.club_id = MC.club_id1 or CL.club_id = MC.club_id2) MC
where CL.club_id = MC.club_id
group by CL.club_id;

SELECT CL.club_id, MC.playdata
FROM match MC, club CL
WHERE CL.club_id = MC.club_id1 or CL.club_id = MC.club_id2