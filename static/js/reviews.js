const products = document.querySelectorAll(".items-wrapper .item-card");

products.forEach(product => {
    
    let reviewStarContainer = product.querySelector(".star");
    console.log(reviewStarContainer);
    // console.log(reviewStarContainer);
    reviewStarContainer.innerHTML='';
    let numReview = product.querySelector(".average-rating").textContent;
    numReview = numReview.replace(',', '');
    reviewRounded = parseInt(numReview)
    decimal = numReview.split(".")[1]
    // console.log('numReview: '+numReview)
    // console.log('rounded: '+reviewRounded);
    // console.log('decimal: '+decimal);


    for (let i=1; i<=5; i++) {
        let halfStar = document.createElement("i");
        let fullStar = document.createElement("i");
        let emptyStar = document.createElement("i");
        fullStar.setAttribute("class", "fa fa-star");
        halfStar.setAttribute("class", "fa fa-star-half-o")
        emptyStar.setAttribute("class", "fa fa-star-o")
        if (i <= reviewRounded) {
            // console.log('i is now '+i, reviewRounded)
            reviewStarContainer.appendChild(fullStar)
        } else {
            if (i == reviewRounded+1 && decimal != 0) reviewStarContainer.appendChild(halfStar);
            else reviewStarContainer.appendChild(emptyStar);
        }
    }
    



});