drop table if exists t_developer_info;

create table t_developer_info
(
	id		int unsigned not null auto_increment,
	developer	varchar(200),
	telephone	varchar(20),
	email		varchar(200),
	app_key		varchar(100),
	primary key (id)
);
