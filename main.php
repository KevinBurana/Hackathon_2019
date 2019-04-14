<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

<!--
    by: Brandon Menyes
    last modified: 4-13-19

    you can run this using the URL:
	http://www.nrs-projects.humboldt.edu/~bjm23/Hackathon/main.php
-->

	<head>
		<title> Hackathon </title>
		<meta charset="utf-8" />

		<link href="http://nrs-projects.humboldt.edu/~st10/styles/normalize.css"
			  type="text/css" rel="stylesheet" />

		<link href="http://nrs-projects.humboldt.edu/~bjm23/Hackathon/main.css"
			  type="text/css" rel="stylesheet" />

		<script type="text/javascript" src="main.js"> </script>

		<?php
			ini_set('display_errors', 1);
			error_reporting(E_ALL);

			require_once("hsu_connection.php");
			$username = "bjm23";
			$password = "Asdfasdf12345";
		?>
	</head>

	<body>
		
		<br /><br />
		<h1 id="Header1"> Hackathon Kiosk Button </h1>

		<div id="div_container">
			<div id="div_stations">
				<form method="POST">
					<table>
						<tr>
							<th> Station </th>
							<th> Status </th>
						</tr>

						<?php
						$connection = hsu_conn($username, $password);

						$statement = "select * 
									  from hsu_kiosk";

						$qry = oci_parse($connection, $statement);
						oci_execute($qry, OCI_DEFAULT);
						
						while (oci_fetch($qry))
						{
							$name = oci_result($qry, "MACHINE_NAME");
							$status = oci_result($qry, "MACHINE_STATUS");
							
							?>

							<tr>
								<td id="station_name"> <p class="error_text"> <?= $name ?> </p> </td>

								<?php
								if ($status == 'g')
								{
									?>
									<td class="status_good"> <p name="station" class="error_text"> Working </p> </td>
									<?php
								}else if ($status == 'b')
								{
									?>
									<td class="status_bad"> <button onClick="Clicked_Bad(<?= "'" . $name . "'" ?>)" name="station" class="error_text"> Click To Help </button> </td>
									<?php
								}else
								{
									?>
									<td class="status_repair"> <button onClick="Clicked_Repair(<?= "'" . $name . "'" ?>)" name="station" class="error_text"> Needs Repair </button> </td>
									<?php
								}
								?>
							</tr>

							<?php
						}

						oci_free_statement($qry);
						oci_close($connection);
						?>

					</table>
				</form>
			</div>
		</div>
		
	</body>
</html>