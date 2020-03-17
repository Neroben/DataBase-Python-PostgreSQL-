create database HockeyLiga;

create table Confederacy{
	confederacy_id serial primary key,
	name VARCHAR(50) not null
};

create table Club{
	club_id serial primary key,
	name VARCHAR(50) not null,
	rating int,
	confederacy_id int references confederacy(confederacy_id) on delete no action on update cascade
};

create table Sponsor{
	sponsor_id serial primary key,
	name VARCHAR(50) not null
};

create table Match{
	match_id serial primary key,
	playdata timestamp with timezone,
	count1 int not null,
	club_id1 int references club(club_id) on delete no action on update cascade,
	count2 int not null,
	club_id2 int references club(club_id) on delete no action on update cascade,
	sold int not null
};

create table Coach{
	coach_id serial primary key,
	club_id int references club(club_id) on delete no action on update cascade,
	name VARCHAR(50) not null,
	lastname VARCHAR(50) not null
};

create table Player{
	player_id serial primary key,
	club_id int references club(club_id) on delete no action on update cascade,
	name VARCHAR(50) not null,
	lastname VARCHAR(50) not null,
	efficiency int
};