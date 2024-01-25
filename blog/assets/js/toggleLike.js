// help link: https://www.youtube.com/watch?v=h1fKWxs7A2c
$(document).ready(function () {
    $("#like-toggle-form").submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: $('#url').val(),
            type: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                article: $('#article').val()
            },
            success: (data) => {

                $('#total_likes').text(data.total_likes)
                $('#like_icon').prop('class', `${data.liked_icon} fa-heart fa-lg`)
            },
            error: (e) => console.error(`There was an error with handling this request ${e.message}`)

        });
    });
});