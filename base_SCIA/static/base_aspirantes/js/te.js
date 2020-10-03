       var la = document.getElementById("tie"),
            minu = 40,
            segun = 00,
            interv = setInterval(function(){
                if (--segun < 0){
                    segun = 59;
                    minu--;
                }
              
                if (!minu && !segun)
                    clearInterval(interv);
          
                la.innerHTML = minu + ":" + (segun < 10 ? "0" + segun : segun);
                   if(minu == 0 && segun == 0)
                    {
            alert('Alerta: El tiempo se finalizó');
            clearInterval(interv);
                setTimeout("location.href='http://127.0.0.1:8000/agradecimiento/'",600)
            
             }
            }, 1000);  