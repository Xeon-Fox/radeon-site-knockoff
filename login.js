const loginForm = document.getElementById('registration');
const loginEmailInput = document.getElementById('email');
const loginPasswordInput = document.getElementById('password');

function login() {
    const email = loginEmailInput.value;
    const password = loginPasswordInput.value;

    const user = JSON.parse(localStorage.getItem('user'));
  
    if (user && user.email === email && user.password === password) {
      alert('Logged In');
      localStorage.setItem('isLoggedIn', true)
    } else {
      alert('Incorect name or password');
    }
  }

  function isLoggedIn(){
    if (localStorage.getItem('isLoggedIn') === "true") {
      const registerWindow = document.getElementById('registerwindow');
      if (registerWindow) {
        registerWindow.remove();
      }
    }
  }
  
  isLoggedIn()
  

loginForm.addEventListener('submit', login);
