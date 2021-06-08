<?php
function changeNum(&$a){
    $a = 2;
}
$a = 1;
changeNum($a);
echo $a;
// 2