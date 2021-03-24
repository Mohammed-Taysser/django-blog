
$(".profile-container").addClass("pre-enter");
setTimeout(function(){
    $(".profile-container").addClass("on-enter");
}, 500);
setTimeout(function(){
    $(".profile-container").removeClass("pre-enter on-enter");
}, 3000);