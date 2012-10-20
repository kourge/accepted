$(document).ready(function() {
   $("#add_sat_subject").click(clone_sat_subject); 
   $("#add_extracurricular").click(clone_extracurricular);
   $("#add_sport").click(clone_sport);
   $("#add_work").click(clone_work);
   $(".icon-remove").click(function() {
       /*var parent = $(this).parent();
       if (
        $(this).parent().remove();*/
    });
});

function clone_sat_subject() {
    var clone = $($(".sat_subject")[0]).clone();
    clone.children()[1].value = "";  
    $($(".sat_subject").last()).after(clone);
}

function clone_extracurricular() {
    var clone = $($(".extracurricular")[0]).clone();
    clone.children()[0].value = "";  
    clone.children()[2].value = "";  
    clone.children()[4].value = "";  
    $($(".extracurricular").last()).after(clone);
}

function clone_sport() {
    var clone = $($(".sport")[0]).clone();
    clone.children()[0].value = "";  
    clone.children()[2].value = "";  
    clone.children()[4].value = "";  
    $($(".sport").last()).after(clone);
}

function clone_work() {
    var clone = $($(".work")[0]).clone();
    clone.children()[0].value = "";  
    clone.children()[2].value = "";  
    clone.children()[4].value = "";  
    $($(".work").last()).after(clone);
}
