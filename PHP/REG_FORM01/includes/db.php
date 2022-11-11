<?php

require "libs/rb.php";

//try{
//    $db = new PDO('mysql:host=localhost;dbname=REG_Form01_DB','ax01','P455-mySQL#ax01555');
//} catch(PDOException $e){
//    echo $e->getmessage();
//}

R::setup( 'mysql:host=localhost;dbname=REG_Form01_DB',
        'ax01', 'P455-mySQL#ax01555' ); //for both mysql or mariaDB

session_start();

?>

