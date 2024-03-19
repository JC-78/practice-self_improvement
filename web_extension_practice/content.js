chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action == 'changeColor') {
      document.body.style.backgroundColor = 'lightblue';
    }
  });
  //modifies the content of web pages.