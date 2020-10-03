var inge = document.getElementById('inge');
inge.addEventListener("click", ingenieria1, false); 

function ingenieria1(){
  if(inge.disabled == false){
     inge.disabled = true;
     
     setTimeout(function(){
        inge.disabled = false;
    }, 14400000)
  }
}