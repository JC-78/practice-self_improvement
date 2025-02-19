// Background script to facilitate communication between different parts of the extension
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // Forward the message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, request);
    });
  });
//manages background tasks and communication between different parts of the extension.  