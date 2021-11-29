$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $('.navbar-nav>li>a').on('click', function(){
            $('.navbar-collapse').collapse('hide');
        });
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $('.navbar-nav>li>a').on('click', function(){
            $('.navbar-collapse').collapse('hide');
        });
    }
});

$(function() {
    $('.page-scroll a').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1000, 'easeInOutExpo');
        event.preventDefault();
    });
});

const btnSend = document.querySelector('#btn-send')
const btnSendLoader = document.querySelector('#btn-send-loader')

btnSend.addEventListener("click", ()=> {
    btnSendLoader.style.display = "block";
    btnSend.style.display = "none"

});

setTimeout(() => {
    document.querySelector('#alert-msg').style.display = 'none';
}, 5000)