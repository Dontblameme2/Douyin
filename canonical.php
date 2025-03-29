<?php
session_start();

// Simpan hash password yang sudah dienkripsi (gunakan hasil password_hash di tempat aman)
define("PASSWORD_HASH", '$2y$10$E9N6/hXIRP9FJgr5JDak0uKOwDpmbEXltjR5DiFDuZwWofPjU6hD.'); // Hash dari '12345'

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST['password'])) {
        if (password_verify($_POST['password'], PASSWORD_HASH)) {
            $_SESSION['loggedin'] = true;
            header("Location: dashboard.php");
            exit();
        } else {
            $error = "Password salah!";
        }
    } else {
        $error = "Password tidak boleh kosong!";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Login</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .login-container {
            text-align: center;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        input[type="password"], button {
            margin-top: 10px;
            padding: 10px;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 5px;
            outline: none;
        }
        button {
            background: black;
            color: white;
            cursor: pointer;
            border: none;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <form action="" method="POST">
            <input type="password" name="password" placeholder="Password" required>
            <br>
            <button type="submit">Login</button>
        </form>
        <?php if (isset($error)) { echo "<p class='error'>" . htmlspecialchars($error) . "</p>"; } ?>
    </div>
</body>
</html>
