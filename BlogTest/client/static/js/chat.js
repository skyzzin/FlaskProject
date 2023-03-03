const enviar = document.querySelector('#enviar')
const box = document.querySelector('.box-msg')

enviar.addEventListener('click', function() {
  const inputText = document.querySelector('#msg_text').value
  
  const msg = document.createElement('div')
  const avatar = document.createElement('div')
  const foto = document.createElement('div')
  const nome = document.createElement('div')
  const txt = document.createElement('p')

  msg.classList.add('msg')
  avatar.classList.add('avatar')
  foto.classList.add('foto')
  nome.classList.add('name')
  txt.classList.add('txt')

  box.append(msg)
  msg.append(avatar)
  avatar.append(foto, nome)
  msg.append(txt)
  
  const txtValue = document.querySelector('#msg_text').value
  txt.textContent = txtValue

  const nomeTags = document.querySelectorAll('.name')
  const get = new XMLHttpRequest()
  get.open('GET', '/user/nome')
  get.onload = function() {
    if (get.status == 200) {
      const data = JSON.parse(get.responseText)
      nomeTags.forEach(nomeTag => nomeTag.innerHTML = data)
    }
  }
  get.send()
  
  
})


function updateMsg() {
  const get = new XMLHttpRequest()
  get.open('GET', '/user/msg')
  get.onload = function() {
    if (get.status == 200) {
      const data = JSON.parse(get.responseText)

      data.forEach(msgData => {
        const msg = document.createElement('div')
        const avatar = document.createElement('div')
        const foto = document.createElement('div')
        const nome = document.createElement('div')
        const txt = document.createElement('p')

        msg.classList.add('msg')
        avatar.classList.add('avatar')
        foto.classList.add('foto')
        nome.classList.add('name')
        txt.classList.add('txt')

        box.append(msg)
        msg.append(avatar)
        avatar.append(foto, nome)
        msg.append(txt)

        const nomeValue = msgData[1]
        const txtValue = msgData[2]

        nome.textContent = nomeValue
        txt.textContent = txtValue
      })
    }
  }
  get.send()
}

setInterval(1000,updateMsg())