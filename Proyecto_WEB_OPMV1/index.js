const btnCart = document.querySelector('.contenedor-icon')
const contenedorCartProducts = document.querySelector('.contenedor-cart-products')

btnCart.addEventListener('click', () => {
   contenedorCartProducts.classList.toggle('hidden-cart') 
})

/*..........................*/

const CarInfo = document.querySelector('cart-product')