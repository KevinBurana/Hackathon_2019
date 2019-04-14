/*
Devin, Kevin, Brandon and Brandon
4/13/19

Purpose:
creates a function that updates the hsu_kiosk table
for status changes
*/


CREATE OR REPLACE procedure repair_done(kiosk varchar2) as
begin
	UPDATE hsu_kiosk
	SET    machine_status = 'g'
	WHERE  machine_name = kiosk;

	commit;
end;
/
show errors