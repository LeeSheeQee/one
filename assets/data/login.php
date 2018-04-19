<?php
$uid = $_POST["uid"];
$pwd = $_POST["pwd"];

//造连接对象
$db = new MySQLi("localhost","root","123","mydb");

//写SQL语句
//SQL注入攻击

$sql = "select password from login where username='{$uid}'";


//执行SQL语句
$reslut = $db->query($sql);

$n = $reslut->fetch_row();

if($uid!="" && $pwd !="" )
{
    if($n[0]==$pwd)
    {
        header("location:main.php");
    }
    else
    {
        echo "用户名或密码错误！";
    }
}
else
{
    echo "用户名密码不能为空";
}
?>
