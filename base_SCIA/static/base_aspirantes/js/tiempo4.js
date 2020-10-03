     var labeli4 = document.getElementById("tiempo4"),
            minuto5 = 20,
            segundo5 = 0,
            interval5 = setInterval(function(){
                if (--segundo5 < 0){
                    segundo5= 59;
                    minuto5--;
                }
              
                if (!minuto5 && !segundo5)
                    clearInterval(interval5);
          
                labeli4.innerHTML = minuto5 + ":" + (segundo5 < 10 ? "0" + segundo5 : segundo5);
                   if(minuto5 == 0 && segundo5 == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval5);
             setTimeout("location.href='http://127.0.0.1:8000/agradecimiento/'",600)
             }
            }, 1000); 