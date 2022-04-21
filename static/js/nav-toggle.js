const navToggleButton = document.querySelector(".toggle-nav-button");
const navBar = document.querySelector(".primary-navigation");

// When screen is resized
window.addEventListener("resize", function() {
    navBar.dataset.visible = "false";
    navToggleButton.dataset.navVisible = "false";
    // left = dropdownButton.offsetLeft;
    // positionDropdownMenu();
    // filterListContainer.dataset.visible = "false";
});


// When nav button is clicked: Toggle (hide or display) nav bar
navToggleButton.addEventListener("click", function() {
    if (this.dataset.navVisible == "true") {
        navBar.dataset.visible = "false";
        this.dataset.navVisible = "false";
    }
    else {
        navBar.dataset.visible = "true";
        this.dataset.navVisible = "true";
    }
});
