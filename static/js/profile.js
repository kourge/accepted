$(document).ready(function() {
   $("#add_sat_subject").click(clone_sat_subject); 
});

function clone_sat_subject() {
    var clone = $($(".sat_subject")[0]).clone();
    clone.children()[2].value = "";  
    $($(".sat_subject").last()).after(clone);
}
