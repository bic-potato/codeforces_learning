<?php
function MainArgs() {
    $str1 = readline();
    $arr1 = str_split($str1);
    $len = count($arr1);
    if ($len > 10 )
    {
        $mid = $len - 2;
        echo("{$arr1[0]}{$mid}{$arr1[$len - 1]}");
        print("\n");
    }
    else {
        print($str1);
        print("\n");
    }
}
settype($n = readline(), "int");
$i = 0;
while ($i < $n) {
    MainArgs();
    $i += 1;
}
?>