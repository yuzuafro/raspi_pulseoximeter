<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/bootstrap.min.css">
<!--
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
-->
<script type="text/javascript" src="js/jquery-3.4.1.min.js"></script>
<script type="text/javascript" src="js/popper.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<script type="text/javascript">
  var $SCRIPT_ROOT = "{{ request.script_name }}";
</script>
</head>
<body>
<title>SpO2 & 心拍数</title>
<script type="text/javascript">
  $(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '_measure', {
      }, function(data) {
        $('#result_spo2').text(data.spo2);
        $('#result_heartrate').text(data.heartrate);
      });
      return false;
    };

    $('#measure').bind('click', submit_form);
  });
</script>
<hr>
<h2 class="text-center text-info">SpO<sub>2</sub> : <span id="result_spo2"></span></br></p>
<h2 class="text-center text-info">心拍数 : <span id="result_heartrate"></span></p>
<p class="text-center"><button type="button" input id="measure" class="btn btn-primary btn-lg btn-block">測定</button></p>
</body>
</html>
