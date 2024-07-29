<?php
session_start();

// Mostrar errores
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include 'conexion.php';

if (isset($_POST['login'])) {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Preparar la consulta para evitar inyecciones SQL
    $consulta = $conex->prepare("SELECT password FROM datos WHERE username = ?");
    $consulta->bind_param("s", $username);
    $consulta->execute();
    $consulta->store_result();
    $consulta->bind_result($hashed_password);

    if ($consulta->num_rows > 0) {
        $consulta->fetch();

        // Verificar la contraseña
        if (password_verify($password, $hashed_password)) {
            $_SESSION['username'] = $username;
            header("Location: dashboard.php"); // Redirigir a la página del dashboard
            exit();
        } else {
            $error = "¡Nombre de usuario o contraseña incorrectos!";
        }
    } else {
        $error = "¡Nombre de usuario o contraseña incorrectos!";
    }

    $consulta->close();
}
?>
