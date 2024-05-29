const registrationForm = document.getElementById('registration');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');


function registerUser() {
  const name = nameInput.value;
  const email = emailInput.value;
  const password = passwordInput.value;

  localStorage.setItem('user', JSON.stringify({
    name: name,
    email: email,
    password: password
  }));

  nameInput.value = '';
  emailInput.value = '';
  passwordInput.value = '';

  alert('Account Created');
}



registrationForm.addEventListener('submit', registerUser);
