<?php
//ini_set("display_errors",true);
//error_reporting(E_ALL);
?>
<script src="http://www.buzzntravel.com/js/jquery.min.1.8.2.js"></script>
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script type="text/javascript" charset="utf-8">
function callSong(ch){
    
}
function callajax(ch){
$("#n"+ch).removeClass("active");
$.ajax({
    url: "musicPlay.php",
    type: 'POST',
    data : {'choice':ch,'ajax':1,'selectSong':1}, 
success: function(result){
    $("#div1").html(result);
}});
}
</script>



<?php
if(!$_POST['ajax']){
    $output = shell_exec('/usr/bin/python /home/pi/gitProjects/pythonExecutable/musicPlay');
    $ll = explode(" => ",$output);
    unset($ll[0]);
    //pe($output);
    //pe($ll);
    
    
}
?>
<?php
session_write_close();
function pe($val){ echo '<pre>';print_r($val);}

if($_POST){
    if($_POST['killSong']){
        echo "Song Stopped ";
        $output=shell_exec("/usr/bin/python /home/pi/gitProjects/pythonExecutable/play.py");
        //pe($output);
        $output=shell_exec("/usr/bin/sudo /usr/bin/bash /home/pi/gitProjects/shellscripts/killomx");
        //pe($output);
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
    <?php /*<input type="text" name="choice" id="choice">
    <input type="button" id="selectSong" name="selectSong" value="PlaySong" onclick="callajax()"> */ ?>
    <input type="submit" name="killSong" value="KillMusic" class="btn btn-large btn-warning">
    <input type="submit" name="random" value="Random" class="btn btn-large btn-warning">
</form>
<div id="div1">
    
</div>


<div class="listSong">
    <ul class="list-group" >
        <?php foreach ($ll as $key => $val) { 
            $val = substr($val,0,-1);
            $val = str_replace("Make you choice","N/A",$val);
            $val = str_replace("Enter Choice","N/A",$val);
        ?>
        <li class="list-group-item active" style="margin: 3px 0;" id="n<?php echo $key-1 ?>" onclick="callajax(<?php echo $key-1 ?>)">
            <span class="newlino">
                <?php echo $key ?>
            </span> 
            <span class="newlisong">
                <?php echo $val ?>
            </span></li>
        <?php } ?>
    </ul>
</div>
