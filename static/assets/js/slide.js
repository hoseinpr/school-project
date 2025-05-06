let slideIndex = 1;
let animationType = 'slide';
let direction = 'right'; // جهت پیش فرض

showSlides(slideIndex);

function plusSlides(n) {
  // تعیین جهت بر اساس مقدار n
  direction = n > 0 ? 'right' : 'left';
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  // تعیین جهت بر اساس موقعیت اسلاید جدید
  direction = n > slideIndex ? 'left' : 'right';
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  
  // غیرفعال کردن همه اسلایدها
  for (i = 0; i < slides.length; i++) {
    slides[i].classList.remove('active');
    slides[i].style.display = "none";
    slides[i].style.animation = "none";
  }
  
  // فعال کردن اسلاید جاری
  slides[slideIndex-1].style.display = "block";
  slides[slideIndex-1].classList.add('active');
  
  // اعمال افکت براساس نوع و جهت
  switch(animationType) {
    case 'slide':
      slides[slideIndex-1].style.animation = direction === 'right' 
        ? "slideInFromRight 1s ease-in-out" 
        : "slideInFromLeft 1s ease-in-out";
      break;
    case 'fade':
      slides[slideIndex-1].style.animation = "fadeIn 1.5s ease-in-out";
      break;
    case 'zoom':
      slides[slideIndex-1].style.animation = "zoomIn 1.2s ease-out";
      break;
    case 'flip':
      slides[slideIndex-1].style.animation = direction === 'right'
        ? "flipInRight 1.8s ease-in-out"
        : "flipInLeft 1.8s ease-in-out";
      break;
  }
  
  // به‌روزرسانی نقاط
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex-1].className += " active";
}

// اتوماتیک با جهت ثابت
setInterval(() => {
  plusSlides(1); // همیشه به سمت راست
}, 25000000000);