CREATE TABLE "suicide" (
    "country"       TEXT        NOT NULL,
    "suicide_rate"  NUMERIC     NOT NULL,
    FOREIGN KEY (country) REFERENCES fifa (country)
);

CREATE TABLE "freedom" (
    "country"           TEXT        NOT NULL,
    "freedom_score"     NUMERIC     NOT NULL,
    "freedom_rank"      NUMERIC     NOT NULL,
    FOREIGN KEY (country) REFERENCES fifa (country)
);

CREATE TABLE "happiness" (
    "country"           TEXT        NOT NULL,
    "happiness_rank"    NUMERIC     NOT NULL,
    "happiness_score"   NUMERIC     NOT NULL,
    FOREIGN KEY (country) REFERENCES fifa (country)
);

CREATE TABLE "fifa" (
    "fifa_rank"             NUMERIC     NOT NULL,
    "country"               TEXT        NOT NULL,
    "total_points"          NUMERIC     NOT NULL,
    "cur_year_avg"          NUMERIC     NOT NULL,
    "cur_year_avg_weighted" NUMERIC     NOT NULL,
    "rank_date"             DATE        NOT NULL,
    PRIMARY KEY (country)
);