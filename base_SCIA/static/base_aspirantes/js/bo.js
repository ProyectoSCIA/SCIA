var bu = document.getElementById('bu');
bu.addEventListener("click", bloq, false); 

function bloq(){
  if(bu.disabled == false){
     bu.disabled = true;
     
     setTimeout(function(){
        bu.disabled = false;
    }, 3600000)
  }    
}