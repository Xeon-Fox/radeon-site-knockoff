
const videoCardData = {
  rx5500: {
    name: 'Radeon RX 5500',
    image: 'resources/3468-front.jpg',
    price: 299
  },
  rx5600: {
    name: 'Radeon RX 5600',
    image: 'resources/1720013.jpg',
    price: 399
  },
  rx5700: {
    name: 'Radeon RX 5700',
    image: 'resources/placa-video-asus-radeon-rx-5700-radeonrx57008gb-dag27C-L.jpg',
    price: 499
  },
  rx6500: {
    name: 'Radeon RX 6500',
    image: 'resources/dlcdnwebimgs.asus.png',
    price: 599
  },
  rx6600: {
    name: 'Radeon RX 6600',
    image: 'resources/2064536_webp.jpg',
    price: 699
  },
  rx6700: {
    name: 'Radeon RX 6700',
    image: 'resources/e513c8e147662d1b7c4af4305d035174365bebc6c2513650d9e11eb5e7eeb47c.jpg',
    price: 799
  },
  rx7600: {
    name: 'Radeon RX 7600',
    image: 'resources/gpiwohjatiupwsrp9kssnaambw22srs7.jpg',
    price: 899
  },
  rx7700: {
    name: 'Radeon RX 7700',
    image: 'resources/100025653_67761bed4b2c32e9bb25ef319b2a644d-500x500_webp.jpg',
    price: 999
  },
  rx7800: {
    name: 'Radeon RX 7800',
    image: 'resources/177893_RX-7800-XT-Phantom-Gaming-16GB-OC_02_2_webp.jpg',
    price: 1099
  },
};

function getItems(){
  let cardsList = {}
  if(localStorage.getItem('rx5500') == 1){
    cardsList.rx5500 = 1
  }
  if(localStorage.getItem('rx5600') == 1){
    cardsList.rx5600 = 1
  }
  if(localStorage.getItem('rx5700') == 1){
    cardsList.rx5700 = 1
  }
  if(localStorage.getItem('rx6500') == 1){
    cardsList.rx6500 = 1
  }
  if(localStorage.getItem('rx6600') == 1){
    cardsList.rx6600 = 1
  } 
  if(localStorage.getItem('rx6700') == 1){
    cardsList.rx6700 = 1
  }
  if(localStorage.getItem('rx7600') == 1){
    cardsList.rx7600 = 1
  }
  if(localStorage.getItem('rx7700') == 1){
    cardsList.rx7700 = 1
  }
  if(localStorage.getItem('rx7800') == 1){
    cardsList.rx7800 = 1
  }
  return cardsList
}

function deleteItem(cardId) {
  localStorage.removeItem(cardId);
  DisplayItems();
}

function DisplayItems(){
  let total = 0;
  let cartContent = '';
  let cartData = getItems()

  for (const id in cartData) {
    const quantity = cartData[id];
    const itemData = videoCardData[id];
    if (quantity > 0) {
      total += itemData.price * quantity;
      cartContent += `
        <tr class="product-line">
          <td><img src="${itemData.image}" alt=""></td>
          <td><p>${itemData.name}</p></td>
          <td><p>${quantity}</p></td>
          <td><p>$${itemData.price * quantity}</p></td>
          <td><button onclick="deleteItem('${id}')">Remove</button></td>
        </tr>
      `
    }
  }

  if (cartContent) {
    cartContent = `
      <h1>My Cart</h1>
      <table class="cart-table">
        <tr>
          <th>Image</th>
          <th>Product</th>
          <th>Quantity</th>
          <th>Price</th>
          <th></th>
        </tr>
        ${cartContent}
        <tr>
          <td colspan="2"><b>Total:</b></td>
          <td>$${total}</td>
        </tr>
      </table>
      <button onclick="BuyButton()" class="btn">Buy</button>
    `
    document.getElementById('cart-container').innerHTML = cartContent;
  } 
  else {
    alert('Your cart is empty.');
  }
}

function BuyButton(){
  alert("Thank you for shopping with us")
  // и тут типо отправка на бэкенд
  localStorage.clear();
  DisplayItems()
}

DisplayItems()