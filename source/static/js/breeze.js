let lastScrollY = window.scrollY;
const navbar = document.querySelector('.nav-bar');
const dynamic_word = document.querySelector('#dynamic-word')
const contact_button = document.querySelector('#contact-btn');
const contact_container = document.querySelector('.contact');
const close_contact_button = document.querySelector('#close-contact')

let languages = ['science des données', 'recherche scientifique', 'algorithme avancé', 'machine learning', 'système bas-niveau', 'calcul quantique']

window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    if (currentScrollY > lastScrollY && currentScrollY > 100) {
        navbar.style.transform = 'translateY(-70px)';
        navbar.style.backgroundColor = "#282c34";
    }
    else if (currentScrollY < lastScrollY ) {
        navbar.style.transform = 'translateY(0px)'
        navbar.style.backgroundColor = "white";
    }
    lastScrollY = currentScrollY;
})




let indexChangeWord = 1;

function changeWord(){
    dynamic_word.style.opacity = 0;
    setTimeout(() => {
        indexChangeWord = (indexChangeWord + 1)%languages.length;
        dynamic_word.innerHTML = languages[indexChangeWord];
        setTimeout(() => {
            dynamic_word.style.opacity = 1;
        }, 500)
    }, 500)
}

setInterval(changeWord, 5000)


close_contact_button.addEventListener('click', () => {
    contact_container.style.opacity = 0;
    setTimeout(() => {
        contact_container.style.display = 'none';
    }, 500)
})

contact_button.addEventListener('click', () => {
    contact_container.style.display = 'flex';
    setTimeout(() => {
        contact_container.style.opacity = 1;
    }, 1)
})