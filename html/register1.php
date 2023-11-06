<?php

    $username = $_POST['username'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    // connect to database
    $db = new PDO('sqlite:/workspaces/group-project-team47/databases/users.db');

    // how to check to make sure connection was successful?
    if ($db->connect_error) {
        echo "Failed connection";
        die("Failed connection: " .$db->connect_error);

    } else {
        // insert values into database
        $stmt = $db->prepare("INSERT INTO users (username_, password_) values(username_tmp, password_tmp)");
        $stmt->bindParam('username_tmp', $username);
        $stmt->bindParam('password_tmp', $password);

        $stmt->execute();
        echo "Registration successful";
        
        $stmt->close();
        $db->close();
    }

    


?>