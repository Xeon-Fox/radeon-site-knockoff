document.querySelector('#rx500').addEventListener('click', function(){
    alert("Sorry, We are out of stock")
})

function isLoggedIn(){
  if (localStorage.getItem('isLoggedIn') === "true") {
    const registerWindow = document.getElementById('registerwindow');
    if (registerWindow) {
      registerWindow.remove();
    }
  }
}

isLoggedIn()
