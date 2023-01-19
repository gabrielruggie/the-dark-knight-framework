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

CREATE TABLE transaction (
    id int NOT NULL,
    first_name character varying (50) NOT NULL,
    last_name character varying (50) NOT NULL,
    amount int NOT NULL,
    transaction_date character varying (128) NOT NULL,
    transaction_time character varying (128) NOT NULL,
    stripe_payer_id character varying (255) NOT NULL,
    physical int NOT NULL,
    verified int NOT NULL, 
    archived int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE team (
    id int NOT NULL,
    church character varying (50) NOT NULL,
    school_level int NOT NULL,
    cap_last_name character varying (255) NOT NULL,
    wins int NOT NULL,
    losses int NOT NULL,
    total_pts int NOT NULL,
    pts_allowed int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE player (
    -- PLAYER NUMBER + TEAM ID
    id character varying (128) NOT NULL,
    first_name character varying (50) NOT NULL,
    last_name character varying (50) NOT NULL,
    --email character varying (255) NOT NULL,
    --position character varying (50) NOT NULL,
    player_number int NOT NULL,
    --grade int NOT NULL,
    --is_team_captain int NOT NULL,
    team_church character varying (50) NOT NULL,
    team_cap_name character varying (50) NOT NULL,
    team_level int NOT NULL,
    team_id int NOT NULL,
    ppg character varying (50) NOT NULL,
    apg character varying (50) NOT NULL,
    rpg character varying (50) NOT NULL,
    spg character varying (50) NOT NULL,
    bpg character varying (50) NOT NULL,
    tot_points int NOT NULL,
    tot_assists int NOT NULL,
    tot_rebounds int NOT NULL,
    tot_steals int NOT NULL,
    tot_blocks int NOT NULL,
    games_played int NOT NULL,
    PRIMARY KEY (id)
);