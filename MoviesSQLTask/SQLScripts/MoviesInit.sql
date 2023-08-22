USE QABootcamp;
-- ALTER TABLE Movies AUTO_INCREMENT =1;
-- Temporarily for Required Error 1052 which can happen because of constraints on foreign keys with composite keys
-- To read more about this error https://bobcares.com/blog/mysql-error-12/ 
-- SET FOREIGN_KEY_CHECKS=0;

-- Insert for Movie Categories

insert into Genre (Category_Name) values ("Action");
insert into Genre (Category_Name) values ("Adventure");
insert into Genre (Category_Name) values ("Animation");
insert into Genre (Category_Name) values ("Crime");
insert into Genre (Category_Name) values ("Drama");
insert into Genre (Category_Name) values ("Comedy");
insert into Genre (Category_Name) values ("Fantasy");
insert into Genre (Category_Name) values ("Thriller");
insert into Genre (Category_Name) values ("Horror");
insert into Genre (Category_Name) values ("Psychological");
insert into Genre (Category_Name) values ("Romance");
insert into Genre (Category_Name) values ("Western");
insert into Genre (Category_Name) values ("Sci-Fi");
insert into Genre (Category_Name) values ("Mystery");
/*
Keys
====
1: 'Action'
2: 'Adventure'
3: 'Animation'
4: 'Crime'
5: 'Drama'
6: 'Comedy'
7: 'Fantasy'
8: 'Thriller'
9: 'Horror'
10: 'Psychological'
11: 'Romance'
12: 'Western'
13: 'Sci-Fi'
14: 'Mystery'
*/

-- Insert for Movies
insert into Movies (Movie_Title, Duration) values ("The flash", 140);
insert into Movies (Movie_Title, Duration) values ("Man of Steel", 145);
insert into Movies (Movie_Title, Duration) values ("Justice League", 240);

insert into Movies (Movie_Title, Duration) values ("Justice League War World", 90);

insert into Movies (Movie_Title, Duration) values ("Scooby Doo Spooky Games", 25);
insert into Movies (Movie_Title, Duration) values ("Ambulance", 140);

insert into Movies (Movie_Title, Duration) values ("Goodfellas", 145);

insert into Movies (Movie_Title, Duration) values ("Casino", 180);

insert into Movies (Movie_Title, Duration) values ("Ugram", 145);

insert into Movies (Movie_Title, Duration) values ("The Out Laws", 95);

insert into Movies (Movie_Title, Duration) values ("Love Hard", 105);

insert into Movies (Movie_Title, Duration) values ("One Rangar", 90);

insert into Movies (Movie_Title, Duration) values ("Hypnotic", 93);

insert into Movies (Movie_Title, Duration) values ("Happy Death Day", 95);

insert into Movies (Movie_Title, Duration) values ("Happy Death Day 2U", 95);

insert into Movies (Movie_Title, Duration) values ("Run Rabbit Run", 95);

insert into Movies (Movie_Title, Duration) values ("The Black Demon", 100);

insert into Movies (Movie_Title, Duration) values ("Swallow", 95);

insert into Movies (Movie_Title, Duration) values ("Intrusion", 92);

insert into Movies (Movie_Title, Duration) values ("Hypnotic", 88);

insert into Movies (Movie_Title, Duration) values ("Love Again", 105);
insert into Movies (Movie_Title, Duration) values ("My Fault", 117);
insert into Movies (Movie_Title, Duration) values ("Chemical Hearts", 93);

insert into Movies (Movie_Title, Duration) values ("Blood & Gold", 100);

insert into Movies (Movie_Title, Duration) values ("The Old Way", 95);

insert into Movies (Movie_Title, Duration) values ("True Grit", 110);

insert into Movies (Movie_Title, Duration) values ("Star Wars IV A New Hope", 105);
insert into Movies (Movie_Title, Duration) values ("Star Wars V Empire Strikes Back", 124);
insert into Movies (Movie_Title, Duration) values ("Star Wars VI Return of the Jedi", 131);

insert into Movies (Movie_Title, Duration) values ("Transformers", 144);
insert into Movies (Movie_Title, Duration) values ("Transformers: Revenge of the Fallen", 149);

insert into Movies (Movie_Title, Duration) values ("Missing", 131);

insert into Movies (Movie_Title, Duration) values ("The Pale Blue Eye", 128);

