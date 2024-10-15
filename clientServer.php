<?php
    $url = $_POST['url'];
    $output = shell_exec('python2 features_extraction.py ' . $url);
    echo $output;
?>
