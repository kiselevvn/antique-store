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
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: `Перейти в корзину`,
      denyButtonText: `Очистить корзину`,
      сancelButtonText: `Отмена`,
    }).then((result) => {
      if (result.isConfirmed) {
        // Swal.fire('Saved!', '', 'success')
      } else if (result.isDenied) {
        cartRemove();
        renderCartValue();
      }
    })
})

document.body.onload = event => {
  renderCartValue();
}

document.onclick = event => {
  if(event.target.classList.contains("add-card-action")){
    const id = event.target.dataset.productId;
    const count = document.querySelector(".cart-plus-minus-box").value;
    addCartAction(id,count);
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
        // cartRemove();
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
