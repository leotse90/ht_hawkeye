drop table if exists t_web_monitor;

create table t_web_monitor
(
	id			int unsigned not null auto_increment,
	url_name		varchar(50),
	url			text,
	url_status		varchar(20),
	url_status_code		int,
	notice_developers	varchar(255),
	last_report_timestamp	timestamp,
	primary key (id)
);
