       var labeli2 = document.getElementById("tiempo2"),
            minuto3 = 20,
            segundo3 = 0,
            interval3 = setInterval(function(){
                if (--segundo3 < 0){
                    segundo3 = 59;
                    minuto3--;
                }
              
                if (!minuto3 && !segundo3)
                    clearInterval(interval3);
          
                labeli2.innerHTML = minuto3 + ":" + (segundo3 < 10 ? "0" + segundo3 : segundo3);
                   if(minuto3 == 0 && segundo3 == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval3);
             setTimeout("location.href='http://127.0.0.1:8000/ingenieria_ingrlm/'",600)
             }
            }, 1000); 