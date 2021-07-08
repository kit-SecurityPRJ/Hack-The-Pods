create table if not exists users (
	`id`   		int auto_increment primary key unique,
	`name` 		varchar(50) not null,
	`gender` 	varchar(128) not null
) default CHARSET=utf8 COLLATE=utf8_bin;

insert into users (name, gender) values ("HideMan", "htp-ctf{SQL_INJECTION_is_rudimentary_but_very_DANGEROUS}");
insert into users (name, gender) values ("Alexandra", "female");
insert into users (name, gender) values ("Alice", "female");
insert into users (name, gender) values ("Charles", "male");
insert into users (name, gender) values ("David", "male");
insert into users (name, gender) values ("Emma", "female");
insert into users (name, gender) values ("Eric", "male");
insert into users (name, gender) values ("Gilbert", "male");
insert into users (name, gender) values ("Henry", "male");
insert into users (name, gender) values ("Isaac", "male");
insert into users (name, gender) values ("Jane", "female");
insert into users (name, gender) values ("Margaret", "female");
insert into users (name, gender) values ("Mary", "female");
insert into users (name, gender) values ("Nick", "male");
insert into users (name, gender) values ("Peter", "male");
insert into users (name, gender) values ("Patricia", "female");
insert into users (name, gender) values ("Philip", "male");
insert into users (name, gender) values ("Raymond", "male");
insert into users (name, gender) values ("Rebecca", "female");
insert into users (name, gender) values ("Richard", "male");
insert into users (name, gender) values ("Steven", "male");
insert into users (name, gender) values ("Tiffany", "female");
insert into users (name, gender) values ("Tomas", "male");
insert into users (name, gender) values ("Victoria", "female");
insert into users (name, gender) values ("William", "male");

revoke all privileges on injection.* from inject;
grant select on injection.* to inject;
