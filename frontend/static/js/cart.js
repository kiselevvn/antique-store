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

const cartMenuSetting = {
  title: 'Меню корзины',
  icon: 'info',
  showDenyButton: true,
  showCancelButton: true,
  confirmButtonText: `Перейти в корзину`,
  denyButtonText: `Очистить корзину`,
  cancelButtonText: `Отмена`,
};

const orderSetting = {
  title: 'Подтверждение оформления',
  icon: 'info',
  showCancelButton: true,
  confirmButtonText: `Оформить товар`,
  cancelButtonText: `Отменить оформление`,
};

const showError = body => {
  Swal.fire({
    icon: 'error',
    title: 'Ошибка',
    html: body,
  })
};

const removeProductCart = id => {
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
      const productId = parseInt(id);
      cartLS.remove(productId);
      renderCart();
      renderCartValue();
    }
  })
};

const renderCart = event => {
  var tableBody = "";
  cartLS.list().forEach(product => {
    const summ = parseFloat(product.price)*parseInt(product.quantity);
    tableBody += "<tr>"+
    "<td class='kenne-product-remove'><div class='remove-btn' onclick='removeProductCart("+product.id+")' data-product-id='"+product.id+"'><i class='fa fa-trash' title='Remove'></i></div>  </td>"+
    "<td class='kenne-product-name'><a href='javascript:void(0)'>"+product.name+"</a></td>"+
    "<td class='kenne-product-price'><span class='amount'>"+product.price+"</span></td>"+
    "<td class='quantity'>"+
        product.quantity+
    "</td>"+
    "<td class='product-subtotal'><span class='amount'>"+summ+"</span></td>"+
    "</tr>"
  });
  table =document.querySelector("#cart-body");
  total =document.querySelector(".cart-total");
  if(table){
    table.innerHTML = tableBody;
  };
  if(total){
    total.innerHTML = cartLS.total();
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
        if(cartLS.exists(id))
        {
          cartLS.amount(id,  parseInt(count));
        }
        cartLS.add({
          id: response.data.id,
          price: response.data.price,
          name: response.data.name
        }, parseInt(count));
        Swal.fire('Товар добавлен в корзину!', '', 'success');
        renderCartValue();
      })
    }
  })

};


document.querySelector('.minicart-wrap').addEventListener('click', (event)=>{
    Swal.fire(cartMenuSetting).then((result) => {
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




const renderCartValue = () => {
  document.querySelectorAll(".cart-count").forEach(element => {
    element.innerHTML = cartLS.list().length;
  });
  document.querySelectorAll(".total-price").forEach(element => {
    element.innerHTML = cartLS.total();
  });
};


if (document.querySelector(".add-card-action")) {
  document
  .querySelector(".add-card-action")
  .addEventListener("click", event => {
      const id = event.target.dataset.productId;
      const count = document.querySelector(".cart-plus-minus-box").value;
      addCartAction(id,count);
  });
}


if (document.querySelector(".order-create-btn")) {
  document
  .querySelector(".order-create-btn")
  .addEventListener("click", event => {
    event.preventDefault();
    Swal
      .fire(orderSetting)
      .then(result => {
        if (result.isConfirmed) {
          const positions = []
          if(cartLS.list().length === 0){
            showError("Корзина товаров пуста");
            return
          }
          cartLS.list().forEach(position =>{
            positions.push({
              count: position.quantity,
              product: position.id
            });
          });

          const scheme = {
            positions: positions,
            address: document.querySelector("#address").value,
            email: document.querySelector("#email").value,
            phone: document.querySelector("#phone").value,
            name: document.querySelector("#name").value,
            comment: document.querySelector("#comment").value,
          };

          errorsHtml = ""
          if(scheme.address === ""){
            errorsHtml += "Необходимо заполнить поле <strong>Адрес</strong> <br />"
          }
          if(scheme.email === ""){
            errorsHtml += "Необходимо заполнить поле <strong>Электронная почта</strong> <br />"
          }
          if(scheme.phone === ""){
            errorsHtml += "Необходимо заполнить поле <strong>Телефон</strong> <br />"
          }
          if(scheme.comment === ""){
            errorsHtml += "Необходимо заполнить поле <strong>Комментарий</strong> <br />"
          }
          if(scheme.name === ""){
            errorsHtml += "Необходимо заполнить поле <strong>ФИО</strong> <br />"
          }
          if(errorsHtml !== ""){
            showError(errorsHtml);
            return;
          }
          console.log(scheme);
          if(scheme.positions.length)
          // const scheme = parseInt(id);
          axios
          .post("/orders/api/create/", scheme)
          .then(response => {
          // cartRemove();

            renderCart();
            renderCartValue();
          })
          .catch(error => console.log(error));

          console.log("success");
        }
      });
  });
}


const cartRemove = () => {
  cartLS.destroy();
};

