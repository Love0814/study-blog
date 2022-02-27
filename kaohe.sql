create database kaohe;

use kaohe;

create table UserInfo(
	userid varchar(20) not null default'-',
    username varchar(20) not null default'-',
    gender varchar(4) not null default'-'
    );
    
load data local infile 'C:\\Users\\cuiha\\Desktop\\test\\data\\userinfo.txt'
	into table UserInfo
    fields terminated by '\t'
    ignore 1 lines;
    
create table RegionInfo(
	regionid varchar(10) not null default'-',
    regionname varchar(20) not null default'-',
    regiontype int not null default'0'
    );
    
load data local infile 'C:\\Users\\cuiha\\Desktop\\test\\data\\regioninfo.txt'
	into table RegionInfo
    fields terminated by '\t'
    ignore 1 lines;
    
create table OrderInfo(
	OrderID varchar(20) not null default'-',
    UsreID varchar(20) not null default'-',
    Country int not null default'0',
    Province int not null default'0',
    City int not null default'0',
    District int null default '0',
    OrderAmount int not null default'0'
    );
    
load data local infile 'C:\\Users\\cuiha\\Desktop\\test\\data\\orderinfo.txt'
	into table OrderInfo
    fields terminated by '\t'
    ignore 1 lines;

select * from orderinfo;
select * from regioninfo;
select * from userinfo;

#求出购买力最强的前十个省份
select regionname as 省,sum(OrderAmount) as 消费额
	from orderinfo left join regioninfo on orderinfo.Province = regioninfo.regionid
    group by 省
    order by 消费额 desc
    limit 10;

#求出购买力最强的前十名顾客以及他们的性别
select username as 顾客名,gender as 性别,sum(OrderAmount) as 消费额
	from orderinfo left join userinfo on orderinfo.UsreID = userinfo.userid
    group by 顾客名
    order by 消费额 desc
    limit 10;

#求出购买力最强的前十个区县以及这些区县所属的城市
create table trans(
	PROVINCEID int not null default'0',
    cityname varchar(20) not null default'-',
    amount int not null default'0'
    );

insert into trans
select Province,regionname as 城市,sum(OrderAmount)
	from orderinfo left join regioninfo on orderinfo.City = regioninfo.regionid
	group by 城市,Province
	order by Province;

select *from trans;
    
select cityname as 城市,regionname as 省,amount as 消费额
	from trans left join regioninfo on trans.PROVINCEID = regioninfo.regionid
    group by 城市,省
    order by 消费额 desc
    limit 10;