<?php
/*echo $_POST["framework"];
echo '<br />'
echo $_POST["hidden_framewokr"];*/

$connect = mysqli_connect("localhost", "root", "", "testing");
$query = "INSERT INTO like_table(framework) VALUES ('".$_POST["hidden_framework
"]."')";

if (mysqli_query($connect, $query))
{
  echo 'Data Inserted';
}
?>
