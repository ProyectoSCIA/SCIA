var b = document.getElementById('b');
b.addEventListener("click", blo, false); 

function blo(){
  if(b.disabled == false){
     b.disabled = true;
     
     setTimeout(function(){
        b.disabled = false;
    }, 60000)
  }    
}