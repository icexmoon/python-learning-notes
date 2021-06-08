<?php
require_once ".\\ContextCallable.php";
require_once ".\\MyDB.php";
$mydb = new MyDB();
$sqlExcuter = new class($mydb) extends ContextCallable
{
    protected function action($callBack)
    {
        $dbConn = $callBack;
        $SQL = "SELECT * FROM log";
        $result = mysqli_query($dbConn, $SQL);
        $logs = mysqli_fetch_all($result, MYSQLI_ASSOC);
        mysqli_free_result($result);
        print_r($logs);
    }
};
$sqlExcuter->run();
