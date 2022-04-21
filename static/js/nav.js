// const navToggleButton = document.querySelector(".toggle-nav-button");
// const navBar = document.querySelector(".primary-navigation");
const dropdownButton = document.querySelector(".search-dropdown");
const searchInput = document.querySelector(".search-input");
const filterListContainer = document.querySelector(".categories-filter-container");

let left = dropdownButton.offsetLeft;
function positionDropdownMenu(){
    console.log(dropdownButton.offsetLeft);
    filterListContainer.style.marginLeft = left+'px';
}
positionDropdownMenu()

// When screen is resized
window.addEventListener("resize", function() {
    // navBar.dataset.visible = "false";
    // navToggleButton.dataset.navVisible = "false";
    left = dropdownButton.offsetLeft;
    positionDropdownMenu();
    filterListContainer.dataset.visible = "false";
});

// Handling Search Form Functionality 
const searchForm = document.forms[0];
class FormHandling {
    constructor(form, dropdownList) {
        this.button = form.querySelector(".search-dropdown");
        this.dropdown = dropdownList
        this.filterList = dropdownList.querySelectorAll("li");
        this.span = this.button.querySelector("span");
    }
    left = dropdownButton.offsetLeft;
    listText = '';
    toggleDropdownList() {
        if (filterListContainer.dataset.visible == "false") {
            filterListContainer.dataset.visible = "true";
            // console.log(this.filterList);
            this.filterList.forEach(list => {
                list.addEventListener("click", this.updateDropdownText);
            })

        } else {
            filterListContainer.dataset.visible = "false";
        }
    }
    updateDropdownText(e) {
        this.listText = e.target.textContent;
        dropdownButton.querySelector("span").textContent = this.listText;
        filterListContainer.dataset.visible = "false";
        searchInput.focus();
    }

}

const formhandle = new FormHandling(searchForm, filterListContainer);
// When dropdown button is clicked: Hide or show Filter dropdown list
dropdownButton.addEventListener("click", function() {
    formhandle.toggleDropdownList();
    // formhandle.updateDropdownText();
    
});
