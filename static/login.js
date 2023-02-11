var formlogar = document.querySelector('#logar')
var formcadastrar = document.querySelector('#cadastrar')
var btcolor = document.querySelector('.btncolor')

document.querySelector('#btnlogin')
.addEventListener('click', () => {
    formlogar.style.left = "25px"
    formcadastrar.style.left = "450px"
    btcolor.style.left = "0px"
})
document.querySelector('#btncadastrar')
.addEventListener('click', () => {
    formlogar.style.left = "-450px"
    formcadastrar.style.left = "25px"
    btcolor.style.left = "110px"
})