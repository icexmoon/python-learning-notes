<?php
require_once(".\\ContextInterface.php");
class MyDB implements ContextInterface
{
    private $dbConnect;
    private $dbConfig;
    function __construct()
    {
        $this->dbConfig = array(
            'db' => 'myweb',
            'servername' => '127.0.0.1',
            'username' => 'root',
            'password' => ''
        );
    }
    public function enter()
    {
        $this->dbConnect = mysqli_connect($this->dbConfig['servername'],
                                             $this->dbConfig['username'], 
                                             $this->dbConfig['password'],
                                            $this->dbConfig['db']);
        // mysql_select_db($this->dbConfig['db'], $this->dbConnect);
        return $this->dbConnect;
    }
    public function exit()
    {
        mysqli_close($this->dbConnect);
    }
}
