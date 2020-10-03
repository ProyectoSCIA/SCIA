     var labeli1 = document.getElementById("tiempo1"),
            minuto2 = 40,
            segundo2 = 0,
            interval2 = setInterval(function(){
                if (--segundo2 < 0){
                    segundo2 = 59;
                    minuto2--;
                }
              
                if (!minuto2 && !segundo2)
                    clearInterval(interval2);
          
                labeli1.innerHTML = minuto2 + ":" + (segundo2 < 10 ? "0" + segundo2 : segundo2);
                   if(minuto2 == 0 && segundo2 == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval2);
             setTimeout("location.href='http://127.0.0.1:8000/ingenieria_ingquim/'",600)
             }
            }, 1000); 