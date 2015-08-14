drop table if exists t_service_monitor;

create table t_service_monitor
(
	id		int unsigned not null auto_increment,
	service_name	varchar(50),
	service_ip	varchar(20),
	service_port	int,
	service_status	varchar(20),
	notice_developers	varchar(255),
	last_report_timestamp	timestamp,
	primary key (id)
);

