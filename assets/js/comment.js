$(document).ready(function(){
    const form = document.querySelector('#commentform');
    const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const modalTriggerBtn = document.querySelector('#submit-modall');
    const modalTitle = document.querySelector('.modal-title');
      
    
    form.addEventListener('submit', function(e){
        e.preventDefault();
        $.ajax({
            type : 'POST', 
            url  : form.action,
            data : {
                'csrfmiddlewaretoken' : csrf_token,
                'user_name'    : document.querySelector('input[name="user_name"]').value,
                'user_email'   : document.querySelector('input[name="user_email"]').value,
                'body' : document.querySelector('textarea[name="body"]').value,
                'captcha_0' : document.querySelector('input[name="captcha_0"]').value,
                'captcha_1' : document.querySelector('input[name="captcha_1"]').value,
            },
            enctype: 'json',
            success : function(r){
              form.reset()
              modalTitle.innerHTML = `لطفا دوباره تلاش کنید`
              if (document.location.hash)
                document.location.hash = ""
              modalTriggerBtn.click()
              setTimeout(()=>{
                document.location.reload()
              }, 3000)
            },
            error : function(r){
              document.location.hash = 'fail'
              document.location.reload()
            },
  
        });
    });
  
    if (document.location.hash === '#fail'){
  
      modalTitle.innerHTML = `لطفا دوباره تلاش کنید`
      modalTriggerBtn.click()
      }
  
  
    })
  
  