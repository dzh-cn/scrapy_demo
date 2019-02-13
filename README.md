## run script
    scrapy crawl douban_movie

## init sql
    create table douban_movie
    ( enterprise_id bigint primary key auto_increment comment '主键',
      name varchar(100) comment 'name',
      name_desc varchar(100) comment 'name_desc',
      stars varchar(100) comment 'stars',
      rating varchar(100) comment 'rating',
      rater_count varchar(100) comment 'rater_count',
      created_date datetime not null default current_timestamp comment '创建时间',
      modified_date datetime not null default current_timestamp on update current_timestamp comment '最后修改时间'
    )engine=innodb  default charset=utf8 collate=utf8_bin comment '将贷方企业实体信息';
