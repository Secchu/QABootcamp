CREATE TABLE movie (
        "Movie_ID" INTEGER NOT NULL,
        "Movie_Title" VARCHAR(100) NOT NULL,
        "Duration" INTEGER NOT NULL,
        "Year" INTEGER NOT NULL,
        PRIMARY KEY ("Movie_ID")
);
CREATE TABLE director (
        "Director_ID" INTEGER NOT NULL,
        "Director_Name" VARCHAR(100) NOT NULL,
        PRIMARY KEY ("Director_ID")
);
CREATE TABLE writer (
        "Writer_ID" INTEGER NOT NULL,
        "Writer_Name" VARCHAR(100) NOT NULL,
        PRIMARY KEY ("Writer_ID")
);
CREATE TABLE moviestar (
        "Star_ID" INTEGER NOT NULL,
        "Star_Name" VARCHAR(100) NOT NULL,
        PRIMARY KEY ("Star_ID")
);
CREATE TABLE IF NOT EXISTS "CategorizedMovie" (
        "Movie_ID" INTEGER,
        "Category_ID" INTEGER,
        FOREIGN KEY("Movie_ID") REFERENCES movie ("Movie_ID"),
        FOREIGN KEY("Category_ID") REFERENCES genre ("Category_ID")
);
CREATE TABLE IF NOT EXISTS "MovieCast" (
        "Movie_ID" INTEGER,
        "Star_ID" INTEGER,
        FOREIGN KEY("Movie_ID") REFERENCES movie ("Movie_ID"),
        FOREIGN KEY("Star_ID") REFERENCES moviestar ("Star_ID")
);
CREATE TABLE IF NOT EXISTS "MovieScript" (
        "Movie_ID" INTEGER,
        "Writer_ID" INTEGER,
        FOREIGN KEY("Movie_ID") REFERENCES movie ("Movie_ID"),
        FOREIGN KEY("Writer_ID") REFERENCES writer ("Writer_ID")
);
CREATE TABLE IF NOT EXISTS "DirectedMovies" (
        "Movie_ID" INTEGER,
        "Director_ID" INTEGER,
        FOREIGN KEY("Movie_ID") REFERENCES movie ("Movie_ID"),
        FOREIGN KEY("Director_ID") REFERENCES director ("Director_ID")
);
CREATE TABLE review (
        "Reviewer_ID" INTEGER NOT NULL,
        "Reviewer_Name" VARCHAR(100) NOT NULL,
        "City" VARCHAR(100) NOT NULL,
        "Review" TEXT NOT NULL,
        "Rating" FLOAT NOT NULL,
        "Movie_ID" INTEGER,
        PRIMARY KEY ("Reviewer_ID"),
        FOREIGN KEY("Movie_ID") REFERENCES movie ("Movie_ID")
);
CREATE TABLE genre (Category_ID INTEGER NOT NULL, Category_Name VARCHAR (100) NOT NULL UNIQUE, PRIMARY KEY (Category_ID));