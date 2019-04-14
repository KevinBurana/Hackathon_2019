/*
Devin, Kevin, Brandon and Brandon
4/13/19

Purpose:
creates a function that updates the hsu_kiosk table
for status changes
*/


CREATE OR REPLACE procedure kiosk_update(kiosk varchar2, status char) as
begin
	UPDATE hsu_kiosk
	SET    machine_status = status
	WHERE  machine_name = kiosk;
	

	commit;
end;
/
show errors
