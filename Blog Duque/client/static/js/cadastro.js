
let btn = document.querySelector("#submit")

btn.addEventListener('click',function(e){
let nome = document.querySelector("#nome").value
let email = document.querySelector("#email").value
let senha1 = document.querySelector("#senha1").value
let senha2 = document.querySelector("#senha2").value
let _senha1 = document.querySelector("#senha1")
let _senha2 = document.querySelector("#senha2")
let _alert = document.querySelector('#alert')

   
   
    if(email.length >= 8){
        if(senha1.length >= 5){
            if(senha2.length >= 5){
                if(senha1 == senha2 || senha2 == senha1){
                    _alert.style.display='none'
                }
                else{
                    _alert.style.display='flex'
                    _senha1.style.border='2px solid red'
                    _senha2.style.border='2px solid red'
                    
                    e.preventDefault()
                }
            }
            else{
                e.preventDefault()
            }
        }
        else{
            e.preventDefault()
        }
    }
    else{
        e.preventDefault()
    }
})