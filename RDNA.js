function isLoggedIn(){
  if (localStorage.getItem('isLoggedIn') === "true") {
    const registerWindow = document.getElementById('registerwindow');
    if (registerWindow) {
      registerWindow.remove();
    }
  }
}

isLoggedIn()
