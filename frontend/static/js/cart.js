const errorSetting = {
  icon: 'error',
  title: 'Ошибка :(',
  text: 'Товар временно недоступен'
};

const noProductsSetting = {
  icon: 'info',
  title: 'Оповещение',
  title: 'Данный товар закончился на складе'
};



document.querySelector('.minicart-wrap').addEventListener('click', (event)=>{
    Swal.fire({
      title: 'Меню корзины',
      icon: 'info',
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: `Перейти в корзину`,
      denyButtonText: `Очистить корзину`,
      cancelButtonText: `Отмена`,
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/cart/";
      } else if (result.isDenied) {
        cartRemove();
        renderCartValue();
      }
    })
})

document.body.onload = event => {
  renderCartValue();

  renderCart();

}

document.onclick = event => {
  if(event.target.classList.contains("add-card-action")){
    const id = event.target.dataset.productId;
    const count = document.querySelector(".cart-plus-minus-box").value;
    addCartAction(id,count);
  };
  if(event.target.classList.contains("remove-btn")){
     Swal
      .fire({
        title: 'Удалить товар из корзины?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonText: `Удалить`,
        cancelButtonText: `Отмена`,
      })
      .then((result) => {
        if (result.isConfirmed) {
          const productId = parseInt(event.target.dataset.productId);
          cartLS.remove(productId);
          console.log(productId);
          renderCart();
        }
      })
  };
  if(event.target.classList.contains("inc-cart-product")){
    cartLS.quantity(event.target.dataset.productId, 1);
    event.target.value +=1;
  };
  if(event.target.classList.contains("dec-cart-product")){

  };
}

const addCartAction = (id, count) => {
  Swal.fire({
    title: 'Подтверждение действия',
    showDenyButton: true,
    confirmButtonText: `Добавить в корзину`,
    denyButtonText: `Отмена`,
  }).then((result) => {
    if (result.isConfirmed) {
      axios
      .get("/products/api/retrive/"+id+"/")
      .then((response)=>{
        if(response.data.count <= 0) {
          Swal.fire(noProductsSetting);
          return;
        }
        cartLS.add({
          id: response.data.id,
          price: response.data.price,
          name: response.data.name
        }, count);
        Swal.fire('Товар добавлен в корзину!', '', 'success');
        renderCartValue();
      })
    } else if (result.isDenied) {

    }
  })

};



const cartRemove = () => {
  cartLS.destroy()
};

const renderCartValue = () => {
  document.querySelectorAll(".cart-count").forEach(element => {
    element.innerHTML = cartLS.list().length
  });
  document.querySelectorAll(".total-price").forEach(element => {
    element.innerHTML = cartLS.total()
  });
};

const renderCart = event => {
  var tableBody = "";
  cartLS.list().forEach(product => {
    const summ = parseFloat(product.price)*parseInt(product.quantity)
    tableBody += "<tr>"+
    "<td class='kenne-product-remove'><div class='remove-btn' data-product-id='"+product.id+"'><i class='fa fa-trash' title='Remove'></i></div>  </td>"+
    "<td class='kenne-product-name'><a href='javascript:void(0)'>"+product.name+"</a></td>"+
    "<td class='kenne-product-price'><span class='amount'>"+product.price+"</span></td>"+
    "<td class='quantity'>"+
        product.quantity+
    "</td>"+
    "<td class='product-subtotal'><span class='amount'>"+summ+"</span></td>"+
"</tr>"
  });
  document.querySelector("#cart-body").innerHTML = tableBody;
  document.querySelector(".cart-total").innerHTML = cartLS.total();

}
