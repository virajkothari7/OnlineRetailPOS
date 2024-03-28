$(document).ready(function(){
        const button = document.createElement("button");
        button.innerText = "Filter Tab";
        button.classList.add("btn-secondary");
        const line = document.createElement("li");
        line.appendChild(button); 
        const object = document.querySelector('.object-tools');
        object.appendChild(line)
        
        button.addEventListener("click", () => {
            $(this).find('#changelist-filter').toggle();
        });
        
    });
   