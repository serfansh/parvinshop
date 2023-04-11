
// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// ENSURE SEARCH FORM EXISTS
if(searchForm){
    for(let i=0; pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            
            // GET DATA ATTRIBUTE
            let page = this.dataset.page

            // ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

            // SUBMIT FORM
            searchForm.submit()
        })
    }
}


document.getElementById("newsectionbtn").addEventListener('click', function (e) {
    var container = document.getElementById("csqpcontainer");
    var form = document.getElementById("csqpform");
    container.appendChild(form.cloneNode(true));
})


let thumbnails = document.getElementsByClassName('thumbnail')
let activeImages = document.getElementsByClassName('active')

for (var i=0; i < thumbnails.length; i++) {
    
    thumbnails[i].addEventListener('mouseover', function(){
        if (activeImages.length > 0){
            activeImages[0].classList.remove('active')
        }

        this.classList.add('active')
        document.getElementById('featured').src = this.src
    })
}