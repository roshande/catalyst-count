$(document).ready(function(){
  const input = document.getElementById('id_file')
  const uploadForm = document.getElementById("upload-form")

  const alertBox = document.getElementById('alert-box')
  const fileBox = document.getElementById('file-box')
  const progressBox = document.getElementById('progress-box')
  const cancelBox = document.getElementById('cancel-box')
  const cancelBtn = document.getElementById('cancel-btn')

  const csrf = document.getElementsByName('csrfmiddlewaretoken')

  input.addEventListener('change', ()=>{
	progressBox.classList.remove('not-visible')
	cancelBox.classList.remove('not-visible')

	const file_data = input.files[0]

	const fd = new FormData()
	fd.append('csrfmiddlewaretoken', csrf[0].value)
	fd.append('file', file_data)

	$.ajax({
	  type: 'POST',
	  url: uploadForm.action,
	  enctype: 'multipart/form-data',
	  data: fd,
	  beforeSend: function(){
		alertBox.innerHTML = ""
	  },
	  xhr: function(){
		const xhr = new window.XMLHttpRequest();
		xhr.upload.addEventListener('progress', function(e){
		  console.log(e)
		  if(e.lengthComputable){
			const percent = e.loaded / e.total * 100;
			console.log(percent)
			progressBox.innerHTML = `<div class="progress">
							  <div class="progress-bar" rolw="progressbar" style="width: ${percent}%" aria-valuenow="${percent}"</div>
							  <p>${percent.toFixed(1)}%`
		  }
		})
		cancelBtn.addEventListener('click', function(){
		  xhr.abort()
		  setTimeout(function(){
			uploadForm.reset();
			alertBox.innerHTML = ""
			progressBox.innerHTML = ""
			cancelBox.classList.add('not-visible')
		  }, 2000)
		})
		return xhr
	  },
	  success: function(response){
		console.log(response)
		alertBox.innerHTML = `<div class="alert alert-success" role="alert"> File Uploaded Successfully </div>`
		cancelBox.classList.add('not-visible')
	  },
	  error: function(error){
		console.log(error)
		alertBox.innerHTML = `<div class="alert alert-danger" role="alert"> Oops!! Something went wrong</div>`
	  },
	  cache: false,
	  contentType: false,
	  processData: false
	})
  })
})
