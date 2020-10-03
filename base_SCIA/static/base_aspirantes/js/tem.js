       var lab = document.getElementById("tiem"),
            minut = 40,
            segund = 00,
            interva = setInterval(function(){
                if (--segund < 0){
                    segund = 59;
                    minut--;
                }
              
                if (!minut && !segund)
                    clearInterval(interva);
          
                lab.innerHTML = minut + ":" + (segund < 10 ? "0" + segund : segund);
                   if(minut == 0 && segund == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interva);
             setTimeout("location.href='http://127.0.0.1:8000/gastronomia_cl/'",600)
             }
            }, 1000);  