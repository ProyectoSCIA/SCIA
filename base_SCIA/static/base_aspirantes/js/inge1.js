var inge1 = document.getElementById('inge1');
inge1.addEventListener("click", ingenieria2, false); 

function ingenieria2(){
  if(inge1.disabled == false){
     inge1.disabled = true;
     
     setTimeout(function(){
        inge1.disabled = false;
    }, 14400000)
  }
}