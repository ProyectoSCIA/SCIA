       var label = document.getElementById("tiempo"),
            minutos = 60,
            segundos = 00,
            intervalo = setInterval(function(){
                if (--segundos < 0){
                    segundos = 59;
                    minutos--;
                }
              
                if (!minutos && !segundos)
                    clearInterval(intervalo);
          
                label.innerHTML = minutos + ":" + (segundos < 10 ? "0" + segundos : segundos);
                    if(minutos == 0 && segundos == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
                    clearInterval(intervalo);
                    setTimeout("location.href='http://127.0.0.1:8000/gastronomia_el/'",600)
             }
            }, 1000);  