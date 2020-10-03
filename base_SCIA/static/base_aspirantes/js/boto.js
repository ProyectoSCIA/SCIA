var buto = document.getElementById('buto');
buto.addEventListener("click", bloque, false); 

function bloque(){
  if(buto.disabled == false){
     buto.disabled = true;
     
     setTimeout(function(){
        buto.disabled = false;
    }, 10800000)
  }
}