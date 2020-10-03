var inge4 = document.getElementById('inge4');
inge4.addEventListener("click", ingenieria5, false); 

function ingenieria5(){
  if(inge4.disabled == false){
     inge4.disabled = true;
     
     setTimeout(function(){
        inge4.disabled = false;
    }, 14400000)
  }
}