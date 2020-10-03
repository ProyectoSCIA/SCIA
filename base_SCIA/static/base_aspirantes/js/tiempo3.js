     var labeli3 = document.getElementById("tiempo3"),
            minuto4 = 40,
            segundo4 = 0,
            interval4 = setInterval(function(){
                if (--segundo4 < 0){
                    segundo4 = 59;
                    minuto4--;
                }
              
                if (!minuto4 && !segundo4)
                    clearInterval(interval4);
          
                labeli3.innerHTML = minuto4 + ":" + (segundo4 < 10 ? "0" + segundo4 : segundo4);
                   if(minuto4 == 0 && segundo4 == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval4);
             setTimeout("location.href='http://127.0.0.1:8000/ingenieria_ingrv/'",600)
             }
            }, 1000); 