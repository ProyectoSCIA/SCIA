       var labe = document.getElementById("tiemp"),
            minuto = 20,
            segundo =00,
            interval = setInterval(function(){
                if (--segundo < 0){
                    segundo = 59;
                    minuto--;
                }
              
                if (!minuto && !segundo)
                    clearInterval(interval);
          
                labe.innerHTML = minuto + ":" + (segundo < 10 ? "0" + segundo : segundo);
                if(minuto == 0 && segundo == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interval);
             setTimeout("location.href='http://127.0.0.1:8000/gastronomia_pm/'",600)
             }
            }, 1000);  