insert into Movies (Movie_Title, Duration) values ("Luther: The Fallen Sun", 129);
/*
Keys
====
1: ('The flash', 140)
2: ('Man of Steel', 145)
3: ('Justice League', 240)
4: ('Justice League War World', 90)
5: ('Scooby Doo Spooky Games', 25)
6: ('Ambulance', 140)
7: ('Goodfellas', 145)
8: ('Casino', 180)
9: ('Ugram', 145)
10: ('The Out Laws', 95)
11: ('Love Hard', 105)
12: ('One Rangar', 90)
13: ('Hypnotic', 93)
14: ('Happy Death Day', 95)
15: ('Happy Death Day 2U', 95)
16: ('Run Rabbit Run', 95)
17: ('The Black Demon', 100)
18: ('Swallow', 9)
19: ('Intrusion', 92)
20: ('Hypnotic', 88)
21: ('Love Again', 105)
22: ('My Fault', 117)
23: ('Chemical Hearts', 93)
24: ('Blood & Gold', 100)
25: ('The Old Way', 95)
26: ('True Grit', 110)
27: ('Star Wars IV A New Hope', 105)
28: ('Star Wars V Empire Strikes Back', 124)
29: ('Star Wars VI Return of the Jedi', 131)
30: ('Transformers', 144)
31: ('Transformers: Revenge of the Fallen', 149)
32: ('Missing', 131)
33: ('The Pale Blue Eye', 128)
34: ('Luther: The Fallen Sun', 129)
*/

-- Insert for Directors
insert into directors (Director_Name) values ("Andy Muschietti");
insert into directors (Director_Name) values ("Zack Snyder");

insert into directors (Director_Name) values ("Jeff Wamster");
insert into directors (Director_Name) values ("Ernie Altbacker");
insert into directors (Director_Name) values ("Josie Campbell");

insert into directors (Director_Name) values ("Curt Geda");

insert into directors (Director_Name) values ("Michael Bay");

insert into directors (Director_Name) values ("Martin Scorsese");

insert into directors (Director_Name) values ("Vijay Kanakamedala");

insert into directors (Director_Name) values ("Tyler Spindel");

insert into directors (Director_Name) values ("Hernán Jiménez");

insert into directors (Director_Name) values ("Jesse V. Johnson");

insert into directors (Director_Name) values ("Robert Rodriguez");

insert into directors (Director_Name) values ("Christopher Landon");

insert into directors (Director_Name) values ("Daina Reid");

insert into directors (Director_Name) values ("Adrian Grunberg");

insert into directors (Director_Name) values ("Carlos Mirabella Davis");

insert into directors (Director_Name) values ("Adam Salky");

insert into directors (Director_Name) values ("Matt Angel");
insert into directors (Director_Name) values ("Suzanne Coote");

insert into directors (Director_Name) values ("Jim Strouse");

insert into directors (Director_Name) values ("Domingo Gonzalez");

insert into directors (Director_Name) values ("Richard Tanne");

insert into directors (Director_Name) values ("Peter Thorwarth");

insert into directors (Director_Name) values ("Brett Donowho");

insert into directors (Director_Name) values ("Ethan Coen");
insert into directors (Director_Name) values ("Joel Coen");

insert into directors (Director_Name) values ("George Lucas");

insert into directors (Director_Name) values ("Irwin Kreshner");

insert into directors (Director_Name) values ("Richard Marquand");

insert into directors (Director_Name) values ("Nicholas D. Johnson");
insert into directors (Director_Name) values ("Will Merrick");

insert into directors (Director_Name) values ("Scott Cooper");

insert into directors (Director_Name) values ("Jamie Payne");
/*
Keys
====
1: 'Andy Muschietti'
2: 'Zack Snyder'
3: 'Jeff Wamster'
4: 'Ernie Altbacker'
5: 'Josie Campbell'
6: 'Curt Geda'
7: 'Michael Bay'
8: 'Martin Scorsese'
9: 'Vijay Kanakamedala'
10: 'Tyler Spindel'
11: 'Hernán Jiménez'
12: 'Jesse V. Johnson'
13: 'Robert Rodriguez'
14: 'Christopher Landon'
15: 'Daina Reid'
16: 'Adrian Grunberg'
17: 'Carlos Mirabella Davis'
18: 'Adam Salky'
19: 'Matt Angel'
20: 'Suzanne Coote'
21: 'Jim Strouse'
22: 'Domingo Gonzalez'
23: 'Richard Tanne'
24: 'Peter Thorwarth'
25: 'Brett Donowho'
26: 'Ethan Coen'
27: 'Joel Coen'
28: 'George Lucas'
29: 'Irwin Kreshner'
30: 'Richard Marquand'
31: 'Nicholas D. Johnson'
32: 'Will Merrick'
33: 'Scott Cooper'
34: 'Jamie Payne'
*/

-- Insert into Writers
insert into Writers (Writer_Name) values ("Christina Hodson");
insert into Writers (Writer_Name) values ("John Francis Daley");
insert into Writers (Writer_Name) values ("Jonathan Goldstein");
insert into Writers (Writer_Name) values ("David Goye");
insert into Writers (Writer_Name) values ("Christopher Nolan");
insert into Writers (Writer_Name) values ("Jerry Siegel");
insert into Writers (Writer_Name) values ("Abburi Ravi");
insert into Writers (Writer_Name) values ("Chris Terrio");
insert into Writers (Writer_Name) values ("Zack Snyder");
insert into Writers (Writer_Name) values ("Jeremy Adams");
insert into Writers (Writer_Name)  values ("Ernie Altbacker");
insert into Writers (Writer_Name) values ("Josie Campbell");
insert into Writers (Writer_Name) values ("Curt Geda");

