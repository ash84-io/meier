function moveRandomPostURL(){
    let headers = {};
    Requests.get(
        apiURL.randomPostAPI,
        headers,
        moveRandomPostURLSuccessCallBack,
        function (){}
    );
}

function moveRandomPostURLSuccessCallBack(response) {
    location.href = response.data.data.url;
}
