
<script src="http://www.buzzntravel.com/js/jquery.min.1.8.2.js">
<script type="text/javascript" charset="utf-8">

$(function(){
alert('wow')
});

function callajax(){
ch =$("#choice").val();
alert(ch);
}
</script>
<?php
$output = shell_exec('/usr/bin/python /home/pi/gitProjects/pythonExecutable/musicPlay');
echo "<pre>$output</pre>";
?>
<?php
session_write_close();
function pe($val){ echo '<pre>';print_r($val);}

if($_POST){
    if($_POST['killSong']){
        echo "Song Stopped ";
        $output=shell_exec("/usr/bin/python /home/pi/gitProjects/pythonExecutable/play.py");
        pe($output);
        $output=shell_exec("/usr/bin/sudo /usr/bin/bash /home/pi/gitProjects/shellscripts/killomx");
        pe($output);
    }elseif ($_POST['selectSong'] && $_POST['choice'] ) {
        $ch = $_POST['choice'];
        echo "sound Played ".$ch;
        echo $scmd = '/usr/bin/python /home/pi/gitProjects/pythonExecutable/play.py --number '.$ch;
        $output = shell_exec($scmd);
        pe($output);
    } elseif ($_POST['selectSong'] && !$_POST['choice'] ) {
        echo '<h1> Select Song </h1>';
    }
}


?>
<form method="post">
    <input type="text" name="choice" id="choice">
    <input type="submit" id="selectSong" name="selectSong" value="PlaySong" onclick="callajax()">
    <input type="submit" name="killSong" value="KillMusic">
</form>
            <div id="div1"></div>
