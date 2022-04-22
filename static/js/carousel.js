const featuredImages = document.querySelectorAll(".featured-image-container");
const nextButton = document.getElementById("next-button");
const prevButton = document.getElementById("prev-button");

let numberOfFeaturedImages = 0;
let visbleImage = 1;

let time;

window.addEventListener("DOMContentLoaded", function() {

    // The timer object handles the featured products carousel transition timing 
    let timer = {
        start: function() {
            time = setInterval(CarouselTimer, 6000);
        },
        stop: function() {
            StopTimer();
        }
    }
    // The number of featured products
    numberOfFeaturedImages = featuredImages.length

    // When carousel's prev button is clicked
    prevButton.addEventListener("click", function() {
            timer.stop();
            timer.start();
            if (visbleImage == 1) {
                visbleImage = numberOfFeaturedImages;
                transitionFeatueredImages(visbleImage);
            } else {
                visbleImage--;
                transitionFeatueredImages(visbleImage);
            }
        });

    // When carousel's next button is clicked
    nextButton.addEventListener("click", function() {
        timer.stop();
        timer.start();
        if (visbleImage == numberOfFeaturedImages) {
            visbleImage = 1;
            transitionFeatueredImages(visbleImage);
        } else {
            visbleImage++;
            transitionFeatueredImages(visbleImage);
        }
    });
    
    /* start carousel timer when page has finished loading
       But stop it when any of the carousel's button is triggered */
    timer.start();

    // Function when carousel interval timer clocks
    function CarouselTimer() {
        console.log(numberOfFeaturedImages);
        if (visbleImage == numberOfFeaturedImages) {
            visbleImage = 1;
            transitionFeatueredImages(visbleImage)
        } else {
            visbleImage++;
            transitionFeatueredImages(visbleImage)
        }
        
    }
    // Function to stop carousel transition timer
    function StopTimer() {
        clearInterval(time);
    }
});

function transitionFeatueredImages(pos, button) {
    featuredImages.forEach((image, index) => {
        if (pos) image.style.transform = `translateX(${-(((pos-index)*100)-100)}%)`;
            /*  The else statement allows more featured images to be positioned correctly without relying
            on a CSS to position them. Say we have 100 featured images. It will be
            very incovenient to position them one by one using CSS */
        else image.style.transform = `translateX(${(index)*100}%)`;
    })
}
// Transition featured images appropriately when page loads, for better performance.
transitionFeatueredImages();