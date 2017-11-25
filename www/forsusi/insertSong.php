<?php function pe($val){ echo '<pre>'; print_r($val); exit(); } ?>
<?php function p($val){ echo '<pre>'; print_r($val); } ?>
<script src="http://www.buzzntravel.com/js/jquery.min.1.8.2.js">
<script type="text/javascript" charset="utf-8">

</script>
<?php
function connection(){
    $servername = "localhost";
    $username = "root";
    $password = "";

    // Create connection
    $conn = new mysqli($servername, $username, $password,"susi");

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
    echo "Connected successfully";
}
$conn = connection();
if(!empty($_POST)){
    $song   = !empty($_POST['url'])?$_POST['url']:'';
    $title  = !empty($_POST['title'])?$_POST['title']:'';
    if(!empty($song) && !empty($title)){
        $sql = "SELECT song FROM songlist where song ='$song'";
        $result = $conn->query($sql);
        if($result->num_rows == 0){
            $sql    = "INSERT INTO songlist (song,title) VALUES ('$song','$title')";
            if ($conn->query($sql) === TRUE) {
                echo "New record created successfully";
            } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
            }            
        }else{
            echo 'Alreay exits';
        }        
    }
    
}
?>
<?php

?>
<form method="post">
    <input type="text" name="url" id="url">
    <input type="text" name="title" id="title">
    <input type="submit" id="addsong" name="addsong" Value="Add Song">   
</form>            
