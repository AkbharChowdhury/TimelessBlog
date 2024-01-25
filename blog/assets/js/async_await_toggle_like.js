window.onload = () => {
    document.querySelector("#like-toggle-form").addEventListener('submit', (e) => {
        e.preventDefault()
        toggleLike().then(data => {
            console.log(data)
            document.querySelector('#total_likes').textContent = data.total_likes
            document.querySelector('#like_icon').setAttribute('class', `${data.liked_icon} fa-heart fa-lg`)
        })
    })
}

// https://blog.stackademic.com/understanding-fetch-with-async-await-5289557d623a
async function toggleLike() {
    try {
        const response = await fetch(document.getElementById('url').value, {
            method: 'POST',
            body: JSON.stringify({
                article: document.querySelector('#article').value,
                csrfmiddlewaretoken: document.querySelector("input[name=csrfmiddlewaretoken]").value,
            }),
            headers: {
                "X-CSRFToken": document.querySelector("input[name=csrfmiddlewaretoken]").value,
                'Content-Type': 'application/json',
            },
        });
        return await response.json();


    } catch (e) {
        console.error(`There was an error toggling like: ${e.message}`);
    }
}