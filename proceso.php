<?php
include("conexion.php");

// Decodificamos el JSON enviado por POST
$discos = json_decode($_POST['discos'], true);

// Obtenemos el serial de la máquina
$serial = $_POST['serial'];

// Recorremos la lista de discos e insertamos cada uno en la base de datos
foreach ($discos as $disco) {
  $unidad = mysqli_real_escape_string($conn, $disco['mountpoint']);
  $capacidad = mysqli_real_escape_string($conn, $disco['capacity']);
  
  $sql = "INSERT INTO disco (punto_control, Capacidad, id_serial) VALUES ('$unidad', '$capacidad', '$serial')";
  if ($conn->query($sql) === TRUE) {
    echo "Datos guardados correctamente";
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }
}

// Cerramos la conexión con la base de datos
mysqli_close($conn);

?>

