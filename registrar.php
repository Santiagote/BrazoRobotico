<?php 
include 'conexion.php';

if(isset($_POST['register'])){
    if(
        isset($_POST['username']) && strlen($_POST['username']) >= 1 &&
        isset($_POST['password']) && strlen($_POST['password']) >= 1 &&
        isset($_POST['confirm_password']) && strlen($_POST['confirm_password']) >= 1 
        ){
             $usuario = trim($_POST['username']);
             $contraseña = trim($_POST['password']);  
             $confirmacion_contraseña = trim($_POST['confirm_password']);       
             
             // Verificar que las contraseñas coincidan
             if ($contraseña === $confirmacion_contraseña) {
                 // Preparar la consulta para evitar inyecciones SQL
                 $consulta = $conex->prepare("INSERT INTO datos (username, password) VALUES (?, ?)");
                 $consulta->bind_param("ss", $usuario, $contraseña);
                 
                 $resultado = $consulta->execute();

                 if($resultado){
                     echo '<h3 class="succes">¡Te has registrado correctamente!</h3>';
                     echo '<a href="index.html" class="btn btn-primary mt-3">Regresar al inicio</a>';
                 } else {
                     echo '<h3 class="error">¡Ha ocurrido un error!</h3>';
                 }
             } else {
                 echo '<h3 class="error">¡Las contraseñas no coinciden!</h3>';
             }
        } else {    
            echo '<h3 class="error">¡Por favor complete los campos!</h3>';
        }
}
?>
