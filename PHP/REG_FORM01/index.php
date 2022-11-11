<?php
//echo "<h1>Hellooo WORLD!!!!";

require "includes/db.php";

//require "x.php";
?>

<?php if( isset($_SESSION['logged_user']) ) : ?>
    Авторизован!<br>
    Привет, <?php echo $_SESSION['logged_user']->login; ?>!
    <hr>
    <a href="logout.php">Выйти</a>

<?php else : ?>
<a href="login.php">Авторизоваться</a><br>
<a href="signup.php">Зарегистрироваться</a><br>
<br>
<a href="x.php">Инфо</a>
<?php endif; ?>