<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "soporte";

// Crear conexión
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Verificar conexión
if (!$conn) {
  die("La conexión falló: " . mysqli_connect_error());
}

// Cerrar conexión
//mysqli_close($conn);
?>