insert into Writers (Writer_Name)  values ("Chris Fedak");
insert into Writers (Writer_Name) values ("Laurits Punch-Petersen");
insert into Writers (Writer_Name) values ("Lars Andreas Pedersen");

insert into Writers (Writer_Name) values ("Martin Scorsese");
insert into Writers (Writer_Name) values ("Nicholas Pileggi");

insert into Writers (Writer_Name) values ("Vijay Kanakamedala");

insert into Writers (Writer_Name) values ("Ben Zazove");
insert into Writers (Writer_Name) values ("Evan Turner");

insert into Writers (Writer_Name) values ("Danny Mackey");
insert into Writers (Writer_Name) values ("Rebecca Ewing");

insert into Writers (Writer_Name) values ("Jesse V. Johnson");

insert into Writers (Writer_Name) values ("Robert Rodriguez");
insert into Writers (Writer_Name) values ("Max Borenstein");

insert into Writers (Writer_Name) values ("Scott Lobdell");
insert into Writers (Writer_Name) values ("Christopher Landon");

insert into Writers (Writer_Name) values ("Hannah Kent");

insert into Writers (Writer_Name) values ("Carlos Cisco");
insert into Writers (Writer_Name) values ("Boise Esquerra");

insert into Writers (Writer_Name) values ("Carlos Mirabella Davis");

insert into Writers (Writer_Name) values ("Chris Sparling");

insert into Writers (Writer_Name) values ("Richard D'Ovidio");

insert into Writers (Writer_Name) values ("Jim Strouse");
insert into Writers (Writer_Name) values ("Sofie Kramer");
insert into Writers (Writer_Name) values ("Andrea Wilson");

insert into Writers (Writer_Name) values ("Domingo Gonzalez");
insert into Writers (Writer_Name) values ("Mercedes Ron");

insert into Writers (Writer_Name) values ("Richard Tanne");
insert into Writers (Writer_Name) values ("Krystal Sutherland");

insert into Writers (Writer_Name) values ("Peter Thorwarth");
insert into Writers (Writer_Name) values ("Stefan Barth");

insert into Writers (Writer_Name) values ("Carl W Lucas");

insert into Writers (Writer_Name) values ("Ethan Coen");
insert into Writers (Writer_Name) values ("Joel Coen");
insert into Writers (Writer_Name) values ("Charles Portis");

insert into Writers (Writer_Name) values ("George Lucas");
insert into Writers (Writer_Name) values ("Leigh Brackett");
insert into Writers (Writer_Name) values ("Lawrance Kasdan");

insert into Writers (Writer_Name) values ("Roberto Orci");
insert into Writers (Writer_Name) values ("Alex Kurtzman");
insert into Writers (Writer_Name) values ("John Rogers");
insert into Writers (Writer_Name) values ("Ehren Kruger");

insert into Writers (Writer_Name) values ("Sev Ohanian");
insert into Writers (Writer_Name) values ("Nicholas D. Johnson");
insert into Writers (Writer_Name) values ("Will Merrick");

insert into Writers (Writer_Name) values ("Scott Cooper");
insert into Writers (Writer_Name) values ("Louis Bayard");

insert into Writers (Writer_Name) values ("Neil Cross");
insert into Writers (Writer_Name) values ("Joseph Barbera");
insert into Writers (Writer_Name) values ("William Hanna");
insert into Writers (Writer_Name) values ("Toom Venkat");

/*
Keys
====
1: 'Christina Hodson'
2: 'John Francis Daley'
3: 'Jonathan Goldstein'
4: 'David Goye'
5: 'Christopher Nolan'
6: 'Jerry Siegel'
7: 'Joe Shuster'
8: 'Chris Terrio'
9: 'Zack Snyder'
10: 'Jeremy Adams'
11: 'Ernie Altbacker'
12: 'Josie Campbell'
13: 'Curt Geda'
14: 'Chris Fedak'
15: 'Laurits Punch-Petersen'
16: 'Lars Andreas Pedersen'
17: 'Martin Scorsese'
18: 'Nicholas Pileggi'
19: 'Vijay Kanakamedala'
20: 'Ben Zazove'
21: 'Evan Turner'
22: 'Danny Mackey'
23: 'Rebecca Ewing'
24: 'Jesse V. Johnson'
25: 'Robert Rodriguez'
26: 'Max Borenstein'
27: 'Scott Lobdell'
28: 'Christopher Landon'
29: 'Hannah Kent'
30: 'Carlos Cisco'
31: 'Boise Esquerra'
32: 'Carlos Mirabella Davis'
33: 'Chris Sparling'
34: "Richard D'Ovidio"
35: 'Jim Strouse'
36: 'Sofie Kramer'
37: 'Andrea Wilson'
38: 'Domingo Gonzalez'
39: 'Mercedes Ron'
40: 'Richard Tanne'
41: 'Krystal Sutherland'
42: 'Peter Thorwarth'
43: 'Stefan Barth'
44: 'Carl W Lucas'
45: 'Ethan Coen'
46: 'Joel Coen'
47: 'Charles Portis'
48: 'George Lucas'
49: 'Leigh Brackett'
50: 'Lawrance Kasdan'
51: 'Roberto Orci'
52: 'Alex Kurtzman'
53: 'John Rogers'
54: 'Ehren Kruger'
55: 'Sev Ohanian'
56: 'Nicholas D. Johnson'
57: 'Will Merrick'
58: 'Scott Cooper'
59: 'Louis Bayard'
60: 'Neil Cross'
61: 'Joseph Barbera'
62: 'William Hanna'
63: 'Toom Venkat'
*/

