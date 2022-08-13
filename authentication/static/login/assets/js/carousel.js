$('#themes-cards').owlCarousel({
  loop: true,
  center: true,
  items: 3,
  margin: 0,
  autoplay: true,
  smartspeed: 50,
  nav: true,
  responsive: {
    0: {
      items: 1
    },
    750: {
      items: 2
    },
    1150 : {
      items: 3
    }
  }
});