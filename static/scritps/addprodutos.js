

const nome = document.querySelector('#name')
const codigo = document.querySelector('#codigo')
const btnconfirm = document.querySelector('#btnconfirm')

btnconfirm.addEventListener('click',function(e){
    if(nome.value != ''){
        nome.style.border='1px solid green'
       
        if(codigo.value != ''){
            codigo.style.border='1px solid green'
           
        }
        else{
            codigo.style.border='1px solid red'
            e.preventDefault()
        }
    }
    else{
        nome.style.border='1px solid red'
        e.preventDefault()
      
        
    }
})