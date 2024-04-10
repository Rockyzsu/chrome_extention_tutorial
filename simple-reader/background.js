chrome.runtime.onInstalled.addListener(() => {
    chrome.action.setBadgeText({
        text: "ON",
    });
});


chrome.action.onClicked.addListener(async function(tab) {
    console.log("this tab url is " + tab.url);
    const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
    // var prevState = ''
    var nextState = prevState;
    if (prevState === 'ON') {
        nextState = 'OFF'
    } else {
        nextState = 'ON'
    }

    await chrome.action.setBadgeText({
        tabId:tab.id,
        text: nextState,
    });

    if (nextState === "ON") {
        // Insert the CSS file when the user turns the extension on
        await chrome.scripting.insertCSS({
          files: ["focus.css"],
          target: { tabId: tab.id },
        });
      } else if (nextState === "OFF") {
        // Remove the CSS file when the user turns the extension off
        await chrome.scripting.removeCSS({
          files: ["focus.css"],
          target: { tabId: tab.id },
        });
      }
    
});



