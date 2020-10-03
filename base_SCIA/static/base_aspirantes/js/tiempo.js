      var labeli = document.getElementById("tiempoi"),
            minuto1 = 60,
            segundo1 = 00,
            interval1 = setInterval(function(){
                if (--segundo1 < 0){
                    segundo1 = 59;
                    minuto1--;
                }
              
                if (!minuto1 && !segundo1)
                    clearInterval(interval1);
          
                labeli.innerHTML = minuto1 + ":" + (segundo1 < 10 ? "0" + segundo1 : segundo1);
                   if(minuto1 == 0 && segundo1 == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval1);
             setTimeout("location.href='http://127.0.0.1:8000/ingenieria_ingfis/'",600)
             }
            }, 1000);