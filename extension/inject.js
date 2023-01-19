now = Date.now().toString()

if (window.injected == undefined) {
   console.info("injecting: %s", now)
   window.injected = now
} else {
   console.info("already injected: %s", window.injected)
}
