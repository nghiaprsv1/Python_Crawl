var updateBtns = document.getElementsByName('update-cart')

for (i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function()
    {
       var productID = this.dataset.product
       var action = this.dataset.action
       console.log('productID',productID,'action',action) 
    })
}