<?php
settype($input = readline(), 'int');
if ($input % 2 == 0 and $input != 2)
{
    print("YES");
}
else{
    print "NO";
}
?>