const dateInput = document.getElementById('id_date')
const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')

const picker = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
  theme: {
    theme_color: '#1f784b'
  }
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})