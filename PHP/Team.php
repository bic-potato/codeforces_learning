<?php
function Matrix($n, $arr) {
    $i = 0;
    while ($i < $n){
        array_push($arr, explode(" ", readline()));
        $i += 1;
    }
    return $arr;
}
$arr1 = array();
Matrix(settype(readline(), "int"), $arr1);
