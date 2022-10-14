
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function CatchAdminButtonClick(apiUrl, buttonData) {
    const csrftoken = getCookie('csrftoken');
    //<body class=" app-adminbuttons model-testclass change-form"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", apiUrl, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    var currentUrl = new URL(window.location.href);
    var currentPathName = currentUrl.pathname;
    var currentPathName = currentPathName.split('/').filter(part => part.length > 0)
    var appName = currentPathName[currentPathName.findIndex(part => part == 'admin') + 1]
    var modelName = currentPathName[currentPathName.findIndex(part => part == 'admin') + 2]
    if (currentPathName.at(-1) == 'change') {
        var data = JSON.stringify({"button_data": buttonData, "app_name": appName, "modelName": modelName});
        xhr.send(data);
    }
    console.log(currentPathName);
    }


function CatchAdminTextButtonClick(apiUrl, buttonData) {
    const csrftoken = getCookie('csrftoken');

    var xhr = new XMLHttpRequest();
    var textAreaData = document.getElementById("MessageText").value;
    console.log(textAreaData);
    xhr.open("POST", apiUrl, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    var currentUrl = new URL(window.location.href);
    var currentPathName = currentUrl.pathname;
    var currentPathName = currentPathName.split('/').filter(part => part.length > 0)
    var appName = currentPathName[currentPathName.findIndex(part => part == 'admin') + 1]
    var modelName = currentPathName[currentPathName.findIndex(part => part == 'admin') + 2]
    if (currentPathName.at(-1) == 'change') {
        var data = JSON.stringify({"button_data": buttonData, "app_name": appName, "modelName": modelName, "text": textAreaData});
        xhr.send(data);
    }

    }

