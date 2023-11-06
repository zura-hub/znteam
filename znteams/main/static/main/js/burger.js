document.querySelector('.burger').addEventListener('click', function() {
    var list = document.querySelector('.list');
    if (list.style.display === 'none' || list.style.display === '') {
        list.style.display = 'block';
    } else {
        list.style.display = 'none';
    }
});


//Carousel

let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide img');
const totalSlides = slides.length;

document.getElementById("nextBtn").addEventListener("click", () => {
    currentSlide++;
    if(currentSlide >= totalSlides) currentSlide = 0;
    updateSlidePosition();
});

document.getElementById("prevBtn").addEventListener("click", () => {
    currentSlide--;
    if(currentSlide < 0) currentSlide = totalSlides - 1;
    updateSlidePosition();
});

function updateSlidePosition() {
    const slideWidth = slides[currentSlide].clientWidth;
    document.querySelector('.carousel-slide').style.transform = `translateX(-${slideWidth * currentSlide}px)`;
}



// active

