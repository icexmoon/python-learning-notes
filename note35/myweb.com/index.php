<?php
header("Access-Control-Allow-Origin:*");
header("Access-Control-Allow-Credentials:true");
$name = isset($_GET['name']) ? $_GET['name'] : '';
$people = array(
    'Han Meimei' => array(
        'name' => 'Han Meimei',
        'age' => '20',
        'career' => 'student',
        'picture' => 'http://myweb.com/images/1.jpg'
    ),
    'Brus Lee' => array(
        'name' => 'Brus Lee',
        'age' => '30',
        'career' => 'engineer',
        'picture' => 'http://myweb.com/images/2.png'
    ),
    'Jack Chen' => array(
        'name' => 'Jack Chen',
        'age' => '50',
        'career' => 'actor',
        'picture' => 'http://myweb.com/images/3.png'
    )
);
$result = array('status' => 'success', 'result' => array());
if (array_key_exists($name, $people)) {
    $result['result'] = $people[$name];
} else {
    $result['status'] = 'fail';
}
sleep(10);
header('Content-Type:application/json; charset=utf-8');
echo json_encode($result);
