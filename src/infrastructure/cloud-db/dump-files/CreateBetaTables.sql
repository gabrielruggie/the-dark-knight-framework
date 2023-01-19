CREATE TABLE admin (
    id character varying(255) NOT NULL,
    login_id int NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    username character varying(128) NOT NULL,
    email character varying(255) NOT NULL,
    hashed_password character varying(255) NOT NULL,
    position character varying(50) NOT NULL,
    astack_right_level int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE team (
    id int NOT NULL,
    team_name character varying (255) NOT NULL,
    church character varying (50) NOT NULL,
    school_level int NOT NULL,
    cap_last_name character varying (255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE player (
    id character varying (128) NOT NULL,
    first_name character varying (50) NOT NULL,
    last_name character varying (50) NOT NULL,
    player_number int NOT NULL,
    team_church character varying (50) NOT NULL,
    team_cap_name character varying (50) NOT NULL,
    team_level int NOT NULL,
    team_id int NOT NULL,
    tot_points int NOT NULL,
    tot_assists int NOT NULL,
    tot_rebounds int NOT NULL,
    tot_steals int NOT NULL,
    tot_blocks int NOT NULL,
    games_played int NOT NULL,
    PRIMARY KEY (id)
);