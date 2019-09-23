

const urlParams = new URLSearchParams(window.location.search);

function redirect_url(element, word) {
    let clicked_rel = element.attr(word);
    urlParams.set(word, clicked_rel);
    window.location.href = '/?' + urlParams.toString(); 
}

$(document).on('click', '#relevance .dropdown-item', function(e) { 
    e.preventDefault();
    redirect_url($(this), 'rel')
});

$(document).on('click', '#latest .dropdown-item', function(e) { 
    e.preventDefault();
    redirect_url($(this), 'rel')
});

$(document).on('click', '#latest .dropdown-item', function(e) { 
    e.preventDefault();
    let clicked_rel = $(this).attr('latest');
    urlParams.set('latest', clicked_rel);
    window.location.href = '/?' + urlParams.toString(); 
});