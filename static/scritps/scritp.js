
const cadMenu = document.querySelector(`.cadMenu`)
const loginMenu = document.querySelector(`.loginMenu`)
let cnome = document.querySelector("#cnome")
let senha1 = document.querySelector("#senha1")
let senha2 = document.querySelector("#senha2")
const btnlogin = document.querySelector('#login')
const subcad = document.querySelector('#subcad')
const sulogin = document.querySelector('#sublogin')
let titlehp = document.querySelector('.aviso')

cadMenu.disabled = false;
loginMenu.disabled = false;

btnlogin.addEventListener('click',function(){

 if(loginMenu.style.display === 'none'){
   loginMenu.style.display='flex'
   btncad.disabled=true;
 }
 else{
   loginMenu.style.display='none'
   btncad.disabled=false;
 }

})

const btncad = document.querySelector('#cad');

btncad.addEventListener('click',function(){
   if(cadMenu.style.display === 'none'){
      cadMenu.style.display='flex'
      btnlogin.disabled=true;
    }
    else{
      cadMenu.style.display='none'
      btnlogin.disabled=false;
    }
})


subcad.addEventListener('click',function(e){
    
    if(cnome.value != ''){
        cnome.style.border='1px solid green'
        if(senha1.value != ''){
            senha1.style.border='1px solid green'
            if(senha2.value != ''){
                senha2.style.border='1px solid green'
                if(senha1.value != senha2.value){
                    alert('As Senhas Não Estão iguais')
                    senha2.style.border='1px solid red'
                    e.preventDefault()   
                }
                else{
                    console.log('Sucesso')
                }
            }
            else{
                senha2.style.border='1px solid red'
                e.preventDefault()
            }
        }
        else{
            senha1.style.border='1px solid red'
            e.preventDefault()
        }
    }
    else{
        cnome.style.border='1px solid red'
        e.preventDefault()
    }
})