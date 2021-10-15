<html>
    <form id="array-input" method="post" name="form" action="">
        <label for="key1">Key1:</lable>
        <input type="text" id="key1" value="4" name="key1"></input><br>
        <label for="value1">Value1:</lable>
        <input type="text" id="value1" value="white" name="value1"></input><br>

        <label for="key2">Key2:</lable>
        <input type="text" id="key2" name="key2" value="6"></input><br>
        <label for="value2">Value2:</lable>
        <input type="text" id="value2" name="value2" value="green"></input><br>

        <label for="key3">Key3:</lable>
        <input type="text" id="key3" name="key3" value="11"></input><br>
        <label for="value3">Value3:</lable>
        <input type="text" id="value3" name="value3" value="red"></input><br>

        <button type="submit" name="ok">Submit</button> <br>
</form>
<?php
    if(isset($_POST['ok'])) {
        $array = array( $_POST['key1'] => $_POST['value1'], $_POST['key2'] => $_POST['value2'], $_POST['key3'] => $_POST['value3']);
    #var_dump($array);
        echo 'First Element ' . $array[array_key_first($array)] . "\n";
    }
?>
</html>