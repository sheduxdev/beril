// Frida hook template. Attach: frida -U -f com.example.app -l frida_hook.js --no-pause
// Adapt the class and method names before use. Keep hooks small and log structured lines.

Java.perform(function () {
  var TAG = "[beril]";

  function log(obj) {
    console.log(TAG + " " + JSON.stringify(obj));
  }

  // 1. Inspect a method's arguments and return value.
  try {
    var Cls = Java.use("com.example.app.Login");
    Cls.checkPassword.implementation = function (user, pass) {
      var result = this.checkPassword(user, pass);
      log({ hook: "Login.checkPassword", user: String(user), pass: String(pass), result: String(result) });
      return result;
    };
  } catch (e) {
    log({ error: "Login hook failed", detail: String(e) });
  }

  // 2. Log WebView loads.
  try {
    var WebView = Java.use("android.webkit.WebView");
    WebView.loadUrl.overload("java.lang.String").implementation = function (url) {
      log({ hook: "WebView.loadUrl", url: String(url) });
      return this.loadUrl(url);
    };
  } catch (e) {
    log({ error: "WebView hook failed", detail: String(e) });
  }

  // 3. Log common crypto input and output sizes.
  try {
    var Cipher = Java.use("javax.crypto.Cipher");
    Cipher.doFinal.overload("[B").implementation = function (data) {
      var out = this.doFinal(data);
      log({ hook: "Cipher.doFinal", in_len: data.length, out_len: out.length });
      return out;
    };
  } catch (e) {
    log({ error: "Cipher hook failed", detail: String(e) });
  }
});
