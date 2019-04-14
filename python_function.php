<?php
	require_once("hsu_connection.php");
	
	function Python_Bad_Kiosk($name)
	{
		$username = "bjm23";
		$password = "Asdfasdf12345";		

		$connection = hsu_conn($username, $password);

		$statement = "BEGIN kiosk_update(:nm, 'b'); END;";

		$call = oci_parse($connection, $statement);
		oci_bind_by_name($call, ":nm", $name);
		
		oci_execute($call, OCI_DEFAULT);
		oci_free_statement($call);
		oci_close($connection);

		?>
		This function Finished!
		<?php
	}
	
	Python_Bad_Kiosk($_GET["name"]);
?>