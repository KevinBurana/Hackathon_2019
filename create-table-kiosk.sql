/*
Devin, Kevin, Brandon and Brandon
4/13/19

Purpose:
Create table for the Kiosk systems
*/

drop table hsu_kiosk;

create table hsu_kiosk
(
	machine_name varchar2(20) NOT NULL,
	machine_status char(1)    NOT NULL, 
	CHECK (machine_status in ('g', 'b', 'r')),
	primary key(machine_name)
);
	