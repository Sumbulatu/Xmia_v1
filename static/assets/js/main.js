
document.addEventListener('DOMContentLoaded', function () {
    const navbarEl = document.querySelector('.navbar');
    const btnContainerEl = document.querySelector('.top-container');

    window.addEventListener('scroll', () => {
        if (window.scrollY > btnContainerEl.offsetTop - navbarEl.offsetHeight - 10) {
            navbarEl.classList.add('active');
        } else {
            navbarEl.classList.remove('active');
        }
    });
});

