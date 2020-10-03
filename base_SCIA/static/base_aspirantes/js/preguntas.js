var tabButtons = document.querySelectorAll(".tabContainer .buttonContainer button");
var tabPanels = document.querySelectorAll(".tabContainer  .tabPanel");

function showPanel(panelIndex, colorCode) {
    tabButtons.forEach(function (node) {
        node.style.backgroundColor = "#eaeded";
        node.style.color = "";
    });

    tabButtons[panelIndex].style.backgroundColor = colorCode;
    tabButtons[panelIndex].style.color = "white";
    tabPanels.forEach(function (node) {
        node.style.display = "none";
    });

    tabPanels[panelIndex].style.display = "block";
    tabPanels[panelIndex].style.backgroundColor = "#f6f6f6";
}

showPanel(0, '#f8c471');


function comprobar(){
        if(document.formulario.imagen.value==""){
            alert("complete los campos");
        }else{
            alert("has seleccionado una imagen");
        }
    }
