
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

function getModelAndAppNames(){
    const bodyElement = document.getElementsByTagName('body');
    let bodyElementClass = bodyElement[0].className.split(' ');
    const appLabel = bodyElementClass[1].replace('app-', '');
    const modelLabel = bodyElementClass[2].replace('model-', '');

    return [appLabel, modelLabel];
}

function CatchAdminButtonClick(apiUrl, buttonData) {
    let appAndModelLabels = getModelAndAppNames();
    const appLabel = appAndModelLabels[0];
    const modelLabel = appAndModelLabels[1];

    const data = JSON.stringify({"button_data": buttonData, "app_name": appLabel, "model_name": modelLabel});

     const csrfToken = getCookie('csrftoken');
     let xhr = new XMLHttpRequest();
     xhr.open("POST", apiUrl, true);
     xhr.setRequestHeader("Content-Type", "application/json");
     xhr.setRequestHeader("X-CSRFToken", csrfToken);
     xhr.send(data);

    }


function CatchAdminTextButtonClick(apiUrl, buttonData) {
    const textAreaData = document.getElementById("MessageText").value;

    const appAndModelLabels = getModelAndAppNames();
    const appLabel = appAndModelLabels[0];
    const modelLabel = appAndModelLabels[1];

    const data = JSON.stringify({"button_data": buttonData, "app_name": appLabel, "modelName": modelLabel, "text": textAreaData});

    const csrfToken = getCookie('csrftoken');
    let xhr = new XMLHttpRequest();
    xhr.open("POST", apiUrl, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.send(data);
    }
