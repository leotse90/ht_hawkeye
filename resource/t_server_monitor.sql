drop table if exists t_server_monitor;

create table t_server_monitor
(
	id		int unsigned not null auto_increment,
	server_name	varchar(50),
	server_ip	varchar(20),
	server_status	varchar(20),
	server_symptom	text,
	notice_developers	varchar(255),
	last_report_timestamp	timestamp,
	primary key (id)
);
