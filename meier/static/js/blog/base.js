const apiURL = {
  randomPostAPI: "/api/v1/random-post",
};


const Requests = {
  async get(url, headers = {}, successCallBack = function (){}, errorCallback = function (){}) {
    axios
      .get(url, { headers: headers })
      .then(function (response) {
        if (successCallBack) {
          successCallBack(response);
        }
      })
      .catch(function (error) {
        console.log(error);
        errorCallback(error);
      });
  },

};


