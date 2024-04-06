// Menu Email o Usuario
const menuEmail = document.querySelector('.navbar-email');
const desktopMenu = document.querySelector('.desktop-menu');

menuEmail.addEventListener('click', toogleDesktopMenu);

function toogleDesktopMenu () {
    desktopMenu.classList.toggle('inactive')
}

// =======================================
// Carrito de compras
const menuCarritoIcon = document.querySelector('.navbar-shopping-card');
const shoppingCart = document.querySelector('#shopping-cart');

menuCarritoIcon.addEventListener('click', toogleCarritoAside);

function toogleCarritoAside () {
    const isProductDetailClose = productDetailContainer.classList.contains('inactive');

    if(!isProductDetailClose) {
        closeProductDetailAside ()
    }
    shoppingCart.classList.toggle('inactive');
}

// =======================================
// Apartado de productos
constcardsContainer = document.querySelector('.cards-container');

const productList = [];
productList.push({
    name: 'Bike',
    price: 20,
    description: '1jhrghui riuoerhtgioua rfidugh',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
});
productList.push({
    name: 'Car',
    price: 130,
    description: '2jhrghui riuoerhtgioua rfidugh',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
});
productList.push({
    name: 'Computer',
    price: 12000,
    description: '3jhrghui riuoerhtgioua rfidugh',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
});

function renderProducts (arr) {

    for (product of productList) {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.addEventListener('click', (event) => {
            event.preventDefault();
            openProductDetailAside(product.image, product.name, product.price, product.description);
        });
    
        const productImg = document.createElement('img');
        productImg.setAttribute('src', product.image);
    
        const productInfo = document.createElement('div');
        productInfo.classList.add('product-info');
    
        const productInfoDiv = document.createElement('div');
    
        const productPrice = document.createElement('p');
        productPrice.innerText = '$' + product.price;
    
        const productName = document.createElement('p');
        productName.innerText = product.name;
    
        const productInfoFigure = document.createElement('figure');
    
        const productImgCart = document.createElement('img');
        productImgCart.setAttribute('src', './icons/bt_add_to_cart.svg');
    
    
        productInfoDiv.appendChild(productPrice);
        productInfoDiv.appendChild(productName);
    
        productInfoFigure.appendChild(productImgCart);
    
        productInfo.appendChild(productInfoDiv);
        productInfo.appendChild(productInfoFigure);
    
        productCard.appendChild(productImg);
        productCard.appendChild(productInfo);
    
        constcardsContainer.appendChild(productCard);
    }
}

renderProducts(productList);

// =======================================
// Detalle de productos

const productDetailContainer = document.querySelector('#product-detail');
const productDetailCloseIcon = document.querySelector('.product-detail-close');
productDetailCloseIcon.addEventListener('click', closeProductDetailAside);

productDetailCloseIcon.addEventListener('click', closeProductDetailAside);

function openProductDetailAside (image, name, price, description) {
    productDetailContainer.classList.remove('inactive');
    shoppingCart.classList.add('inactive');

    const detailImage = document.querySelector('#detail-image');
    const detailPrice = document.querySelector('.product-info p:nth-child(1)')
    const detailName = document.querySelector('.product-info p:nth-child(2)')
    const detailDescription = document.querySelector('.product-info p:nth-child(3)')

    detailImage.src = image;
    detailPrice.innerHTML = price;
    detailName.innerHTML = name;
    detailDescription.innerHTML = description;
}

function closeProductDetailAside () {
    productDetailContainer.classList.add('inactive');
}

