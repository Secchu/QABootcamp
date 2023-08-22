USE QABootcamp;

create table movies (
	Movie_ID int primary key auto_increment,
    Movie_Title varchar(100) not null,
    Duration int not null
);

create table directors(
	Director_ID int primary key auto_increment,
    Director_Name varchar(100) not null
);

create table reviewers(
	Reviewer_ID int primary key auto_increment,
    Reviewer_Name varchar(100) not null,
    city varchar(100)
);

create table Writers(
	Writer_ID int primary key auto_increment,
    Writer_Name varchar(100) not null
);

create table MovieStars(
	Star_ID int primary key auto_increment,
    Star_Name varchar(100) not null
);

create table Genre
(
    Category_ID int primary key auto_increment,
    Category_Name varchar(100) not null
);

create table CategorizedMovie(
	FKMovie_ID int not null,
    FKCategory_ID int not null,
	FOREIGN KEY (FKMovie_ID) REFERENCES Movies(Movie_ID),
    FOREIGN KEY (FKCategory_ID) REFERENCES Genre(Category_ID),
    primary key(FKMovie_ID, FKCategory_ID)
);

create table MovieCast (
	FKMovie_ID int not null,
    FKStar_ID int not null,
    PRIMARY KEY (FKMovie_ID, FKStar_ID),
    FOREIGN KEY (FKMovie_ID) REFERENCES Movies(Movie_ID),
    FOREIGN KEY (FKStar_ID) REFERENCES MovieStars(Star_ID)
);

create table MovieScript(
	FKMovie_ID int not null,
	FKWriter_ID int not null,
    PRIMARY KEY (FKMovie_ID, FKWriter_ID),
    FOREIGN KEY (FKMovie_ID) REFERENCES Movies(Movie_ID),
    FOREIGN KEY (FKWriter_ID) REFERENCES Writers(Writer_ID)
);

create table DirectedMovies(
	FKMovie_ID int not null,
	FKDirector_ID int not null,
    PRIMARY KEY (FKMovie_ID, FKDirector_ID),
    FOREIGN KEY (FKMovie_ID) REFERENCES Movies(Movie_ID),
    FOREIGN KEY (FKDirector_ID) REFERENCES directors(Director_ID)
);

create table ratings(
	FKMovie_ID int not null,
    FKReviewer_ID int not null,
    Rating float,
	Review varchar(1000),
    PRIMARY KEY (FKMovie_ID, FKReviewer_ID),
    FOREIGN KEY (FKMovie_ID) REFERENCES Movies(Movie_ID),
    FOREIGN KEY (FKReviewer_ID) REFERENCES reviewers(Reviewer_ID)
);

