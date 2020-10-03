var but = document.getElementById('but');
but.addEventListener("click", bloqu, false); 

function bloqu(){
  if(but.disabled == false){
     but.disabled = true;
     
     setTimeout(function(){
        but.disabled = false;
    }, 7200000)
  }
}