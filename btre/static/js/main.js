const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(function () {
  $("#messsage").fadeOut("slow");
}, 3000);
