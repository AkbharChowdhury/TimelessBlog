window.onload = () => {
    document.querySelector("#like-toggle-form").addEventListener('submit', (e) => {
        e.preventDefault()
        const url = document.getElementById('url').value;
        toggleLike(url).then(data => {
            if (data) {
                document.querySelector('#total_likes').textContent = data.total_likes
                document.querySelector('#like_icon').setAttribute('class', `${data.liked_icon} fa-heart fa-lg`)
            }
        })
    })
}

// https://blog.stackademic.com/understanding-fetch-with-async-await-5289557d623a
async function toggleLike(url) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify({
                article: document.getElementById('article').value,
            }),
            headers: {
                "X-CSRFToken": document.querySelector("input[name=csrfmiddlewaretoken]").value,
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            alert(`There was an error toggling like: ${response.status} - ${response.statusText} ${url}`);
            return
        }

        return await response.json();


    } catch (e) {
        console.error(`There was an error toggling like: ${e.message}`);
    }
}
