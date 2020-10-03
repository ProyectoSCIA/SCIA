var inge3 = document.getElementById('inge3');
inge3.addEventListener("click", ingenieria4, false); 

function ingenieria4(){
  if(inge3.disabled == false){
     inge3.disabled = true;
     
     setTimeout(function(){
        inge3.disabled = false;
    }, 14400000)
  }
}