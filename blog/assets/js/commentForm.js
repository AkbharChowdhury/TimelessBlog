// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()


let commentForm = document.querySelector('#commentForm');
let commentName = document.querySelector('#name');
let comment = document.querySelector('#body');
const errors = document.querySelector('#errors');
const errorClass = 'border-danger';

const trim = (element) => {

   element.value = element.value.
   replace(/(^\s*)|(\s*$)/gi, ""). // removes leading and trailing spaces
   replace(/[ ]{2,}/gi, " "). // replaces multiple spaces with one space
   replace(/\n +/, "\n"); // Removes spaces after newlines
   return element;
}
const showErrorMessage = (message) => `
                            <div class="alert alert-danger d-flex align-items-center" role="alert">
                              <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                              <div>
                               ${message}
                              </div>
                            </div>
                    `;
const removeError = (element) => trim(element).value !== '' && element.classList.contains(errorClass) ? element.classList.remove(errorClass) : '';
const addError = (element) => trim(element).value == '' && !element.classList.contains(errorClass) ? element.classList.add(errorClass) : '';


if (commentForm) {
    document.querySelector('#name').addEventListener("focusout", (e) => removeError(commentName));
    document.querySelector('#body').addEventListener("focusout", (e) => removeError(comment));


   commentForm.addEventListener('submit', (e) => {
      errors.innerHTML = '';

      if (trim(commentName).value === '' && trim(comment).value === '') {

         e.preventDefault();
         errors.innerHTML = showErrorMessage('name and body is required!');
         commentName.classList.add(errorClass);
         comment.classList.add(errorClass);
         return;
      }

      if (trim(comment).value === '') {

         e.preventDefault();
         errors.innerHTML = showErrorMessage('comment is required!');
         removeError(commentName);
         addError(comment);
         return;
      }

      if (trim(commentName).value === '') {
         e.preventDefault();
         errors.innerHTML = showErrorMessage('name is required!');
         removeError(comment);
         addError(commentName);
         return;
      }
   })
}