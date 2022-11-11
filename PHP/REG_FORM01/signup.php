<?php
   require "includes/db.php";

   $data = $_POST;
   if(isset($data['do_signup']))
   {
    // reg
    $errors = array();
    if( trim($data['login']) == '' )
    {
        // логин пустой
        $errors[] = 'Введите логин';
    }

    if( trim($data['email']) == '' )
    {
        // email пустой
        $errors[] = 'Введите email';
    }

    if( $data['password'] == '' )
    {
        // password пустой
        $errors[] = 'Введите password';
    }

    if( $data['password_2'] != $data['password'] )
    {
        // совпадение паролей
        $errors[] = 'Пароли не совпадают!!!';
    }

    if( R::count('users', "email = ?", array($data['email'])) > 0 )
    {
        // совпадающие емаил
        $errors[] = 'Пользователь с таким email уже существует!!!';
    }

    if( R::count('users', "login = ?", array($data['login'])) > 0 )
    {
        // совпадающие логин
        $errors[] = 'Пользователь с таким login уже существует!!!';
    }

    if( empty($errors) )
    {
        // Всё хорошо - регистрируем
        $user = R::dispense( 'users' );
        $user->login = $data['login'];
        $user->email = $data['email'];
        $user->password = password_hash($data['password'], PASSWORD_DEFAULT);
        $user->join_date = date('Y-m-d H:i:s');
        R::store($user);
        
        echo '<div style="color:green;">Вы успешно зарегистрированы!</div><hr>'; // нужно убирать сообщение через 5 секунд и очищать формы

    } else
    {
        echo '<div style="color:red;">'.array_shift($errors).'</div><hr>';
    }
   }

   //echo 'Сейчас:           '. date('Y-m-d H:i:s') ."\n";
   
?>

<form action="/signup.php" method="POST">

<p>
    <p><strong>Ваш логин</strong>:</p>
    <input type="text" name="login" value="<?php echo @$data['login'] ?>">
</p>

<p>
    <p><strong>Ваш Email</strong>:</p>
    <input type="email" name="email" value="<?php echo @$data['email'] ?>">
</p>

<p>
    <p><strong>Ваш пароль</strong>:</p>
    <input type="password" name="password" value="<?php echo @$data['password'] ?>">
</p>

<p>
    <p><strong>Введите ваш пароль ещё раз</strong>:</p>
    <input type="password" name="password_2" value="<?php echo @$data['password_2'] ?>">
</p>

<p>
    <button type="submit" name="do_signup">Зарегистрироваться</button>
</p>

</form>