-- Insert for MovieStars
insert into MovieStars (Star_Name) values ("Ezra Miller");
insert into MovieStars (Star_Name) values ("Sasha Calle");
insert into MovieStars (Star_Name) values ("Ben Affleck");
insert into MovieStars (Star_Name) values ("Jeremy Irons");
insert into MovieStars (Star_Name) values ("Henry Cavill");
insert into MovieStars (Star_Name) values ("Amy Adams");
insert into MovieStars (Star_Name) values ("Diane Lane");
insert into MovieStars (Star_Name) values ("Gal Galdot");
insert into MovieStars (Star_Name) values ("Jensen Ackles");
insert into MovieStars (Star_Name) values ("Stana Katic");
insert into MovieStars (Star_Name) values ("Matt Bomer");
insert into MovieStars (Star_Name) values ("Frank Welker");
insert into MovieStars (Star_Name) values ("Grey Griffin");
insert into MovieStars (Star_Name) values ("Matthew Lillard");
insert into MovieStars (Star_Name) values ("Mindy Cohn");
insert into MovieStars (Star_Name) values ("Jake Gyllenhaal");
insert into MovieStars (Star_Name) values ("Yahya Abdul-Mateen");
insert into MovieStars (Star_Name) values ("Eiza Gonzalez");
insert into MovieStars (Star_Name) values ("Robert De Niro");
insert into MovieStars (Star_Name) values ("Ray Liotta");
insert into MovieStars (Star_Name) values ("Joe Pesci");
insert into MovieStars (Star_Name) values ("Sharon Stone");
insert into MovieStars (Star_Name) values ("Allari Naresh");
insert into MovieStars (Star_Name) values ("Mirnaa");
insert into MovieStars (Star_Name) values ("Adam Devine");
insert into MovieStars (Star_Name) values ("Pierce Brosnan");
insert into MovieStars (Star_Name) values ("Ellen Barkin");
insert into MovieStars (Star_Name) values ("Nina Dobrev");
insert into MovieStars (Star_Name) values ("Darren Barnett");
insert into MovieStars (Star_Name) values ("Jimmy O Yang");
insert into MovieStars (Star_Name) values ("Mikaela Hoover");
insert into MovieStars (Star_Name) values ("Thomas Jane");
insert into MovieStars (Star_Name) values ("Dean Jaggar");
insert into MovieStars (Star_Name) values ("Dominique Tipper");
insert into MovieStars (Star_Name) values ("Alice Braga");
insert into MovieStars (Star_Name) values ("JD Pardo");
insert into MovieStars (Star_Name) values ("Jessica Rothe");
insert into MovieStars (Star_Name) values ("Israel Broussard");
insert into MovieStars (Star_Name) values ("Ruby Modine");
insert into MovieStars (Star_Name) values ("Sarah Snook");
insert into MovieStars (Star_Name) values ("Lilly LaTorre");
insert into MovieStars (Star_Name) values ("Neil Melville");
insert into MovieStars (Star_Name) values ("Omar Chaparro");
insert into MovieStars (Star_Name) values ("Bolivar Sanchez");
insert into MovieStars (Star_Name) values ("Carlos Solorzano");
insert into MovieStars (Star_Name) values ("Haley Bennett");
insert into MovieStars (Star_Name) values ("Austin Stowell");
insert into MovieStars (Star_Name) values ("Denis O'Hare");
insert into MovieStars (Star_Name)  values ("Freida Pinto");
insert into MovieStars (Star_Name) values ("Logan Marshall Green");
insert into MovieStars (Star_Name) values ("Robert John Burke");
insert into MovieStars (Star_Name)  values ("Kate Siegel");
insert into MovieStars (Star_Name) values ("Jason O'Mara");
insert into MovieStars (Star_Name) values ("Dule Hill");
insert into MovieStars (Star_Name)  values ("Priyanka Chopra Jonas");
insert into MovieStars (Star_Name) values ("Sam Heughan");
insert into MovieStars (Star_Name) values ("Celine Dion");
insert into MovieStars (Star_Name) values ("Nicola Wallace");
insert into MovieStars (Star_Name) values ("Gabriel Guevara");
insert into MovieStars (Star_Name) values ("Marta Hazas");
insert into MovieStars (Star_Name)  values ("Lili Reinhart");
insert into MovieStars (Star_Name) values ("Austin Abrams");
insert into MovieStars (Star_Name) values ("Sarah Jones");
insert into MovieStars (Star_Name)  values ("Robert Maaser");
insert into MovieStars (Star_Name) values ("Jordis Triebel");
insert into MovieStars (Star_Name) values ("Marie Hacke");
insert into MovieStars (Star_Name) values ("Phillip Aguirre");
insert into MovieStars (Star_Name) values ("Ryan Kiera Armstrong");
insert into MovieStars (Star_Name) values ("Clint Howard");
insert into MovieStars (Star_Name) values ("Jeff Bridges");
insert into MovieStars (Star_Name) values ("Matt Damon");
insert into MovieStars (Star_Name) values ("Hailee Steinfield");
insert into MovieStars (Star_Name) values ("Mark Hamil");
insert into MovieStars (Star_Name) values ("Harrison Ford");
insert into MovieStars (Star_Name) values ("Carrie Fisher");
insert into MovieStars (Star_Name) values ("Shia LeBeouf");
insert into MovieStars (Star_Name) values ("Megan Fox");
insert into MovieStars (Star_Name) values ("Josh Duhamel");
insert into MovieStars (Star_Name) values ("Tim Griffin");
insert into MovieStars (Star_Name) values ("Ava Zaria Lee");
insert into MovieStars (Star_Name) values ("Nia Long");
insert into MovieStars (Star_Name) values ("Christian Bale");
insert into MovieStars (Star_Name) values ("Harry Melling");
insert into MovieStars (Star_Name) values ("Simon McBurney");
insert into MovieStars (Star_Name) values ("Idris Elba");
insert into MovieStars (Star_Name) values ("Cynthia Erivo");
insert into MovieStars (Star_Name) values ("Andy Serkis");
insert into MovieStars (Star_Name) values ("Darren Barnett");
/*
Keys
====
1: 'Ezra Miller'
2: 'Sasha Calle'
3: 'Ben Affleck'
4: 'Jeremy Irons'
5: 'Henry Cavill'
6: 'Amy Adams'
7: 'Diane Lane'
8: 'Gal Galdot'
9: 'Jensen Ackles'
10: 'Stana Katic'
11: 'Matt Bomer'
12: 'Frank Welker'
13: 'Grey Griffin'
14: 'Matthew Lillard'
15: 'Mindy Cohn'
16: 'Jake Gyllenhaal'
17: 'Yahya Abdul-Mateen'
18: 'Eiza Gonzalez'
19: 'Robert De Niro'
20: 'Ray Liotta'
21: 'Joe Pesci'
22: 'Sharon Stone'
23: 'Allari Naresh'
24: Mirnaa
25: 'Adam Devine'
26: 'Pierce Brosnan'
27: 'Ellen Barkin'
28: 'Nina Dobrev'
29: 'Darren Barnett'
30: 'Jimmy O Yang'
31: 'Mikaela Hoover'
32: 'Thomas Jane'
33: 'Dean Jaggar'
34: 'Dominique Tipper'
35: 'Alice Braga'
36: 'JD Pardo'
37: 'Jessica Rothe'
38: 'Israel Broussard'
39: 'Ruby Modine'
40: 'Sarah Snook'
41: 'Lilly LaTorre'
42: 'Neil Melville'
43: 'Omar Chaparro'
44: 'Bolivar Sanchez'
45: 'Carlos Solorzano'
46: 'Haley Bennett'
47: 'Austin Stowell'
48: "Denis O'Hare"
49: 'Freida Pinto'
50: 'Logan Marshall Green'
51: 'Robert John Burke'
52: 'Kate Siegel'
53: "Jason O'Mara"
54: 'Dule Hill'
55: 'Priyanka Chopra Jonas'
56: 'Sam Heughan'
57: 'Celine Dion'
58: 'Nicola Wallace'
59: 'Gabriel Guevara'
60: 'Marta Hazas'
61: 'Lili Reinhart'
62: 'Austin Abrams'
63: 'Sarah Jones'
64: 'Robert Maaser'
65: 'Jordis Triebel'
66: 'Marie Hacke'
67: 'Phillip Aguirre'
68: 'Ryan Kiera Armstrong'
69: 'Clint Howard'
70: 'Nicholas Cage'
71: 'Jeff Bridges'
72: 'Matt Damon'
73: 'Hailee Steinfield'
74: 'Mark Hamil'
75: 'Harrison Ford'
76: 'Carrie Fisher'
77: 'Shia LeBeouf'
78: 'Megan Fox'
79: 'Josh Duhamel'
80: 'Tim Griffin'
81: 'Ava Zaria Lee'
82: 'Nia Long'
83: 'Christian Bale'
84: 'Harry Melling'
85: 'Simon McBurney'
86: 'Idris Elba'
87: 'Cynthia Erivo'
88: 'Andy Serkis'
89: 'Darren Barnett'
*/

