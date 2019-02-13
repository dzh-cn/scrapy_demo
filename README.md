## run script
    scrapy crawl douban_movie

## init sql
    create table movie_top_250
    ( enterprise_id bigint primary key auto_increment comment '主键',
      url varchar(100) comment 'url',
      number varchar(100) comment 'number',
      name varchar(100) comment 'name',
      time varchar(100) comment 'time',
      director varchar(100) comment 'director',
      scenario varchar(100) comment 'scenario',
      starts varchar(100) comment 'starts',
      type varchar(100) comment 'type',
      district varchar(100) comment 'district',
      language varchar(100) comment 'language',
      time_desc varchar(100) comment 'time_desc',
      created_date datetime not null default current_timestamp comment '创建时间',
      modified_date datetime not null default current_timestamp on update current_timestamp comment '最后修改时间'
    )engine=innodb  default charset=utf8 collate=utf8_bin comment 'movie top 250';
