function isLoggedIn(){
  if (localStorage.getItem('isLoggedIn') === "true") {
    const registerWindow = document.getElementById('registerwindow');
    if (registerWindow) {
      registerWindow.remove();
    }
  }
}

isLoggedIn()

const videoCardData = {
  rx5500: {
    name: 'Radeon RX 5500',
    image: 'resources\3468-front.jpg',
    price: 299
  },
  rx5600: {
    // ... data for other video cards ...
  },
  // ... data for all video cards ...
};

function updateCartList() {
  const cartList = document.getElementById('cart-list').getElementsByTagName('tbody')[0];
  cartList.innerHTML = ''; // Clear existing cart items

  const cartItems = getCartItemsFromLocalStorage();

  if (cartItems.length === 0) {
    cartList.innerHTML = '<tr><td colspan="4">Your cart is empty.</td></tr>';
    return;
  }

  let total = 0;
  for (const [videoId, quantity] of Object.entries(cartItems)) {
    const videoCard = videoCardData[videoId];
    const row = cartList.insertRow();

    const cellName = row.insertCell();
    cellName.textContent = videoCard.name;

    const cellImage = row.insertCell();
    const imageElement = document.createElement('img');
    imageElement.src = videoCard.image;
    cellImage.appendChild(imageElement);

    const cellQuantity = row.insertCell();
    cellQuantity.innerHTML = `
      <input type="number" min="1" value="${quantity}" data-video-id="${videoId}">
    `;

    const cellRemove = row.insertCell();
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.addEventListener('click', () => removeFromCart(videoId));
    cellRemove.appendChild(removeButton);

    total += videoCard.price * quantity;
  }

  const totalRow = cartList.insertRow();
  const totalCell = totalRow.insertCell().colSpan = 4;
  totalCell.innerHTML = `<b>Total: $${total.toFixed(2)}</b>`;
}

function getCartItemsFromLocalStorage() {
  try {
    const cartItemsString = localStorage.getItem('cart');
    return cartItemsString ? JSON.parse(cartItemsString) : {};
  } catch (error) {
    console.error('Error retrieving cart from localStorage:', error);
    return {};
  }
}


function addToCart(videoId) {
  const cartItems = getCartItemsFromLocalStorage();
  cartItems[videoId] = cartItems[videoId] || 0;
  cartItems[videoId]++;

  localStorage.setItem('cart', JSON.stringify(cartItems));
  updateCartList();
}

function removeFromCart(videoId) {
  const cartItems = getCartItemsFromLocalStorage();
  delete cartItems[videoId];

  localStorage.setItem('cart', JSON.stringify(cartItems));
  updateCartList();
}

function handleQuantityChange(event) {
  const videoId = event.target.dataset.videoId;
  const quantity = parseInt(event.target.value);

  if (quantity < 1) {
    removeFromCart(videoId);
    return;
  }

  const cartItems = getCartItemsFromLocalStorage();
  cartItems[videoId] = quantity;

  localStorage.setItem('cart', JSON.stringify(cartItems));
  updateCartList();
}

const buttons = document.querySelectorAll('#rx5500, #rx5600, #rx5700, #rx6500, #rx6600, #rx6700, #rx7600, #rx7700, #rx7800');
for (const button of buttons) {
  button.addEventListener('click', () => addToCart(button.id));
}

const quantityInputs = document.querySelectorAll('input[type="number"]');
for (const input of quantityInputs) {
  input.addEventListener('change', handleQuantityChange);
}

updateCartList();