-- insert for reviewers
insert into reviewers (Reviewer_Name, City) values ("Joe Stevens", "London");
insert into reviewers (Reviewer_Name, City) values ("Jo Ferry", "London");
insert into reviewers (Reviewer_Name, City) values ("Jane Daley", "Sheffied");
insert into reviewers (Reviewer_Name, City) values ("Paul Cross", "Norwich");

insert into reviewers (Reviewer_Name, City) values ("Simon Tate", "Sheffied");
insert into reviewers (Reviewer_Name, City) values ("Peter Simmons", "Scotland");
insert into reviewers (Reviewer_Name, City) values ("Mike Smith", "Scotland");

insert into reviewers (Reviewer_Name, City) values ("Paul Trust", "Brighton");
insert into reviewers (Reviewer_Name, City) values ("Samantha Taylor", "Brighton");
insert into reviewers (Reviewer_Name, City) values ("Jason Reeds", "London");
insert into reviewers (Reviewer_Name, City) values ("Anne Tate", "Newmarket");
insert into reviewers (Reviewer_Name, City) values ("Peter Hancock", "Newmarket");

insert into reviewers (Reviewer_Name, City) values ("Jessie Youth", "Leeds");
insert into reviewers (Reviewer_Name, City) values ("Bob Missile", "Manchester");
insert into reviewers (Reviewer_Name, City) values ("Jennifer Aymes", "Manchester");
insert into reviewers (Reviewer_Name, City) values ("Simon Ridley", "Leeds");
insert into reviewers (Reviewer_Name, City) values ("Charlie Simms", "Leeds");
insert into reviewers (Reviewer_Name, City) values ("Charlene", "Ripon");
insert into reviewers (Reviewer_Name, City) values ("Mike Howorth", "Ripon");
insert into reviewers (Reviewer_Name, City) values ("Jason Richards", "Manchester");
insert into reviewers (Reviewer_Name, City) values ("Jermaine Roberts", "York");
insert into reviewers (Reviewer_Name, City) values ("Mike Chalk", "York");
insert into reviewers (Reviewer_Name, City) values ("Pat Colt", "York");
insert into reviewers (Reviewer_Name, City) values ("Nicola Holmes", "Sheffield");
insert into reviewers (Reviewer_Name, City) values ("Joseph Pine", "London");

