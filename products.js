function isLoggedIn(){
  if (localStorage.getItem('isLoggedIn') === "true") {
    const registerWindow = document.getElementById('registerwindow')
    if (registerWindow) {
      registerWindow.remove()
    }
  }
}

isLoggedIn()

function BuyButton(event) {
  const buttonID = event.target.id;
  const currentQuantity = parseInt(localStorage.getItem(`${buttonID}`) || '0');

  if (currentQuantity > 0) {
    alert(`${buttonID} is already in your cart`);
    return;
  }

  try {
    localStorage.setItem(`${buttonID}`, 1);
    alert(`${buttonID} has been added to your cart`);

  } catch (error) {
    console.error('Error saving purchase to localStorage:', error);
  }
}

const buttons = document.querySelectorAll('#rx5500, #rx5600, #rx5700, #rx6500, #rx6600, #rx6700, #rx7600, #rx7700, #rx7800');
for (const button of buttons) {
  button.addEventListener('click', BuyButton);
}
