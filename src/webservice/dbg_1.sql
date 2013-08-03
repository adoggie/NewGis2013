--delete from giscore_ao_alarmactionlog;
--delete from giscore_ao_alarmlog;
select * from giscore_ao_alarmlog order by time desc;
select * from giscore_ao_alarmactionlog order by time desc;