insert into reviewers (Reviewer_Name, City) values ("Craig Peters", "Barnsley");

insert into reviewers (Reviewer_Name, City) values ("Kelly Bowchurch", "London");
insert into reviewers (Reviewer_Name, City) values ("Daniel Taylor", "Barnsley");

insert into reviewers (Reviewer_Name, City) values ("Jess Best", "London");
insert into reviewers (Reviewer_Name, City) values ("Joseph Holiday", "Barnsley");

insert into reviewers (Reviewer_Name, City) values ("Jane Doe", "Oxford");

/*
Keys
====
1: ('Joe Stevens', 'London')
2: ('Jo Ferry', 'London')
3: ('Jane Daley', 'Sheffied')
4: ('Paul Cross', 'Norwich')
5: ('Simon Tate', 'Sheffied')
6: ('Peter Simmons', 'Scotland')
7: ('Mike Smith', 'Scotland')
8: ('Paul Trust', 'Brighton')
9: ('Samantha Taylor', 'Brighton')
10: ('Jason Reeds', 'London')
11: ('Anne Tate', 'Newmarket')
12: ('Peter Hancock', 'Newmarket')
13: ('Jessie Youth', 'Leeds')
14: ('Bob Missile', 'Manchester')
15: ('Jennifer Aymes', 'Manchester')
16: ('Simon Ridley', 'Leeds')
17: ('Charlie Simms', 'Leeds')
18: ('Charlene', 'Ripon')
19: ('Mike Howorth', 'Ripon')
20: ('Jason Richards', 'Manchester')
21: ('Jermaine Roberts', 'York')
22: ('Mike Chalk', 'York')
23: ('Pat Colt', 'York')
24: ('Nicola Holmes', 'Sheffield')
25: ('Joseph Pine', 'London')
26: ('Craig Peters', 'Barnsley')
27: ('Kelly Bowchurch', 'London')
28: ('Daniel Taylor', 'Barnsley')
29: ('Jess Best', 'London')
30: ('Joseph Holiday', 'Barnsley')
31: ('Jane Doe', 'Oxford')
*/

-- Insert for CategorizedMovie

