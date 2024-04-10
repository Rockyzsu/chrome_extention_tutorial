
function getColor() {
  return 'red';
}



function changeBackgroundColor() {
  console.log('change its color ');
  // document.body.style.backgroundColor = getColor();
  document.body.style.backgroundColor = 'red';

}


chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "ON",
  });
});


chrome.action.onClicked.addListener(async function (tab) {
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
    tabId: tab.id,
    text: nextState,
  });

  if (nextState === "ON") {
    // Insert the CSS file when the user turns the extension on
    await chrome.scripting.executeScript({
      files: ["myscript.js"],
      target: { tabId: tab.id },
    }).then(() => console.log("injected script file"));
  } else {
    await chrome.scripting.executeScript({
      func: changeBackgroundColor,
      target: { tabId: tab.id },
    }).then(() => console.log("injected script file"));

  }

});



