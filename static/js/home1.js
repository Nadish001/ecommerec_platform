let currentSlide = 0;

function changeSlide(n) {
  let slides = document.querySelectorAll(".slide");
  let indicators = document.querySelectorAll(".indicators span");

  slides[currentSlide].style.display = "none";
  indicators[currentSlide].style.backgroundColor = "#ffffff80";

  currentSlide = currentSlide + n;

  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }

  if (currentSlide < 0) {
    currentSlide = slides.length - 1;
  }

  slides[currentSlide].style.display = "flex";
  indicators[currentSlide].style.backgroundColor = "white";
}

// sgs
let header = document.querySelector(".header");
let con2 = document.querySelector(".con2");
window.addEventListener("scroll", function () {
    let con2Bottom = con2.getBoundingClientRect().bottom;

    if (con2Bottom <= header.offsetHeight) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});
// rhhdn


let con3Index = 0;

function changeCon3Slide(direction) {
    let slides = document.querySelectorAll(".con3-slide");
    let indicators = document.querySelectorAll(".con3 .indicators span");

    slides[con3Index].classList.remove("active");
    indicators[con3Index].classList.remove("active");

    con3Index = con3Index + direction;

    if (con3Index >= slides.length) {
        con3Index = 0;
    }

    if (con3Index < 0) {
        con3Index = slides.length - 1;
    }

    slides[con3Index].classList.add("active");
    indicators[con3Index].classList.add("active");
}


// ################


let con5 = document.querySelector(".con5");
let header5 = document.querySelector(".header");

window.addEventListener("scroll", function () {
    let position = con5.getBoundingClientRect();

    if (position.top <= header5.offsetHeight &&
        position.bottom > header5.offsetHeight) {
        header5.classList.add("con5-header");
    } else {
        header5.classList.remove("con5-header");
    }
});
