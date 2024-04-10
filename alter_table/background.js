
chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "ON",
  });
});


chrome.action.onClicked.addListener(async function (tab) {


  await chrome.scripting.executeScript({
    files: ["altertable.js"],
    target: { tabId: tab.id },
  }).then(() => console.log("injected script file"));
}

);

