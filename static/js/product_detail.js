(function(){

    document.addEventListener("DOMContentLoaded", function() {

        const selectInput = document.querySelector("select");
        const inputWrapper = document.querySelector(".quantity-wrapper");

        selectInput.addEventListener("change", function(e) {
            if (this.value == "more") {
                const input = document.createElement("input");
                input.setAttribute("name", "quantity")
                input.setAttribute("class", "quantity-text")
                inputWrapper.innerHTML = ""
                inputWrapper.appendChild(input)
                input.focus();
                input.addEventListener("keydown", allowNumbersOnly);
            }
        }, true);

    });

    function allowNumbersOnly(e) {
        if (/[0-9]/.test(e.key) == false) e.preventDefault(); 
    }



}());

(function() {

    // const products = document.querySelectorAll(".items-wrapper .item-card");

    // products.forEach(product => {
        
        let reviewStarContainer = document.querySelector(".star");
        // console.log(reviewStarContainer);
        reviewStarContainer.innerHTML='';
        let numReview = document.querySelector(".average-rating").textContent;
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
                reviewStarContainer.appendChild(fullStar)
            } else {
                if (i == reviewRounded+1 && decimal != 0) reviewStarContainer.appendChild(halfStar);
                else reviewStarContainer.appendChild(emptyStar);
            }
        }
        



    // });


}())