-- Categoring "The Flash" => Action, Adventure, Fantasy
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (1, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (1, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (1, 6);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (1, 7);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (2, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (2, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (2, 7);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (2, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (3, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (3, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (3, 7);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (4, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (4, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (4, 3);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (4, 7);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (4, 13);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (5, 3);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (5, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (6, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (6, 4);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (6, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (6, 8);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (7, 4);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (7, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (8, 4);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (8, 5);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (9, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (9, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (9, 11);


insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (10, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (10, 4);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (10, 6);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (11, 11);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (11, 6);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (12, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (12, 8);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (13, 14);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (13, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (13, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (13, 10);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (14, 14);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (14, 6);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (14, 9);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (15, 14);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (15, 6);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (15, 9);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (16, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (16, 9);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (17, 9);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (17, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (17, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (18, 9);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (18, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (18, 5);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (19, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (19, 14);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (19, 10);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (19, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (19, 5);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (20, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (20, 10);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (20, 14);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (21, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (21, 6);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (21, 11);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (22, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (22, 11);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (23, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (23, 11);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (24, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (24, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (24, 12);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (25, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (25, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (25, 12);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (26, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (26, 12);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (27, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (27, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (27, 7);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (27, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (28, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (28, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (28, 7);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (28, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (29, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (29, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (29, 7);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (29, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (30, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (30, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (30, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (31, 1);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (31, 2);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (31, 13);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (32, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (32, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (32, 14);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (33, 8);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (33, 14);

insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (34, 4);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (34, 5);
insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (34, 13);

-- Insert for MovieCast
insert into MovieCast (FKMovie_ID, FKStar_ID) values (1, 1);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (1, 2);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (1, 3);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (1, 4);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (2, 5);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (2, 6);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (2, 7);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 1);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 2);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 3);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 4);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 5);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 8);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 6);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (3, 7);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (4, 9);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (4, 10);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (4, 11);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (5, 12);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (5, 13);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (5, 14);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (5, 15);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (6, 16);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (6, 17);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (6, 18);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (7, 19);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (7, 20);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (7, 21);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (8, 19);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (8, 22);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (8, 21);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (9, 23);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (9, 24);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (10, 25);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (10, 26);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (10, 27);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (11, 28);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (11, 29);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (11, 30);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (11, 31);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (11, 89);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (12, 32);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (12, 33);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (12, 34);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (13, 35);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (13, 36);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (13, 3);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (14, 37);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (14, 38);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (14, 39);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (15, 37);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (15, 38);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (15, 39);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (16, 40);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (16, 41);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (16, 42);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (17, 43);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (17, 44);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (17, 45);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (18, 46);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (18, 47);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (18, 48);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (19, 49);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (19, 50);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (19, 51);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (20, 52);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (20, 53);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (20, 54);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (21, 55);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (21, 56);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (21, 57);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (22, 58);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (22, 59);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (22, 60);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (23, 61);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (23, 62);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (23, 63);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (24, 64);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (24, 65);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (24, 66);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (25, 67);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (25, 68);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (25, 69);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (25, 70);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (26, 71);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (26, 72);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (26, 73);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (27, 74);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (27, 75);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (27, 76);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (28, 74);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (28, 75);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (28, 76);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (29, 74);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (29, 75);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (29, 76);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (30, 77);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (30, 78);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (30, 79);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (31, 77);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (31, 78);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (31, 79);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (32, 80);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (32, 81);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (32, 82);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (33, 83);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (33, 84);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (33, 85);

insert into MovieCast (FKMovie_ID, FKStar_ID) values (34, 86);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (34, 87);
insert into MovieCast (FKMovie_ID, FKStar_ID) values (34, 88);

-- Insert for MovieScript
-- Insert for "The Flash" Script Writers
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (1, 1);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (1, 2);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (1, 3);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (2, 4);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (2, 5);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (2, 6);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (3, 7);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (3, 8);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (3, 9);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (4, 10);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (4, 11);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (4, 12);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (5, 13);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (6, 14);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (6, 15);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (6, 16);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (7, 17);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (7, 18);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (8, 17);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (8, 18);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (9, 19);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (9, 8);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (9, 63);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (10, 20);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (10, 21);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (11, 23);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (11, 22);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (12, 24);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (13, 25);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (13, 26);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (14, 27);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (15, 28);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (15, 27);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (16, 29);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (17, 30);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (17, 31);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (18, 32);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (19, 33);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (20, 34);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (21, 37);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (21, 36);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (21, 35);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (22, 38);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (22, 39);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (23, 40);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (23, 41);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (24, 42);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (24, 43);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (25, 44);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (26, 45);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (26, 46);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (26, 47);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (27, 48);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (28, 48);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (28, 49);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (28, 50);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (29, 48);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (29, 50);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (30, 51);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (30, 52);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (30, 53);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (31, 51);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (31, 52);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (31, 54);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (32, 55);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (32, 56);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (32, 57);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (33, 58);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (33, 59);

insert into MovieScript (FKMovie_ID, FKWriter_ID) values (34, 60);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (5, 61);
insert into MovieScript (FKMovie_ID, FKWriter_ID) values (5, 62);

-- Insert for DirectedMovies
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (1, 1);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (2, 2);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (3, 2);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (4, 3);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (5, 6);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (6, 7);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (7, 8);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (8, 8);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (9, 9);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (10, 10);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (11, 11);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (12, 12);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (13, 13);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (14, 14);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (15, 14);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (16, 15);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (17, 16);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (18, 17);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (19, 18);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (20, 19);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (20, 20);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (21, 21);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (22, 22);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (23, 23);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (24, 24);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (25, 25);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (26, 26);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (26, 27);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (27, 28);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (28, 29);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (29, 30);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (30, 7);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (31, 7);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (32, 31);
insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (32, 32);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (33, 33);

insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (34, 34);

-- Insert for Ratings
-- Insert for "The Flash" Ratings
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (1, 1, 7.2, "Erza is great. Contains jaw dropping action scenes");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (1, 2, 5.1, "Seen too many of these movies. They are all the same");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (1, 3, 8.0, "Funny. Pleasure to watch");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (1, 4, 7.3, "Great movie. Definitely recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (2, 5, 7.2, "Great Watch");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (2, 6, 6.8, "Prefer Christopher Reeves. Superman isn't trusted in movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (2, 3, 8.0, "Definitely recommend");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (3, 5, 8.9, "Great Watch but too long");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (3, 6, 8.1, "My favourite superhero movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (3, 7, 8.2, "Definitely recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (3, 4, 8.0, "Recommend");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (4, 2, 5.1, "Slow and boring");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (4, 4, 4.1, "Don't waste your time");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (5, 7, 7.2, "I loved it");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (5, 4, 8.2, "Definitely recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (5, 8, 4.3, "No Thank you");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (5, 9, 3.1, "Worst Animation I have seen so far");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (6, 10, 7.2, "Definitely recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (6, 8, 7.3, "Must see");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (6, 9, 8.1, "Loved it");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (7, 10, 9.1, "Classic. Even for today");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (7, 4, 9.8, "Never get bored watching this");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (8, 11, 7.1, "Even now it is still good");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (8, 10, 7.1, "Good Crime movie");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (9, 12, 4.2, "Don't bother");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (8, 13, 3.1, "Didn't watch all of it because it was a drag");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (10, 6, 6.1, "OK");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (10, 8, 5.0, "Don't bother");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (10, 13, 6.8, "Funny");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (11, 14, 6.4, "Worth a watch");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (11, 12, 6.1, "I love romantic Comedies");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (11, 9, 6.2, "Better than I thought");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (13, 15, 5.1, "Even with Ben Affleck movie is dull");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (13, 9, 4.29, "Wierd movie");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (15, 5, 6.3, "Sequel even better");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (15, 2, 6.0, "Prefer the original");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (15, 3, 6.6, "Could have been better");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (15, 8, 7.39, "Always like these kind of movies");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (16, 16, 5.0, "Dissapointing");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (16, 10, 4.9, "Better horror movies out there");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (16, 7, 5.1, "Not scary at all");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (17, 17, 3.31, "Absolute lame movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (17, 18, 3.3, "Cannot recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (17, 6, 4.2, "Low budget scenes and dissapointing plot");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (17, 5, 4.1, "Scary but boring as well");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (18, 19, 6.31, "Watchable");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (18, 20, 5.7, "Cannot recommend");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (18, 18, 5.9, "Pyschological movie with a difference");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (18, 3, 4.7, "This is not my cup of tea");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (19, 21, 3.3, "Seen too many movies");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (19, 22, 2.2, "One of the worst movies I have seen");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (20, 22, 5.0, "Movie plays with your mind");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (22, 22, 5.2, "It is not bad");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (22, 11, 4.3, "Waste of time");



insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (23, 23, 6.2, "I like it");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (23, 24, 6.3, "I don't usually watch Romantic movies but this was OK");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (25, 25, 6.3, "Cage is always good Actor. He stars in this exciting Western Drama");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (26, 26, 4.3, "I didn't like it");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (26, 27, 3.3, "Slow and for a Western it is very badly written");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (27, 3, 8.8, "Best Sci-Fi Franchise");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (27, 2, 8.7, "Never forget this. I will always be a fan");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (27, 1, 8.9, "Brilliant");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (27, 23, 7.7, "This is the best movie in the whole franchise");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (27, 21, 8.3, "Imagine they use the special effects available now then this would be even better");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (28, 9, 9.2, "Classic Sci-Fi");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (28, 11, 9.0, "Great Plot and movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (28, 12, 9.2, "Old classic. I even watch even today");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (28, 19, 8.3, "Wastch when I was a kid and I am still a big fan");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (29, 13, 8.2, "I like it");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (29, 14, 8.3, "Lovely");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (29, 19, 9.3, "Great. But the sequel franchise is not as good and the ideas were copied. They can never match Lucas");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (29, 12, 8.43, "Star wars and may the force be with us");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (29, 17, 9.3, "Excellent");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (30, 28, 8.3, "Was never a Transformer fan until now");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (30, 29, 7.0, "Give it a 7 because too much violence but overall good movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (30, 8, 8.0, "Amazing fight scenes and special effects");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (30, 9, 8.2, "Must watch");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 10, 7.8, "Best Transformers movie so far");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 12, 8.4, "I loved it");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 11, 8.2, "Great movie");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 4, 9.0, "Great. I am a fan of the whole franchise so far");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 2, 8.73, "Great sequel to an excellent franchise so far");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (31, 5, 7.9, "Excellent");

insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (33, 30, 5.8, "Watchable");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (33, 29, 4.9, "Started well then plot drifted");
insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (33, 11, 6.1, "Was surprised");