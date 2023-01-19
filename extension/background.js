function injectCode(url, tabid) {
  console.info("injecting into %s", url)

  chrome.tabs.executeScript(tabid, {file: 'inject.js'})
  console.info("injected into %s", url)
}


chrome.webNavigation.onCompleted.addListener(detail => {
  const fid = detail.frameId
  const url = detail.url
  if (fid == null || url == null) {
    return
  }
  if (fid != 0) {
    // only handle main frame
    return
  }
  const tabid = detail.tabId
  injectCode(url, tabid)
})
