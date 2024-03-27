$('.portfolio-slider').slick({
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: true,
  autoplay: true,
  speed: 300,
  cssEase: 'linear',
  responsive: [
    {
      breakpoint: 993,
      settings: {
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        autoplay: true,
        speed: 300,
        fade: true,
        cssEase: 'linear',
      }
    },
  ]
});
$('.portfolio-detail-slider').slick({
  adaptiveHeight: true,
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: true,
  autoplay: true,
  speed: 300,
  cssEase: 'linear',
});






