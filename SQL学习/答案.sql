##第一题
select regionname, sum(orderamount)
from orderinfo left join regioninfo on province = regionid
group by province
order by sum(orderamount) desc
limit 10;

##第二题
select username, gender,sum(orderamount)
from orderinfo left join userinfo on orderinfo.userid = userinfo.userid
group by orderinfo.userid
order by sum(orderamount) desc
limit 10;


##第三题
create table gdb(select regionname as区县名称, city as 城市id,sum(orderamount) as金额from orderinfo left join regioninfo on district = regionid
group by district
order by sum(orderamount) desc
limit 10);
 
select 区县名称,regionname as 城市名称, 金额
from gdb left join regioninfo on 城市id = regionid;
