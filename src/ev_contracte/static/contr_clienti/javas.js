function updateTextArea1() {         
    var allVals = [];
    $("#p_p :checked").each(function() {
      allVals.push($(this).val());
    });
    $('#p').val(allVals);
 }
$(function() {
  $('#p_p input').click(updateTextArea1);
  updateTextArea1();
});

function updateTextArea2() {         
    var allVals = [];
    $("#s_s :checked").each(function() {
      allVals.push($(this).val());
    });
    $('#s').val(allVals);
 }
$(function() {
  $('#s_s input').click(updateTextArea2);
  updateTextArea2();
});

function updateTextArea3() {         
    var allVals = [];
    $("#a_a :checked").each(function() {
      allVals.push($(this).val());
    });
    $('#a').val(allVals);
 }
$(function() {
  $('#a_a input').click(updateTextArea3);
  updateTextArea3();
});

function updateTextArea() {         
  var allVals = [];
  $('#c_b :checked').each(function() {
    allVals.push($(this).val());
  });
  $('#t').val(allVals);
}
$(function() {
$('#c_b input').click(updateTextArea);
updateTextArea();
});


$('.datepicker').datepicker({
  format: 'dd/mm/yyyy'
});


