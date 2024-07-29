<?php 
// Detalles de la conexión
$servername = "sql300.infinityfree.com";
$username = "if0_36990074";
$password = "ErosvXDaEh";
$dbname = "if0_36990074_registro";

// Crear la conexión
$conex = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conex->connect_error) {
    die("Conexión fallida: " . $conex->connect_error);
}
?>
