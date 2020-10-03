var inge2 = document.getElementById('inge2');
inge2.addEventListener("click", ingenieria3, false); 

function ingenieria3(){
  if(inge2.disabled == false){
     inge2.disabled = true;
     
     setTimeout(function(){
        inge2.disabled = false;
    }, 14400000)
  }
}